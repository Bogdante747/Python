from django.db import models

# Create your models here.
class Product:
    def __init__(self, name, price, discount):
        self._name = name
        self._price = price
        self._discount = discount

    @property
    def price_with_discount(self):
        price = self._price * ((100 - self._discount)/100)
        return price
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, amount):
        if amount < 0:
            raise ValueError("Цена не может быть отрицательной")
        self._price = amount

    @property
    def discount(self):
        return self._discount

    @discount.setter    
    def discount(self, amount):
        if 0 > amount > 100:
            raise ValueError("Скидка не может быть меньше 0 или больше 100")
        self._discount = amount


class Employee:
    def __init__(self, name, salary, age):
        self._name = name
        self._salary = salary
        self._age = age

    @property
    def name(self):
        return self._name
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, amount):
        if amount < 30000:
            raise ValueError("Зарплата не может быть меньше 30к")
        self._salary = amount

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self):
        if self._age == "":
            self._age = None
            
    def apply_raise(self, amount):
        if amount < 0:
            raise ValueError("Укажите положительное число")
        self._salary += amount

p1 = Product("asd", 100, 30)
print(p1.discount)
