# def palindrome(val):
#     if val == val[::-1]:
#         return "palindrome"
#     else:
#         return "not palindrome"

data = 'thisis'

def longest_palindrome(data):
    n = len(data)
    result = []
    for i in range(n , 0 , -1):
        status = False
        for j in range(n-i+1):
            tmp = data[j : j +i]
            if tmp == tmp[::-1]:
                result.append(tmp)
                status = True
        if status:
            break
    return result
        
print (longest_palindrome(data))

from typing import Counter


def isPalendrome(number):
    if str(number) == str(number)[::-1]:
        print ("yes")
    else:
        print ("no")

duplicates = ['a','b','c','d','d','d','e','a','b','f','g','g','h']
print (duplicates)
dictt = {}
for i in duplicates:
    if i in dictt.keys():
        dictt[i] += 1
    else:
        dictt[i] = 1
print (dictt)


a,b = b,a
a,b,c,d = b,a,d,c
a = b,a,d,c

a = [i for i in range(10)]
b = (i for i in range(10))
c = {i:i for i in range(10)}