# Longest substring in python


def longest_sub_string(input_str):
    len_str = len(input_str)
    index = 0
    lon_sub_str = ""
    output_length = 0
    while len_str != 0:
        l_str = ""
        for i in range(index, len_str):
            if input_str[i] not in l_str:
                l_str += input_str[i]
            else:
                break
        if len(l_str) > output_length:
            output_length = len(l_str)
            lon_sub_str = l_str
        index = index +1
        len_str = len_str- 1
    return output_length, lon_sub_str


if __name__ == '__main__':
    data = input("enter the string :   ")
    print (longest_sub_string(data))
