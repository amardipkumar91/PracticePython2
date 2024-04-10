'''
Open Closed Principle.
Open for extension and closed for modification
The purpose of the open-closed principle is to make it easy to add new features (or use cases) to the system without directly modifying the existing code.
'''

# Example 1.

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @abstractmethod
    def work(self):
        pass

class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    
    def develop(self):
        print ("{} is developing".format(self.name))
    
    def work(self):
        self.develop()

class Tester(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    
    def test(self):
        print ("{} is testing".format(self.name))
    
    def work(self):
        self.test()

class Company(object):
    def __init__(self, name):
        self.name = name
    
    def work(self, employee: Employee):
        employee.work()

comp = Company("L&T")
developer = Developer("Amardip", 10000)
tester = Tester("Swati", 5000)
comp.work(developer)
comp.work(tester)

