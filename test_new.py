# def foo():
#     for i in range(10):
#         yield i

# obj = foo()
# for i in obj:
#     print (i)

# def fibo():
#     a = 0
#     b = 1
#     for i in range(10):
#         c = a + b
#         a = b
#         b = c
#         yield c

# obj = fibo()
# for i in obj:
#     print (i)


class Test:
    cc = 8
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    @staticmethod
    def foo(b):
        c = Test.cc
        return c

    @classmethod
    def create_from_list(cls, data):
        return cls(data[0], data[1])
        
obj = Test(10,13)

obj = Test.create_from_list([3,4])
# print obj.foo(6)
print obj.foo(5)
print "---"

# # obj = Test(4,5)


from datetime import date 
  
class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
      
    # a class method to create a Person object by birth year. 
    @classmethod
    def fromBirthYear(cls, name, year): 
        return cls(name, date.today().year - year) 
      
    # a static method to check if a Person is adult or not. 
    @staticmethod
    def isAdult(age): 
        return age > 18
  
person1 = Person('mayank', 21) 
person2 = Person.fromBirthYear('mayank', 1996) 
  
print person1.age 
print person2.age 
  
# print the result 
print Person.isAdult(22) 


def findZeroes(arr, n, m) : 
      
    # Left and right indexes of current window 
    wL = wR = 0
  
    # Left index and size of the widest window  
    bestL = bestWindow = 0
  
    # Count of zeroes in current window 
    zeroCount = 0
  
    # While right boundary of current  
    # window doesn't cross right end 
    while wR < n: 
          
        # If zero count of current window is less than m, 
        # widen the window toward right 
        
        if zeroCount <= m : 
            if arr[wR] == 0 : 
                zeroCount += 1
            wR += 1
  
        # If zero count of current window is more than m, 
        # reduce the window from left 
        if zeroCount > m : 
            
            if arr[wL] == 0 : 
                zeroCount -= 1
            wL += 1
            
  
        # Updqate widest window if 
        # this window size is more 
        
        if (wR-wL > bestWindow) and (zeroCount<=m) : 
            bestWindow = wR - wL 
            bestL = wL 
  
    # Print positions of zeroes  
    # in the widest window 
    
    for i in range(0, bestWindow): 
        if arr[bestL + i] == 0: 
            print (bestL + i)
            
arr = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1] 
m = 2
n = len(arr)    
findZeroes(arr, n, m)  