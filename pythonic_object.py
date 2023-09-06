from array import array
import math

class Vector2d:
    typecode = 'd'

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __iter__(self):
        return (i for i in (self.a, self.b))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({}, {})'.format(class_name, *self)
    
    def __str__(self):
        return str(tuple(self))
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))
    
    def __format__(self, fmt_spec = ''):
        components = (format(c, fmt_spec) for c in self)
        return 'input is :({}, {})'.format(*components)


obj = Vector2d(5,6)
print (obj)


#_---------------------

from array import array
# import math
# class Vector:
#     typecode = 'd'
#     def __init__(self, components):
#         self._components = array(self.typecode, components)

#     def __len__(self):
#         return len(self._components)
    
#     def __iter__(self):
#         return iter(self._components)
    
#     def __abs__(self):
#         return math.sqrt(sum(x*x for x in self))

#     def __eq__(self, other):
#         return (3 == len(other) and all( a==b for a,b in zip(self,other)))

# obj = Vector([1,2,3])
# obj1 = Vector([1,2,3])
# print (obj == obj1)
# print (len(obj))

#-------------- In Python3
import reprlib
import numbers
import math
class Vector(list):
    typecode = 'd'
    def __init__(self, components):
        self._components = array(self.typecode, components)
        super().__init__(self._components)
    
    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    # def __iter__(self):
    #     return iter(self._components)

    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real):
            return Vector(n * scalar for n in self)
        else:
            raise NotImplemented
    
    # reverse multiplicaton ---
    def __rmul__(self, scalar):
        return self * scalar

    def __matmul__(self, other):
        try:
            return sum(a * b for a , b in zip(self, other))
        except TypeError:
            raise NotImplemented

    def __rmatmul__(self, other):
        return (self @ other)
    
    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integer'
            return TypeError(msg.format(cls = cls))
        


obj = Vector([1,2,3])
data = obj * 10
print ("obj multiply with 10 with help of __mul__ function", data)
data1 = 10 * obj
print ("10 multiply with obj with help of __rmul__ function", data)

obj1 = Vector([10,12, 13])
data2 = obj @ obj1
print ("Two vector object multiply with __matmul__ function", data2)
data3 = [10,20,30] @ obj1
print ("List multiply with obj with @ symbol and __rmatmul__ function", data3)
print ("slice data", obj[1])
print ("slice data", obj[0:2])
print ("slice data", obj['amar'])



