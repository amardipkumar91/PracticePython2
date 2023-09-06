class ListNode:
    def __init__(self, node = None, next = None, prev = None):
        self._node = node
        self._next = next
        self._prev = prev

    def __repr__(self):
        return repr(self._node)
    
    def set_data(self, data):
        self._node = data
    
    def get_data(self):
        return self._node

    def set_next(self, next):
        self._next = next
    
    def get_next(self):
        return self._next
    
    def has_next(self):
        return self._next != None
    
    def set_prev(self, prev):
        self._prev = prev
    
    def get_prev(self):
        return self._prev
    
    def has_prev(self):
        return self._prev != None

    def __str__(self):
        return "Node[Data = %s]"%(self.get_data())

class DoublyLinkList(object):
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    def __repr__(self):
        nodes = []
        current = self.head
        while current: 
            nodes.append(repr(current))
            current = current.get_next()
        return '[' + ', '.join(nodes) + ']'
    
    def insert_data_at_begning_DL(self, data):
        new_node = ListNode(data, None, None)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.set_prev(None)
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node
    
    def insert_data_at_end_DL(self, data):
        if self.head == None:
            self.head = self.tail = ListNode(data, None, None)
        else:
            current = self.head
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(ListNode(data, None, current))
            self.tail  = current.get_next()
    
    def getNode(self, index):
        currentNode = self.head
        if currentNode == None:
            return None
        i = 0
        while i < index and currentNode.get_next() != None:
            currentNode = currentNode.get_next()
            if currentNode == None:
                break
            i = i + 1
        return currentNode

    def insert_data_at_position_DL(self, data, index):
        new_node = ListNode(data)
        if self.head == None or index == 0:
            self.insert_data_at_begning_DL(data)
        elif index >0:
            tmp = self.getNode(index)
            if tmp == None or tmp.get_next() == None:
                self.insert_data_at_end_DL(data)
            else:
                new_node.set_next(tmp.get_next())
                new_node.set_prev(tmp)
                tmp.get_next().set_prev(new_node)
                tmp.set_next(new_node)

            
            
    
obj = DoublyLinkList()
obj.insert_data_at_begning_DL(56)
obj.insert_data_at_begning_DL(16)
obj.insert_data_at_begning_DL(156)
obj.insert_data_at_begning_DL(65)
print ("insert data at begning in DL", obj)
obj.insert_data_at_end_DL(67)
print ("insert data at end in DL", obj)
obj.insert_data_at_position_DL(776,2)
print ("insert data at end in DL", obj)