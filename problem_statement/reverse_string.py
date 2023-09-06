# Reverse a string without affecting the number.
# input : abc123def
# output : fed123cba

def reverse_string_without_affecting_number(text):
    temp = []
    text = list(text)
    for i in text:
        if not i.isnumeric():
            temp.append(i)
    reverse_temp =  temp [::-1]
    count = 0
    for i in range(0,len(text)):  
        if not text[i].isnumeric():
            text[i] = reverse_temp[count]
            count +=1  
        else:
            continue
    return "".join(text)

print (reverse_string_without_affecting_number('abc1235de9f15ui'))