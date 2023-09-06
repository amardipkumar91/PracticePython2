class Celsius:
    def __init__(self, temperature = 0):
        self.temp = temperature

    def to_fahrenheit(self):
        return (self.temp * 1.8) + 32

    # @property
    def get_temp(self):
        return self._temp
    
    # @temp.setter
    def set_temp(self, value):
        if value < -273:
            raise ValueError("It should not be less than -273")
        self._temp = value

    temp = property(get_temp,set_temp)
    
obj = Celsius()
print (obj.temp)
obj.temp = 38
print (obj.to_fahrenheit())


#----------



# class Celsius:
#     def __init__(self, temperature = 0):
#         self.temp = temperature

#     # def to_fahrenheit(self):
#     #     return (self.temp * 1.8) + 32

#     @property
#     def temp(self):
#         return self._temp
    
#     @temp.setter
#     def temp(self, value):
#         if value < -273:
#             raise ValueError("It should not be less than -273")
#         self._temp = value

  
    
# obj = Celsius()

#--------------------------Custom List -------------------

class CustomeList:
    def __init__(self, elements = 1):
        self.mylist = [0] * elements
    
    def __setitem__(self, index, value):
        self.mylist[index] = value
    
    def __getitem__(self, index):
        return "Yous item is {}".format(self.mylist[index])


obj = CustomeList()
obj[0] = 19
print (obj[0])
