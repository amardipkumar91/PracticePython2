'''
Q2. Define a class Person. Person should have 2 attributes- name(string) and age(int).
1. Store 5 objects of Person class in a list.
2. Print the list
3. Sort the list according to the name of Person objects.
4. Print the list again
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return str(self.name) +" "+ str(self.age)

lst = []    
lst.append(Person("Amardip", 30))
lst.append(Person("vicky", 25))
lst.append(Person("Rahul", 25))
lst.append(Person("Monu", 25))
lst.append(Person("Sonu", 25))
lst.append(Person("Rahul", 28))
lst.sort(key = lambda x: (x.name, -x.age))
print (lst)

#---- sort list of dictonary------
lst = [{'name': 'Amardip', 'age' : 23}, {'name': 'Ama', 'age' : 30}, {'name': 'Ama', 'age' : 32}]
lst.sort(key = lambda x: (x['name'], -x['age']))
print (lst)


import time
import datetime
import functools
def timer(func):
    @functools.wraps(func)
    def inner(*args):
        start_time = datetime.datetime.now()
        func(*args)
        end_time = datetime.datetime.now()
        print ("time taken by function: ", func.__name__, end_time - start_time)
    return inner
@timer
def test(n):
    print ("hello", n)
    time.sleep(1)
test(5)
print (test.__name__)



