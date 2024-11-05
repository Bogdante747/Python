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

class Library:
    def __init__(self, name, max_books):
        self.name = name
        self.books = []
        self.max_books = max_books

    def __setattr__(self, name, value):
        if name == 'max_books' and hasattr(self, 'max_books'):
            print("Невозможно изменить после инициализации")
        else:
            self.__dict__[name] = value
            if name == 'books' and len(self.books) > self.max_books:
                print("Невозможно добавить книгу, достигнут лимит")

    def __getattribute__(self, name):
        print(f"Доступ к атрибуту: {name}")
        return object.__getattribute__(self, name)

    def __getattr__(self, name):
        print(f"Атрибут {name} не найден")

    def __delattr__(self, name):
        if name == 'name':
            print("Невозможно удалить атрибут name")
        else:
            print(f'Удаление атрибута {name}')
            del self.__dict__[name]

    def add_book(self, book):
        if len(self.books) < self.max_books:
            self.books.append(book)
        else:
            print("Невозможно добавить книгу, достигнут лимит")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print("Книга не найдена в библиотеке")
    
    def list_books(self):
        return self.books
