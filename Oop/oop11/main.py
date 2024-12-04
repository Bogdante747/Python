class Book:
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author

class Library:
    def __init__(self):
        self.data = None

def __add__(self, other):
    if not self.data.get(other.author):
        self.data[other.author] = [other]
        return self
    self.data[other.author].append(other)

    return self

def __sub__(self, other):
    if other.author not in self.data.keys():
        return
    
    if not len(self.data[other.author]):
        del self.data[other.author]
        return self
    self.data.pop(other.author)

    return self

lib = Library()

book = Book("Горе от ума", "Александр Грибоедов", 1825)
book2 = Book("Портрет Дормана Грея", "Оскар Уайльд", 2020)

lib + book
lib + book2

lib - book
print(lib.data)