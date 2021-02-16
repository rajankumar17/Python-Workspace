class Animals:
    animalType = "Mammal"

class Pets:
    color = "White"

class Dog(Pets,Animals):
    @staticmethod
    def bark():
        print("Bow bow!")

d  = Dog()
print(d.color+" "+d.animalType+" makes sound ",end="")
d.bark()