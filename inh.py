class Test(object):
    def __init__(self):
        self._a = 10
    
    def dispaly(self):
        return self._a
    
    def __display1(self):
        return self._a
    
    def get_val(self):
        return self.__display1()

class Test1(Test):
    def __init__(self):
        super().__init__()
        self.b = 20

    def foo(self):
        return self.dispaly(), self.b   

obj = Test1()
obj.get_val() 

import pdb;pdb.set_trace()

#---------property---------

class Test:
    def __init__(self):
        self.__name = ''
    
    @property
    def name(self):
        return self.__name + "hello"
    
    @name.setter
    def name(self, val):
        self.__name = val
    
obj = Test()
obj.name = 'Amardip'
import pdb;pdb.set_trace()
print (obj.name)


#---------
# class Person:
#     def __init__(self):
#         self.__name=''
        
#     def setname(self, name):
#         self.__name=name

#     def getname(self):
#         return self.__name
        
#     name=property(getname, setname)

# obj = Person()
# obj.name = "Vicky"
# print (obj.name)
