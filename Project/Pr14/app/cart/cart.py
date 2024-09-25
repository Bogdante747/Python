from django.contrib.sessions.backends.base import SessionBase
from furniture.models import Furniture

class CartSession(SessionBase):
    CART_SESSION_ID = 'cart'


    def __init__(self, session: dict) -> None:
        self.session : dict = session
        self.cart = self.session.get(self.CART_SESSION_ID)

        if not self.cart:

            self.cart = self.session[self.CART_SESSION_ID] = {}

    def __iter__(self):
        furniture_ids = self.cart.keys()

        furnitures = Furniture.objects.filter(id__in=furniture_ids)

        cart = self.cart.copy()

        for furniture in furnitures:
            cart[str(furniture.id)]['furniture'] = furniture

        for item in cart.values():
            item['price'] = int(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def save(self):
        self.session.modified = True

    def add(self, furniture, quantity=1, update_quantity=False):
        furniture_id = str(furniture.id)

        if furniture_id not in self.cart:
            self.cart[furniture_id] = {'quantity' : 0, 'price' : furniture.price}

        if update_quantity:
            self.cart[furniture_id]['quantity'] = quantity

        else:
            self.cart[furniture_id]['quantity'] += quantity
        self.save()

    def remove(self, furniture):
        furniture_id = str(furniture.id)

        if furniture_id in self.cart:
            if self.cart[furniture_id]['quantity'] > 1:
                self.cart[furniture_id]['quantity'] -= 1
            else:
                del self.cart[furniture_id]
            self.save()

    def get_total_price(self):

        return sum(int(item['price']) * int(item['quantity']) for item in self.cart.values())
    
    
    def clear(self):
        del self.session[self.CART_SESSION_ID]
        self.save()