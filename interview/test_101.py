# def deco(func):
#     def inner(*args):
#         status = True
#         for i in args:
#             if isinstance(i, int):
#                 status = False
#         if status:
#             result = func(*args)
#             return result
#         else:
#             return "parameter is not integer"
        
#     return inner

# @deco    
# def foo(a,b):
#     return a + b
# print (foo(10,'12'))

# ------ nonlocal -----
# def outer():
#     x = "local"
#     def inner():
#         nonlocal x
#         x = "nonlocal"
#         print ("inner :", x)
#     inner()

#     def inner_1():
#         nonlocal x
#         x = "nonlocal 1"
#         print ("inner_1:", x)
#     inner_1()

#     print ("outer: ", x)
# outer()

#---- context manager---

# class ContextManager():
#     def __init__(self):
#         print ("init called")
    
#     def __enter__(self):
#         print ("enter called")
#         return self
    
#     def __exit__(self, exc_type, exc_valnue, exc_traceback):
#         print ("exit called")

# with ContextManager() as manager:
#     print ("start")

#--- Python Iterator -----
# class Conter():
#     def __init__(self, start, end):
#         self.current = start - 1
#         self.end = end
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current < self.end:
#             next_num = self.current
#             self.current += 2
#             return self.current
#         raise StopIteration
# for i in Conter(5,10):
#     print (i)
       
# Through generator ---
# def counter(low, high):
#     current = low
#     while current < high:
#         yield current
#         current += 1
# for c in counter(10, 20):
#     print (c)

#----- fibonacci generator --

def fibo(num):
    a = 0
    b = 1
    for _ in range(num):
        yield a
        a, b = b , a+ b

print(list(fibo(10)))

