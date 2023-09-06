class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Test(metaclass=Singleton):

    def __init__(self, a, b):
        self.a = a
        self.b = b
    def foo(self):
        print (self.a, self.b)
    
obj = Test(5,6)
print (id(obj))
obj1 = Test(10,12)
print (id(obj1))
import pdb;pdb.set_trace()


def singleton(class_):
    class class_w(class_):
        _instance = None
        def __new__(class2, *args, **kwargs):
            if class_w._instance is None:
                class_w._instance = super(class_w, class2).__new__(class2, *args, **kwargs)
                class_w._instance._sealed = False
            return class_w._instance
        def __init__(self, *args, **kwargs):
            if self._sealed:
                return
            super(class_w, self).__init__(*args, **kwargs)
            self._sealed = True
    class_w.__name__ = class_.__name__
    return class_w

@singleton
class MyClass(object):
    def __init__(self, text):
        self.text = text
    def foo(self):
        print (self.text)
    

