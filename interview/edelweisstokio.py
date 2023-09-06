'''1
5
4 9 1 32 13
Sample Output  
3
'''
# Find Minimum difference ----
import copy

def foo(data, n, highest):
    diff = highest
    f_e = l_e = None
    for i in range(n-1):
        for j in range(i+1, n):
            if abs(data[i] - data[j]) < diff:
                diff = abs(data[i] - data[j])
                f_e = data[i]
                f_pos = i
                l_e = data[j]
                l_pos = j

    return diff, f_e, f_pos, l_e, l_pos
data = [4,9,1,32,13]
f_data = copy.copy(data)
data.sort()
first_elemct = data[-1]
last_element = data[-2]
highest = first_elemct * last_element
n = len(data)
diff, f_e, f_pos, l_e, l_pos = foo(f_data, n, highest)
print (diff)
print ("Horse {0} : skill {1}".format(f_pos,f_e ))
print ("Horse {0} : skill {1}".format(l_pos, l_e ))

    
  
  

