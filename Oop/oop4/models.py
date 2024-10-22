class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
s1 = Singleton()
s2 = Singleton()

# print(s1 is s2)
# print(s2)
# print(s1)

class Five:
    __instance = None
    __count = 0
    
    def __init__(self):
        Five.__count +=1

    def __new__(cls, *args, **kwargs):
        if Five.__count<5:
            cls.__instance = super().__new__(cls)
        return cls.__instance
        
f1 = Five()
f2 = Five()
f3 = Five()
f4 = Five()
f5 = Five()
f6 = Five()

# print(f1)
# print(f2)
# print(f3)
# print(f4)
# print(f5)
# print(f6)

class Book:
    __instances = {}

    def __new__(cls, title, author, year):
        try:
            return cls.__instances[title, author]
        except KeyError:
            pass

        obj = super().__new__(cls)

        cls.__instances[title, author] = obj

        return obj
    
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
            

b1 = Book("asd", "dsa", "wsx")
b2 = Book("asd", "dsa", "wsx")
print(b1)
print(b2)