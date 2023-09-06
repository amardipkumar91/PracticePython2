import os
def priceCheck(products, productPrices, productSold, soldPrice):
    print ("hi")
    d1 = {}
    for i, j in zip(products, productPrices):
        d1[i] = j

    d2 = {}   
    for m, x in zip(productSold, soldPrice):
        if m in d2:
            d2[m].append(x)
        else:
            d2[m] = [x]
    
    error_count = 0
    for key, values in d2.items():
        prouct_price = d1[key]
        for val in values:
            if val != prouct_price:
                error_count = error_count + 1

    return error_count
    
    
    # Write your code here

if __name__ == '__main__':    
    products = ['egg', 'mango', 'oil']
    productPrices = [1.1, 2.2, 3.3]
    productSold = ['egg', 'mango', 'mango', 'oil']
    soldPrice = [1.1, 2.3, 2.3, 3.3]
    
    result = priceCheck(products, productPrices, productSold, soldPrice)

#-----------

import requests
url = 'https://jsonmock.hackerrank.com/api/article_users?page=1'

def getUsernames(threshold):
    rr = requests.get(url = url)
    usernames = []
    data = rr.json()['data']
    for i in data:
        if i['submission_count'] > threshold:
            usernames.append(i['username'])
    return usernames
    # Write your code here

if __name__ == '__main__':
    threshold = int(input().strip())

    result = getUsernames(threshold)
    print (result)

#----------
def a():
    def b():
        c = 0
        def c():
            return
        return c()
    return b()
print (a())

#-------------------

a = b = c = 3
if a:
    a = b = c = 2
if b:
    a = b = c = 1
elif c ==1:
    a = b = c = 0

else:
    print (b)
print (c)

#-----------------
import threading
import time
sem = threading.Semaphore()
def fun(arg):
    sem.acquire()
    print (arg, end= ' ')
    sem.release()
    time.sleep(0.25)
a = lambda b : threading.Thread(target = fun, args=[b])
a('car').start()
a('bus').start()
a('van').start()

#----------

a = 0
b = 1
c = False
a = a or b
a = c or b

#------
y = lambda a,b : a and b + 10
print (y(True, False))

#---------
m = [i for i in range(40)]
print (m[-6] + m[5:][-6])

#-------------
a = (set(list({range(1)})),0)
print (a[0])

#------------
a = 'a'
b = 'b'
ba = c = 'c'
aa = cc = 10
c = eval(c + eval(b + a))
print (c)
#--------

self = 10

def globalself():
    global self
    return self
    ...:

class self:
    def __init__(self):
        return
    self = 'self'
    self = globalself()

print (getattr(self, 'self'))


