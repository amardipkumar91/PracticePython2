class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if self.radius < 0:
            raise ValueError("radius should not be less than 0")
        else:
            self._radius = radius
    
    @property
    def area(self):
        return 3.14 *self.radius ** 2
    


circle = Circle(2)
print (circle.area)

circle.radius = 10
print (circle.area)


# Non Local

def count_func(func):
    count = 0
    def inner():
        nonlocal count
        count = count +1
        print (count)
        func()
    return inner



@count_func
def test():
    print ("First Function test")


test()
test()
test()
test()

@count_func
def test1():
    print ("First Function test1")
test1()

class Singleton:
    _instanse = None
    def __new__(cls,*args, **kwargs):
        if cls._instanse is None:
            cls._instanse = super().__new__(cls, *args, **kwargs)
        return cls._instanse

    

class Singleton_nxt:
    _instanse = {}
    def __new__(cls,*args, **kwargs):
        if cls._instanse not in cls._instanse:
            cls._instanse[cls] = super().__call__(*args, **kwargs)
        return cls._instanse[cls]



        