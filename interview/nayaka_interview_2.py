# # check no of frequency of the word and return it in the descresing order.

import operator
sample_input = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
l_dict = {}
for i in sample_input:
    if i in l_dict:
        l_dict[i] += 1
    else:
        l_dict[i] = 1
result = dict(sorted(l_dict.items(), key=operator.itemgetter(1), reverse=True)[0:3])
print (result)     

''' Find Largest time from the number :
    input = [1,2,3,4]
    output = 23:41
'''
def get_number_frequency(arr):
    from collections import Counter
    return dict(Counter(arr))

def check_val(mapped_val, val):
    if val in mapped_val:
        mapped_val[val] -= 1
        return True
    return False

def getMax_time(arr, n):
    time_value = ""
    flag = False
    mapped_val = get_number_frequency(arr)
    
    for i in range(2,-1,-1):
        if check_val(mapped_val, i):
            time_value += str(i)
            flag = True
            break
    if not flag:
        return ""
    flag = False
    
    if time_value[0] == 2:
        for i in range(3,-1,-1):
            if check_val(mapped_val, i):
                flag = True
                time_value += str(i)
            break
    else:
        for i in range(9, -1, -1):
            if check_val(mapped_val, i):
                flag = True
                time_value += str(i)
                break
    time_value += ":"
    if not flag:
        return ""
    flag = False
  
    for i in range(5,-1,-1):
        if check_val(mapped_val, i):
            flag = True
            time_value += str(i)
            break
   
    if not flag:
        return ""
    flag = False

    for i in range(9,-1,-1):
        if check_val(mapped_val, i):
            flag = True
            time_value += str(i)
            break


    return time_value

if __name__ == "__main__":   
    arr = [2,2,2,2] 
    n = len(arr)
    print(getMax_time(arr, n)) 
