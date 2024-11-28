def deco(func):
    def inner(*args, **kwargs):
        print ("hi")
        data = func()
        return data
    return inner

@deco
def foo():
    return 10

print (foo())


class Vector:
    def __init__(self, x):
        self.x = x

    
    def __add__(self, y):
        return Vector(self.x+y.x+10)


obj1 = Vector(10)
obj2 = Vector(20)
print (obj1+obj2).x



def set_doc_string():
    '''To check the docstring'''
    return 10

print (set_doc_string())
print (set_doc_string.__doc__)