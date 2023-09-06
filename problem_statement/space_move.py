
#Move the space infrot of string that contains some character. But you have to iterate only one time.

#1. Solution 1

def move_string_begin(user_string):
    i = len(user_string) - 1
    datalist = list(user_string)
    j = i
    for j in range(i , -1, -1):
        if not datalist[j].isspace():
            tmp = datalist[i]
            datalist[i] = datalist[j]
            datalist[j] = tmp
            i -=1
    user_string = "".join(datalist) 
    return user_string
user_string = "My Name is Amardip Kumar"
print (user_string), "\n",move_string_begin(user_string)

#2 Solution 2
def move_string_begin_2(user_string):
    nospace_char = [i for i in user_string if i != ' ']
    len_str = len(user_string)
    spaces = len_str - len(nospace_char)
    result = ' '*spaces
    result = result + "".join(nospace_char)
    return result
user_string = "My Name is Amardip Kumar"
print (user_string), "\n",move_string_begin_2(user_string)

# move all zero to last of list but remain all the items order should be same

#solution 1
def move_zero_to_end(lst):
    non_zero_element = [i for i in lst if i]
    len_lst = len(lst)
    total_zero = len_lst - len(non_zero_element)
    # for i in range(total_zero):
    #     non_zero_element.append(0)
    lst = non_zero_element +[0] * total_zero
    return lst
lst = [1,2,3,0,0,7,9,0,3,4,0]
print (lst), "\n",move_zero_to_end(lst)

def move_zero_to_end_2(lst):
    i = len(lst) - 1
    j = i
    for j in range(i , -1, -1):
        if lst[j] !=0:
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp
            i -=1
    return lst
lst = [1,2,3,0,0,7,9,0,3,4,0]
print (lst), "\n",move_zero_to_end_2(lst)


# solution 2
def move_zero_to_begin(lst):
    i = 0
    j = i   
    n = len(lst)-1
    for j in range(i , n):
        if lst[j] !=0:
            # import pdb;pdb.set_trace()
            tmp = lst[j]
            lst[i] = lst[j]
            lst[j] = tmp
            i +=1
    return lst
lst = [1,2,3,0,0,7,9,0,3,4,0]
print (lst), "\n",move_zero_to_begin(lst)








