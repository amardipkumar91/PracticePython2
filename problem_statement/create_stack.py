#create stack class and implement push, pop and get_max function with 0(1) time complaxity

class Stk:
    def __init__(self, max_limit = 10):
        self.limit = max_limit
        self.stk = []
        self.max_element = []
    
    def push(self, item):
        if len(self.stk) >= self.limit:
            print ("stack is overflow")
        else:
            if len(self.stk) == 0:
                self.stk.append(item)
                self.max_element.append(item)
            else:
                if self.max_element[-1] <= item:
                    self.stk.append(item)
                    self.max_element.append(item)
                else:
                    self.stk.append(item)
    
    def pop(self):
        if len(self.stk) == 0:
            print ("stack is empty")
        else:
            num = self.stk.pop()
            if num in self.max_element:
                self.max_element.pop()
    
    def get_max(self):
        return self.max_element[-1]

obj = Stk()
obj.push(10)
obj.push(5)
obj.push(12)
obj.push(18)
print (obj.get_max())
obj.pop()
print (obj.get_max())