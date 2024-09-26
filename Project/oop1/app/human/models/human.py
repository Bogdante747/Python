class Human:
    height = None
    age = None

human_one = Human()
human_two = Human()

print(human_one.age)
print(human_two.age)

human_one.age = 22
human_two.age = 27

print(human_one.age)
print(human_two.age)

# Говорит, что нету атрибута
# delattr(human_one, 'height') 
# delattr(human_two, 'height')
# а так работает
delattr(Human, 'height')

print(hasattr(human_one, 'height'))
print(hasattr(human_two, 'height'))

human_one.name = "Илья"

print(human_one.name)