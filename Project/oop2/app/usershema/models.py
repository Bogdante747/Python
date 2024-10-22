from django.db import models
from io import TextIOWrapper
import re

# Create your models here.
class UserShema:
    pass

class DataBase:
    def get_data(self, url):
        with open(url, 'r', encoding='UTF-8') as f:
            result = f.readlines()
            f.close()
            return result
        
    def serializers(self, data:TextIOWrapper):
        content = []
        for i in data:
            schema=dict()
            line = [i for i in re.split(r'\s', i) if i != '']
            for index in range(0,len(line)-1, 2):
                schema[line[index]] = line[index+1]
            content.append(schema)
        return content
    
    def create(self, data):
        for i in data:
            user = UserShema()
            for key, item in i.items():
                setattr(user, key, item)


class Translator:
    def __init__(self): 
        self.words = {} 

    def add(self, eng, rus): 
        if eng not in self.words.keys(): 
            self.words[eng] = [] 
        self.words[eng].append(rus) 

    def remove(self, eng): 
        self.words.pop(eng) 

    def translate(self, eng): 
        for i in self.words[eng]: 
            print(i, end=' ') 
        print() 
