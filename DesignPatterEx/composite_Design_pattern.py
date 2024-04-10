''' 
The Composite Design Pattern is a structural design pattern that 
lets you compose objects into tree structures to represent part-whole hierarchies. 
Composite allows clients to treat individual objects and compositions of objects uniformly.
'''




class LeafElement:
    def __init__(self, *args):
        self.position = args[0]
    
    def showDetails(self):
        print ("\t", end = "")
        print (self.position)



class CompositeElement:
    def __init__(self, *args):
        self.position = args[0]
        self.children = []
    
    def add(self, child):
        self.children.append(child)
    
    def remove(self, child):
        self.children.remove(child)
    
    def showDetails(self):
        print (self.position)
        for child in self.children:
            print ("\t", end = "")
            child.showDetails()


if __name__ =='__main__':
    top1 = CompositeElement("General Manager")
    top2 = CompositeElement("Manager")
    top3 = CompositeElement("Manager")

    top12 = LeafElement("Developer1")
    top13 = LeafElement("Developer2")
    top14 = LeafElement("Developer3")

    top2.add(top12)
    top2.add(top13)

    top3.add(top14)

    top1.add(top2)
    top1.add(top3)

    top1.showDetails()








    





