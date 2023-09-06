
# Move all zero to begning
# Solution 1:
AA = [0, 3, 5, 0, 7, 2, 6, 9, 0, 0, 4, 8, 11, 6, 0, 8]
def foo():
    lengthA = len(AA)
    write_index = lengthA - 1
    read_index = lengthA - 1
    while(read_index >= 0):
        if AA[read_index] != 0:
            AA[write_index] = AA[read_index]
            write_index -= 1
        read_index -= 1
    while write_index >=0:
        AA[write_index] = 0
        write_index -= 1
    return AA
print (foo())

# Solution 2
AA.sort(key=lambda v: v != 0)
print (AA)


# Move all zero to end
# Solution 1
def fooEnd():
    lengthA = len(AA)
    write_index = 0
    read_index = 0
    while(read_index < lengthA):
        if AA[read_index] != 0:
            AA[write_index] = AA[read_index]
            write_index += 1
        read_index += 1
    while write_index < lengthA:
        AA[write_index] = 0
        write_index += 1
    return AA
print (fooEnd())
# Solution 2
a = [0, 3, 5, 0, 7, 2, 6, 9, 0, 0, 4, 8, 11, 6, 0, 8]
def foo1():
    count = 0
    for i in range(len(a)):
        if a[i] == 0:
            continue
        else:
            a[count] = a[i] 
            count += 1

    while count < len(a):
        a[count] = 0
        count += 1
    print (a)
foo1()

# Solution 3

# Move all zero to end
a.sort(key=lambda v: v == 0)
print (a)


#----------------------
class A(object):
    def __init__(self):
        self.a = 10
        self.b = 20

class B(A):
    def __init__(self,c):
        super().__init__()
        self.c = c

bb = B(50)
print (bb.a, bb.c)

#--------------------
class Test(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def sum(self):
        return self.a + self .b
    
class Test1(Test):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

obj = Test1(10,20,30)
print (obj.a, obj.b, obj.c)
print (obj.sum())
