# def bar(fun):
#     def inner(*args):
#         print (type(args))
#         fun(*args)
#     return inner

# @bar
# def foo(n):
#     print ("Hi")
# foo(4)

#--- fibonacci ---
dictt = {}
lst = []
def fib(n):
    if n==0:
        dictt[n] = 0
        return 0
    if n < 2:
        dictt[n] = 1
        return 1
    if not dictt.get(n):
        dictt[n] = fib(n-1) + fib(n-2)
    return dictt[n]
fib(5)
for i in range(0,6):
    print (dictt.get(i))

# def bubblesort(arr):
#     n = len(arr)
#     status = True
#     for m in range(len(arr) - 1):
#         if arr[m] > arr[m+1]:
#             status = False
#     if not status:
#         for j in range(n-1,0,-1):
#             for i in range(j):
#                 if arr[i] > arr[i+1]:
#                     tmp = arr[i]
#                     arr[i] = arr[i+1]
#                     arr[i+1] = tmp
#     else:
#         print ("already sorted")
#     return arr
# lst =  [1, 2, 3, 4 ,5, 7, 6]
# print (bubblesort(lst))

#-------- Binary Search ---
# Time Complexity : log2 (n)
def binarySearch(arr, num):
    first = 0
    last = len(arr) - 1
    found = False
    while (first <= last) and not found:
        mid = (first + last)//2
        print (mid)
        if arr[mid] == num:
            found = True
        else:
            if num < arr[mid]:
                last = mid -1
            else:
                first = mid + 1
    return found
print(binarySearch([1,2,3,5,8], 6))


# import functools
# @functools.l
# def factorial(n):
#     print ("nn")
#     return n * factorial(n-1) if n else 1

# factorial(10)

def swap_case(s):
    result = ''
    for i in s:
        
        if i.isupper():
            result = result + i.lower()
        elif i.islower():
            result = result + i.upper()    
        else:
            result = result + i      
    return result

if __name__ == '__main__':
    # s = input()
    s = 'HackerRank.com presents "Pythonist 2".'
    result = swap_case(s)
    print(result)