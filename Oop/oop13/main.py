class ShopItem:
    def __init__(self, name, weight, price) -> None:
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self) -> int:
        return hash((self.name, self.weight, self.price))
    
    def __eq__(self, value) -> bool:
        if isinstance(value, ShopItem):
            return self.__hash__() ==  value.__hash__()
        return False
    
item1 = ShopItem("Кружка", 3, 500)
item2 = ShopItem("Ложка", 1, 200)
item3 = ShopItem("Кружка", 3, 500)

print({item1, item2, item3})

class Book:
    def __init__(self, title, author, publisher, year):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year

    def __hash__(self)-> int:
        return hash((self.title, self.author, self.publisher))
    
    def __eq__(self, value) -> bool:
        if isinstance(value, ShopItem):
            return self.__hash__() == value.__hash__()
        return False