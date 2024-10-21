from django.db import models

# Create your models here.
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
