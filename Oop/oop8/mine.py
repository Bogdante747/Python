class Shop:

    def __init__(self):
        self.goods = []
    def add_product(self, product):
        self.goods.append(product)
    def remove_product(self, product):
        for index in range(len(self.goods)):
            if self.goods[index] == product:
                self.goods.pop(index)
                return
            
class Product:
    __id = 0
    def __new__(cls, *args, **kwargs):
        cls.__id+=1
        obj = super().__new__(cls)
        obj.id = cls.__id
        return obj
    
    def __init__(self, name:str, weight:float, price:float):
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, name: str, value) -> None:
        type_dict = {
            "id": int,
            "name": str,
            "weight": (int, float),
            "price": (int, float),
        }

        if not isinstance(value, type_dict[name]):
            raise TypeError("Неверный тип присваиваемых данных.")
        
        if name == 'weight' and not value > 0:
            raise TypeError("Неверный тип присваиваемых данных.")
        if name == 'price' and not value > 0:
            raise TypeError("Неверный тип присваиваемых данных.")
        super().__setattr__(name, value)

    def __delattr__(self, name: str) -> None:
        if name == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        super().__delattr__(name)