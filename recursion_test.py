#-----------Factorial ----------
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n -1)
print (factorial(0))
print("------------")
def fibonnaci(num):
    # import pdb;pdb.set_trace()
    if num <= 1:
        return num
    else:
        return (fibonnaci(num-1) + fibonnaci(num -2))

for i in range(10):
    print (fibonnaci(i))
#----------------------------
def append_at_begning_front(x, l):
    return [x + element for element in l]
def bit_string(n):
    if n==0:
        return []
    if n==1:
        return ["0", "1"]
    else:
        return (append_at_begning_front("0", bit_string(n -1)) + append_at_begning_front("1", bit_string(n -1)))
print (bit_string(3))
print ("--------")
def bit_string_next(n):
    if n==0:
        return []
    if n==1:
        return ["0", "1"]
    else:
        return [ i + j for i in bit_string_next(1) for j in bit_string_next(n - 1)]
print (bit_string_next(3))
print ("----------------------")

def foo(x, y):
    if x ==0:
        return y
    else:
        return foo(x-1, x +y)
print (foo(5, 2))

print ("---------")
def bar(n):
    if n == 4:
        return n
    else:
        return 2 * bar(n + 1)
print (bar(2))