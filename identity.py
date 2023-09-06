# class Test:
#     def __init__(self, number):
#         self.number = number
    
#     def __repr__(self):
#         return str(self.number)

#     def __eq__(self, other):
#         if isinstance(other, Test):
#             return self.number == other.number
#         return True

# obj = Test(1)
# obj1 = Test([1])
# print (obj == obj1)

#-----------------
# class Test:
#     def __init__(self,pessangers = None):
#         self.pessangers = pessangers

#     def pick(self, name):
#         self.pessangers.append(name)
    
#     def drop(self, name):
#         self.pessangers.remove(name)

# obj = Test(['vicky', 'Amardip'])

# class Test:
#     def __init__(self,pessangers = None):
#         if pessangers is None:
#             self.pessangers = []
#         else:
#             self.pessangers = list(pessangers)

#     def pick(self, name):
#         self.pessangers.append(name)
    
#     def drop(self, name):
#         self.pessangers.remove(name)

# p_list = ['Amardip', 'Vicky', 'Rahul']
# obj = Test(p_list)

#-------------

class Test:
    def __init__(self, a, b):
        self._a = a
        self._b = b
    
    def get_element(self):
        return self._a, self._b

class Test1(Test):
    def get_parent_element(self):
        return self.get_element()

obj = Test1(4,5)
import pdb;pdb.set_trace()


