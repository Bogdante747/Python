from django.db import models
import re
from string import ascii_lowercase, digits

# Create your models here.
class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        pattern = r'^\d{4}-\d{4}-\d{4}-\d{4}$'
        return bool(re.match(pattern, number))
    
    @classmethod
    def check_name(cls, name):
        words = name.split()
        if len(words) != 2:
            return False
        
        first_name, last_name = words
        return all(char in cls.CHARS_FOR_NAME for char in first_name) and all(char in cls.CHARS_FOR_NAME for char in last_name)
    
class TemperatureConverter:
    celsius = 0
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        fahrenheit = 1.8 * celsius + 32
        return fahrenheit
    
    @classmethod
    def from_kelvin(cls, kelvin):
        celsius = kelvin - 273
        cls.celsius = celsius
        return celsius
    

class Employee:

    @staticmethod
    def is_valid_age(age):
        if age < 18:
            return "Молодой"
        elif age > 65:
            return "Старый"
        else:
            return age
        
    @classmethod
    def from_string(cls, name, age, post):
        if 65 >= age >= 18:
            cls.name = name
            cls.age = age
            cls.post = post
            return "Четко"
        else:
            raise ValueError("Не повезло, не фортануло")
        
    @classmethod
    def get_details(cls):
        return f"Имя: {cls.name}, Возраст: {cls.age}, Должность: {cls.post}"
    
e1 = Employee()

print(e1.from_string("asd", 20, "ad"))
print(e1.get_details())