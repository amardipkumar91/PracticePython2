def foo(num):
    if num < 2:
        return num
    else:
        return foo(num - 1) + foo( num - 2)

for i in range(10):
    print foo(i)
