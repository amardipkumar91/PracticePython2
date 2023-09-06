#-----------------------Functool Wrap-------------------
import functools
user = {'username' : 'Amardip', 'access_level' : "guest"}


def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function():
            if user['access_level'] == access_level:
                return func()
            else:
                return f"No {access_level} permission for user {user['username']}"    
        return secure_function    
    return decorator

@make_secure("admin")
def get_admin_password():
    return "admin: 1234"
 
@make_secure("guest")
def get_dashboard_password():
    return "user: user_password"

import pdb;pdb.set_trace()
print (get_admin_password())
print (get_dashboard_password())

user = {'username' : 'vicky', 'access_level' : "admin"}

print (get_admin_password())
print (get_dashboard_password())


def deco(func):
    print ("1")
    def inner(*args):
        print ("2")
        result = func(*args)
        return result
    return inner

@deco
def add(a,b):
    return a+ b
[add(i, i+1) for i in range(10)]
