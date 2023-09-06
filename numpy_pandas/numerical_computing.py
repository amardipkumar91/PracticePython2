import numpy as np

a = [1,2,3,4]
b = [10,11,12,13]

a_array = np.array(a)
b_array = np.array(b)

print (a_array + b_array)
print (a_array ** b_array)

print (a_array.dtype)

a_array[0] = 100
print (a_array)

a_array[1] = 10.9
print (a_array)

x = np.array([1,2,3,4.7], dtype='int64')
print (x.dtype)
print (x)

td_element = [ [1,2,3,4], [10,11,12,13] ]
td = np.array(td_element)
print(td.shape)


a = np.arange(0,80,10)
indices = [1,2,-3]
y = a[indices]
print (y)

a = np.array([1,2,3,-6,4,-5,-7])
neg_element = a<0
a[neg_element]

a[a<0] = 0

np.nonzero(a)

#dignol

ar = np.arange(36).reshape(6,6)

ar[3:,[0,2,5]]
