# class CustomDict(dict):
#     def __init__(self,data):
#         self.data = data
#         super(CustomDict, self).__init__()

#     def __str__(self):
#         return str(self.data) 
        
#     def __getitem__(self, key)
#         return self.data[key]
    
#     def __setitem__(self, key, val):
#         self.data.update({key : val})
   

# abc = {'a':4, 'b' :5}
# obj = CustomDict(abc)
# print (obj['a'])

# print (obj)

#--------------__missing__--------------


# class StrKeyDict0(dict):
#     def __missing__(self, key):
#         if isinstance(key, str):
#             raise KeyError(key)
#         return self(str(key))
    
#     def get(self, key, default = None):
#         try:
#             return self[key]
#         except:
#             return default
    
#     def __contains__(self, key):
#         return key in self.keys() or str(key) in self.keys()

# d = {4:5}
# obj = StrKeyDict0(d)
# print obj
# print obj.get('6')

#--------------------------


    

        
    
# class Celsius:
#     def __init__(self, temperature = 0):
#         self.temperature = temperature

#     def to_fahrenheit(self):
#         return (self.temperature * 1.8) + 32

#     def get_temperature(self):
#         print("Getting value")
#         return self._temperature

#     def set_temperature(self, value):
#         if value < -273:
#             raise ValueError("Temperature below -273 is not possible")
#         print("Setting value")
#         self._temperature = value
    
#     temperature = property(get_temperature,set_temperature)

# obj = Celsius()
# obj.temperature = 45
# print obj.to_fahrenheit()



# class Test(object):
#     def __init__(self):
#         self.__a = "amardip"
    
#     @staticmethod
#     def __foo():
#         return "vicky"
    
#     def bar(self):
#         return self.__foo()
    
# obj = Test()


#----------------------USER DEFINED CALLABLE TYPE ------------- 

import random
class TestCallable(object):
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except:
            raise IndexError

    def __call__(self):
        self.pick()

obj =  TestCallable(range(10))