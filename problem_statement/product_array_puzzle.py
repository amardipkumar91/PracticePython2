import math 
EPS = 1e-9
def productPuzzle(a, n): 
    sum = 0
    for i in range(n): 
        sum += math.log10(a[i]) 
    for i in range(n): 
        print (int((EPS + pow(10.00, sum - math.log10(a[i])))), ) 
    return
a = [10, 3, 5, 6, 2 ] 
n = len(a) 
print ("The product array is: ")
productPuzzle(a, n)

#-------------Another Approach ----------

def solve(arr,n):
    result = []
    prod = 1
    for i in arr:
        prod *= i
    for i in arr:
        result.append(int(prod*(1/i)))
    return result
arr = [1, 2, 3, 4, 5] 
n = len(arr) 
print (solve(arr, n))