1.

# from multiprocessing import Queue
# import multiprocessing

# def test(q):
#     print (q.qsize())

# if __name__ == "__main__":
#     q = Queue()
#     for i in range(100):
#         q.put(i)
#     p = multiprocessing.Process(target=test, args= (q,))
#     p.start()
#     p.join()

2.
# a = {}
# a[(1,2,4)] = 8
# a[(4,2,1)] = 10
# a[(1,2)] = 12
# sum = 0
# for k in a:
#     sum += a[k]
# print len(a) + sum

3.

# def foo():
#     print "0: start"
#     print "1: start"
#     print "2: start"
#     x = raw_input("selection:")
#     try:
#         num = int(x)
#         if num > 2 and num <0:
#             return None
#         return num
#     except:
#         return None
    
# num = foo()
# if not num:
#     print "invalid"
# else:
#     print "valid"

4. 

# def my_func(x, y):
#     return x /y

# for i in range(100):
#     print (my_func(1, 100 -i))

5.

# from threading import Timer
# i = 0
# def foo():
#     global i
#     i += 1
#     print (i)
#     if i > 5:
#         exit()
# if __name__ == "__main__":
#     c = Timer(1, foo)
#     c.start()
#     c.join()


6.
# def sum(a, b):
#     print (a + b)

# def my_func(a, b):
#     def sum(a, b):
#         return a**2 + 2*a*b + b**2

# sum(10,10)
# my_func(10,10)
# locals()["sum"](10,10)
# globals()["sum"](10,10)

7.

# print r"\nRicha"



class MyMeta(type):
    pass
class Myclass(metaclass=MyMeta):
    pass
class Mysubclass(Myclass):
    pass
