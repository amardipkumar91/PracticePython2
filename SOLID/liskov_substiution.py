'''
The Liskov Substitution Principle states that objects of a superclass should be replaceable with objects of its subclasses\
      without affecting the correctness of the program. In simpler terms, if a program is using a base class, \
        it should be able to work correctly with any derived class without causing unexpected behaviors or breaking the program’s functionality.
'''

class Shape:
    def area(self):
        pass


class Rectangle:
    def __init__(self, width, hight):
        self.width = width
        self.hight = hight
    
    def area(self):
        return self.width * self.hight
    

class Square:
    def __init__(self, side):
        super.__init__(side, side)
    
    def area(self):
        return self.side * self.side
        

def make_area(shape):
    shape.area()

if __name__ == "__main__":
    rectangle = Rectangle(5,4)
    print (make_area(rectangle))