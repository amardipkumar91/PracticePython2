lst = [1,2,3,4,5,6,9]

def insertStack(lst, value):
    if not lst:
        lst.append(value)
    else:
        popped_element = lst.pop()
        insertStack(lst, value)
        lst.append(popped_element)

def reverse_lst(lst):
    if not lst:
        return
    element = lst.pop()
    reverse_lst(lst)
    insertStack(lst,element)
reverse_lst(lst)
print (lst)

# -------- Bubble Sort-----
