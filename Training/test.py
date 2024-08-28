# def check_even_odd(number):
#     if isinstance(number, int):
#         enev = []
#         odd = []
#         for i in range(1, number):
#             if i %2 ==0:
#                 enev.append(i)
#             else:
#                 odd.append(i)
#         return enev, odd
#     else:
#         return False, False
# even, odd = check_even_odd(40)
# print (even, odd)



# def check_number(number):
#     a = [1,2,3,4]
#     while a:
#         if number %2 ==0:
#             print (number)
#             break
#         else:
#             a.pop()
#             print ("In else", a)
#     print ("Complete")
    
# check_number(11)




def reverse_string_keeping_special_chars(input_string):
    all_apha_num = [char for char in input_string if char.isalnum()]
    all_apha_num.reverse()
    result = []
    index = 0
    for i in input_string:
        if i.isalnum():
            result.append(all_apha_num[index])
            index +=1
        else:
            result.append(i)
    return "".join(result)
    
input_string = "a!b@c#d$"
output_string = reverse_string_keeping_special_chars(input_string)
print(output_string) 