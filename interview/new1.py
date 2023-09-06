 # 1. Difference between list and tuple.
 # 2. What is generator.
 # 3. Decorator
 # 4. write palindrome that if string is palindrome or not.
 # 5. what is list comprehension.
 # 6. context manager in python
 # 7. what is super.
 # 8. Global, local and nonlocal difference.
 # 9. what is super .
 # 10 lambda in python

 # --- Mysql.
# how many types of join.
# diff between left and right join.
# indexing in mysql

# -- Django --
# eloborate the django cycle.
# middleware in django


def welcome(func):
    def wrapper(*args):
        print("Welcome")

        return func(*args)
    return wrapper

@welcome
def s(a, b, c):
    
    print(a + b + c)

s(10, 20, 30)

class a(object):
    def f(self):
        print ("hello")
class b(a):
    def f(self):
        super().f()
        print("hi")


c = b()

c.f()

a = [i for i in range(20) if i % 2 == 0]