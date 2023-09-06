def fibo(n):
    a= 0
    b = 1
    for i in range(n):
        a, b = b , a + b
    return a
print fibo(10)

#time complexity = 0(n)
#space complexity = 0(1)


def fibo2(n):
    fibTable = [0,1]
    for i in range(2, n+1):
        fibTable.append(fibTable[i-1] + fibTable[i-2])
    return fibTable[n]
print (fibo2(10))
#time complexity = 0(n)
#space complexity = 0(n)

#--------------------------

def fibo3(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo3(n-1) + fibo3(n-2)
print (fibo3(10))

#time complexity = 0(2^n) 