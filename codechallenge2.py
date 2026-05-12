class Animal():
    def sound(self):
        return "Sound"
    
class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Mewo"
    
animal = Animal()
dog = Dog()
cat = Cat()

animal_list = [animal, dog, cat]
for animal in  animal_list:
    print(animal.sound())