'''
The Interface Segregation Principle is a part of the SOLID principles of object-oriented programming. \
    It states that a client should not be forced to depend on interfaces it does not use. In other words, \
        classes should be designed with small, focused interfaces that are tailored to the needs of their clients.

'''
from abc import ABC, abstractmethod
class Walk(ABC):
    @abstractmethod
    def walk(self):
        pass


class Swim(ABC):
    @abstractmethod
    def swim(self):
        pass


class Amphibian(Walk,Swim):
    def walk(self):
        print ("can walk")
    
    def swim(self):
        print ("can swim")

class OnlyWalkAnimal(Walk):
    def walk(self):
        print ("can walk")


class OnlySwimAnimal(Swim):
    def swim(self):
        print ("can swim")



def walking_style(animal):
    animal.walk()

def swimming_style(animal):
    animal.swim()



if __name__ == '__main__':
    aligator = Amphibian()
    walking_style(aligator)
    swimming_style(aligator)

    fish = OnlySwimAnimal()
    swimming_style(fish)

    




