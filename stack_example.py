#--------------------------STACK IMPLEMENTATION ------------------------
class Stack(object):
    def __init__(self, limit = 10):
        self.limit = limit
        self.stk = []
    
    def is_empty(self):
        return len(self.stk)
    
    def push(self, data):
        if len(self.stk) >= self.limit:
            print ("stack is overflow")
        else:
            self.stk.append(data)
        print ("After push data stack is ", self.stk)
    
    def pop(self):
        if len(self.stk) <= 0:
            print ("stack is empty")
        else:
            self.stk.pop()
        print ("After pop stack is ", self.stk)

    def size(self):
        return len(self.stk)


# obj = Stack()
# obj.push(10)
# obj.push(20)
# obj.push(20)
# print ("size of stak is", obj.size())
# obj.pop()

#--------------Dynamic Array Implementation -------------------------

# class Stack(object):
    def __init__(self, limit = 10):
        self.stk = limit*[None]
        self.limit = limit
    
    def is_empty(self):
        return len(self.stk) <=0
    
    def size(self):
        return len(self.stk)
    
    def push(self, item):
        if len(self.stk) >= self.limit:
            self.resize()
        self.stk.append(item)
        print ("Stack after PUSH :-", self.stk)
    
    def pop(self):
        if len(self.stk) <= 0:
            print ("stack is empty")
        else:
            return self.stk.pop()
    
    def resize(self):
        newStk = list(self.stk)
        self.limit = self.limit * 2
        self.stk = newStk

# obj = Stack(6)
# obj.push(10)
# obj.push(12)
# obj.push(14)
# obj.push(18)
# obj.push(31)
# import pdb;pdb.set_trace()

#----------------Check Balanced symbol using Stack--------

