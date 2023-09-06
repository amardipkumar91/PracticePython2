# class Test(object):
#     def __init__(self, n):
#         self.n = n

#     def __add__(self, number):
#         return self.n + number
    

# num = Test(10)
# print (num + 5)


#------------j-

# class Test(object):
#     def __foo(self):
#         print " I am A class Method"
    
#     def foo(self):
#         self.__foo()
    
# obj = Test()
# obj.foo()

#------------

# class A(object):
#     def __foo(self):
#         print " I am A class Method"
    
#     def foo(self):
#         self.__foo()

# class B(A):
#     def __foo(self):
#         print "I am B class Method"

# obj = A()
# obj.foo()

#------------Call Function -------


# class A(object):
#     def __call__(self, a, b):
#         return a + b

# a = A()
# print a(4,5)

#-----------------------------Implement Queue using stack -----------

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def enQueue(self, x):
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
        self.s1.append(x)
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def deQueue(self):
        if len(self.s1) == 0:
            print ("queue is empty")
        x = self.s1[-1]
        self.s1.pop()
       
        return x

obj = Queue()
obj.enQueue(1)
obj.enQueue(2)
obj.enQueue(3)
obj.deQueue()

#--------------

# class Queue:
#     def __init__(self):
#         self.s1 = []

#     def enQueue(self, x):
#         self.s1.append(x)
    
#     def deQueue(self):
#         if len(self.s1) == 0:
#             print ("queue is empty")
#         self.s1 = self.s1[::-1]
#         import pdb;pdb.set_trace()
#         x = self.s1[-1]
#         self.s1.pop()
#         self.s1 = self.s1[::-1]
#         return x

# obj = Queue()
# obj.enQueue(1)
# obj.enQueue(2)
# obj.enQueue(3)
# import pdb;pdb.set_trace()
# obj.deQueue()






#-------------------------Implemet Stack using Queue ---------------

from queue import Queue 
class Stack: 
      
    def __init__(self): 
          
        # Two inbuilt queues  
        self.q1 = Queue() 
        self.q2 = Queue()  
              
        # To maintain current number  
        # of elements 
        self.curr_size = 0
  
    def push(self, x): 
        self.curr_size += 1
        # Push x first in empty q2  
        self.q2.put(x)  
  
        # Push all the remaining  
        # elements in q1 to q2.  
        import pdb;pdb.set_trace()
        while (not self.q1.empty()): 
            self.q2.put(self.q1.queue[0])  
            self.q1.get() 
  
        # swap the names of two queues  
        self.q = self.q1  
        self.q1 = self.q2  
        self.q2 = self.q 
  
    def pop(self): 
  
        # if no elements are there in q1  
        if (self.q1.empty()):  
            return
        import pdb;pdb.set_trace()
        self.q1.get()  
        self.curr_size -= 1
  
    def top(self): 
        if (self.q1.empty()): 
            return -1
        return self.q1.queue[0] 
  
    def size(self): 
        return self.curr_size 
  
# Driver Code  
if __name__ == '__main__': 
    s = Stack() 
    s.push(1)  
    s.push(2)  
    s.push(3)  
    import pdb;pdb.set_trace()
    print("current size: ", s.size()) 
    # print(s.top())  
    s.pop()  
    # print(s.top())  
    s.pop()  
    # print(s.top())  
  
    print("current size: ", s.size()) 

#-------------bubble sort ----------

alist = [54,26,93,17,77,31,44,55,20]
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

bubbleSort(alist)
print(alist)

#-------------selection sort -----------
def selection_sort(alist):
    for i in range(len(alist)-1 , 0 , -1):
        pom = 0
        for j in range(1, i +1 ):
            if alist[j] < alist[pom]:
                pom = j
            tmp = alist[i]
            alist[i] = alist[pom]
            alist[pom] = tmp
    return alist

print (selection_sort([3,6,1,5]))



