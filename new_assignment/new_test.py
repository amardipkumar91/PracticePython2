# aa = [1,5,0,6,8,0]
# aa_out = [1,5,6,8,0,0]
# def foo():
#     len_aa = len(aa)
#     ww = 0
#     rr = 0
#     while (rr < len_aa):
#         if aa[rr] != 0:
#             aa[ww] = aa[rr]
#             ww += 1
#         rr += 1
#     while ww < len_aa:
#         aa[ww] = 0
#         ww += 1
#     return aa     
# print (foo())

class Stack(object):
    def __init__(self):
        self.lst = []

    def get_size(self):
        return len(self.lst)

    def push(self, elemnt):
        if self.get_size() == 10:
            print ("Stack is full")
        else:
            self.lst.append(elemnt)
    
    def pop(self):
        if self.get_size() ==0 :
            print ("underflow")
        else:
            self.lst.pop()

    def peek(self):
        if self.get_size() ==0:
            print ("unserflow")
        else:
            return self.lst[-1]

    def insert(self, element, pos):
        if self.get_size() == 10:
            print ("Stack is full")
        else:
            self.lst.insert( pos, element)

obj = Stack()
# obj.push(10)
# obj.push(20) 
# obj.pop()
# obj.pop()
# obj.pop()
# print (obj.peek())
# obj.push(10)
# obj.push(20) 
# obj.insert(30, 12) 
# def sum(x,y):
#     return x+y
# sum(1,2) =3
# sum('a', 'b') = ab
# sum(2,'a') = error


aa = [[1 , 2 , 3 , 4], 
 [5, 6,7, 8], 
 [9, 10, 11, 12 ], 
[13, 14, 15, 16 ]]

n = 4
def foo(): 
    result = [] 
    for i in range(0,n):
        result.append(aa[i][i])
    return result 
print (foo())

global l
def Exe(v, l=[4,6]):
    l = [7,8]
    l.append(v)
    return l
print(Exe(1,[2,3]))


