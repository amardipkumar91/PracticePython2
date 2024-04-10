
# Find Longest Substring in the string without repeating characters.
def find_non_repeating_substring(input_str):
    output_length = 0
    longest_sub_str = ''
    len_str = len(input_str)
    index = 0
   
    while len_str != 1:
        l_str = ''
        for i in range(index, len(input_str)):
            if input_str[i] not in l_str:
                l_str = l_str + input_str[i]
            else:
                break
        sub_str_length = len(l_str)
        if sub_str_length >  output_length:
            output_length = sub_str_length
            longest_sub_str = l_str
        len_str = len_str -1
        index = index + 1
    return output_length,longest_sub_str
if __name__ == '__main__':
    input_str = "abcabcde"
    sub_str_length, sub_str = find_non_repeating_substring(input_str)
    print ('    sting lenght is "{0}" and the sub string is "{1}"'.format(sub_str_length, sub_str))


def solution(N):
    num = str(N)
    leng = len(str(num))
    num_list = []
    for i in range(0, leng):
        aa = list(str(num))
        aa.insert(i, str(5))
        num_list.append("".join(aa))
    
    print (max(num_list))
    print (num_list)
solution(268)

