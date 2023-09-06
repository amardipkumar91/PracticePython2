#question 1
'''Given a string of integers, find out the number of even integers at each index i . 
Assume string starts at index 1.  You have to print the count for each index in space separated format.
Sample Input:

First line contains a string S.

574674546476

Sample Output:
Print  space-separated integers,the result of every index.

7 7 7 6 5 5 4 4 3 2 1 1

'''
sample_string = '574674546476'
result = []
len_str = len(sample_string)
outer_count = 0
for i in sample_string:
    count = 0
    for j in range(outer_count, len_str):
        if int(sample_string[j]) % 2 == 0:
            count = count + 1
        else:
            continue
    result.append(str(count))
    outer_count = outer_count + 1
print (" ".join(result))

#---------------------------

#question 2
'''Given a string s, return the longest palindromic substring in s.
'''

sample_input = 'ac'
result = 0
final_substring = ''
count = 0

for i in range(0, len(sample_input)):
    sub_str = sample_input[i]
    for j in range(i+1, len(sample_input)):
        sub_str = sub_str +  sample_input[j]
        count = count +1
        print (sub_str)
        if sub_str == sub_str[::-1]:
            if len(sub_str) > result:
                result = len(sub_str)
                final_substring = sub_str
print (result, final_substring)




