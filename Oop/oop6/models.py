class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self._author = author
        self.__pages = pages
    
    def get_author(self):
        return self._author
    
    def set_author(self, author):
        self._author = author

    def get_pages(self):
        return self.__pages
    
    def set_pages(self, pages):
        if pages > 0:
            self.__pages = pages
        else:
            raise ValueError("Количество страниц должно быть положительным числом")
        
    def display_info(self):
        return f"Название: '{self.title}', Автор: {self._author}, Страниц: {self.__pages}"
    
# b1 = Book("asd", "dsa", 10)
# b1.set_author("DSA")
# b1.set_pages(10)
# print(b1.display_info())

class Car:
    def __init__(self, model, year, mileage):
        self.model = model
        self._year = year
        self.__mileage = mileage

    def get_year(self):
        return self._year
    
    def set_year(self, year):
        if 1885 < year < 2025:
            self._year = year
        else:
            raise ValueError("Неверно указан год")
    
    def get_mileage(self):
        return self.__mileage
    
    def set_mileage(self, mileage):
        if mileage > 0:
            self.__mileage = mileage
        else:
            raise ValueError("Пробег должен быть указан положительным числом")
        
    def display_info(self):
        return f"Модель: '{self.model}', Год: {self._year}, Пробег: {self.__mileage}"
        
c1 = Car("BMW", 1234, 4321)
c1.set_year(2020)
c1.set_mileage(100200)
print(c1.display_info())


