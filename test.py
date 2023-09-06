# class A(object):
#     def __init__(self):
#         print "A init"

#     # def foo(self):
#     #     print ("A")
    
    

# class B(object):
#     def __init__(self):
#         print "B init"

#     def foo(self):
#         print "B"


# class E(B):
#     def __init__(self):
#         super(E, self).__init__()
#         print "E init"

#     def foo(self):
#         super(E, self).foo()
#         print "E"
    
# class D(E):
#     pass

# obj = D()
# obj.foo()




# ## --------------Decorator ---------------
# def test(func):
#     def inner(*args, **kwargs):
#         print "welcome"
#         func(*args, **kwargs)
        
#     return inner

# @test
# def test_deco():
#     print "hi"
# test_deco()


# #-------------Count of total anagram substrings--------------------
# def countOfAnagramSubstring(s): 
#     n = len(s) 
#     mp = dict() 
#     for i in range(n): 
#         sb = '' 
#         for j in range(i, n):   
#             sb = ''.join(sorted(sb + s[j])) 
#             mp[sb] = mp.get(sb, 0) 
#             mp[sb] += 1
#     anas = 0
#     for k, v in mp.items(): 
#         anas += (v*(v-1))//2
#     return anas 
# s = ["aa", "aa", "dog", "god"]
# print(countOfAnagramSubstring(s))

#----------------------------------

# class Test(object):
#     def __init__(self, a,b):
#         self.a = a
#         self.b = b

#     def sum(self):
#         result = self.a + self.b
#         print (result)

# class Test1(Test):
#     def __init__(self, a, b, c):
#         super().__init__(a, b)
#         self.c = c

#     def sub(self):
#         # super(Test1, self).sum()
#         result = self.a + self.b + self.c
#         return result

# obj = Test1(5,6,7)
# print (obj.sub())
# print (obj.__new__)



class Student(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    @classmethod
    def from_string(cls, name_str):
        first_name, last_name = map(str, name_str.split(' '))
        student = cls(first_name, last_name)
        return student
    
    def full_name(self, first_name, last_name):
        return (self.first_name + self.last_name)

scott = Student('Scott',  'Robinson')

scott = Student.from_string('Ammardip Kumar')






