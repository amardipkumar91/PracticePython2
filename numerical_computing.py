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


