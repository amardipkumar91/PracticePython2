class ListNode:
    def __init__(self, node = None, next = None):
        self._node = node
        self._next = next
    
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
             self._next != None
    
class SinglyLinkList(object):
    def __init__(self, head = None):
        self.head = None
        self.length = 0

    def __repr__(self):
        nodes = []
        current = self.head
        while current: 
            nodes.append(repr(current))
            current = current.get_next()
        return '[' + ', '.join(nodes) + ']'

    def get_linklist_length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def insert_data_at_beginning(self, data):
        new_node = ListNode()
        new_node.set_data(data)
        if self.length == 0:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
        self.length += 1
    
    def insert_data_at_ending(self, data):
        new_node = ListNode()
        new_node.set_data(data)
        current = self.head
        while current.get_next() != None:
            current = current.get_next()
        current.set_next(new_node)
        
        self.length += 1
    
    def insert_data_at_middle(self, pos, data):
        if pos > self.length and pos < 0:
            return None
        else:
            if pos == 0:
                self.insert_data_at_beginning(data)
            elif pos == self.length:
                self.insert_data_at_ending(data)
            else:
                new_node = ListNode()
                new_node.set_data(data)
                count = 1
                current = self.head
                while count < pos -1:
                    count +=1
                    current = current.get_next()
                new_node.set_next(current.get_next())
                current.set_next(new_node)
                self.length +=1

    def delete_data_at_begning(self):
        if self.length ==0:
            print ("list is empty")
        else:
            self.head = self.head.get_next()
            self.length -= 1

    def delete_data_at_end(self):
        if self.length == 0:
            print ("list is empty")
        else:
            currentNode = self.head
            previousNode = self.head
            while currentNode.get_next() != None:
                previousNode = currentNode
                currentNode = currentNode.get_next()
            previousNode.set_next(None)
            self.length -= 1

    def delete_from_list_with_node(self, node):
        if self.length == 0:
            print ("Link list is empty")
        else:
            current = self.head
            previous = None
            found = False

            while not found:
                if current.get_data() == node.get_data():
                    found = True
                elif current is None:
                    raise ValueError("Node Not in linklist")
                else:
                    previous = current
                    current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        self.length -= 1

    # def delete_from_list_by_value(self, value):
    #     currentNode = self.head
    #     previousNode = self.head
    #     # import pdb;pdb.set_trace()
    #     while currentNode.get_next() != None and currentNode.get_data() != value:
    #         print currentNode.get_data()
    #         if currentNode.get_data() == value:
                
    #             previousNode = currentNode.get_next()
    #             self.length -= 1
    #         else:
    #             previousNode = currentNode
    #             currentNode = currentNode.get_next()

    # def delete_list_by_position(self, pos):
    #     count = 0
    #     currentNode = self.head
    #     previousNode = self.head
    #     if pos > self.length or pos <0:
    #         print ("This position does not exist in the linklist")
    #     else:
    #         while currentNode.get_next() != None or count < pos:
    #             count = count + 1
    #             if count == pos:
    #                 previousNode.set_next(currentNode.get_next())
    #                 self.length -= 1
    #                 return
    #             else:
    #                 previousNode = currentNode
    #                 currentNode.set_next(currentNode.get_next())

    

obj = SinglyLinkList()
obj.insert_data_at_beginning('a')
obj.insert_data_at_beginning(23)
obj.insert_data_at_beginning(123)
obj.insert_data_at_beginning(1234)
obj.insert_data_at_beginning('hj')
obj.insert_data_at_beginning('hj1')
print ("Link List is :--", obj)
obj.insert_data_at_ending(90)
print ("Link list is after inserting at end", obj)
print ("Length of linklist is :--", obj.get_linklist_length())
obj.insert_data_at_middle(2, 555)
print ("link list after inserting the data at middle", obj)
obj.delete_data_at_begning()
print ("After delete link list is :--", obj)
obj.delete_data_at_end()
print ("After detete from end link list is :--", obj)

d_node = ListNode(1234, 123)
obj.delete_from_list_with_node(d_node)
print ("After delete the node link list is :", obj)

# obj.delete_from_list_by_value(23)
# print ("After delete the node by value link list is :", obj)

# obj.delete_list_by_position(2)
# print ("After delete the node by postion link list is :", obj)




    