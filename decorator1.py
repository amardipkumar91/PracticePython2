def outer_d(active = True):
    def inner(func):
        if active:
            print ("Welcome")
            return func
    return inner

@outer_d()
def foo(n):
    print ("amardip", n)
foo(15)