#Max Consecutive Ones III
import math
def max_consecutive_one_3(nums, k): 
    left = 0
    ans = 0
    window = 0
    n = len(nums)
    for right in range(n):
        window = window + nums[right]
        while (window + k) < (right -left +1):
            window = window - nums[left]
            left +=1
        ans = max(ans, right - left +1)
    return ans

nums = [0,1,1,0,0,1]
k = 2
print (max_consecutive_one_3(nums, k))


def max_consecutive_one_3_2nd_sol(nums, k):
    start = 0
    zero_count = 0
    max_ones = 0
    for end in range(len(nums)):
        if nums[end] ==0:
            zero_count += 1
        while zero_count>k:
            if nums[start] ==0:
                zero_count -=1
            start +=1
        max_ones = max(max_ones, end-start+1)
    return max_ones
nums = [0,1,1,0,0,1]
k = 2
print (max_consecutive_one_3_2nd_sol(nums, k))



def max_consecutive_one_1(nums):
    left = 0
    ans = -1
    window = 0

    for right in range(len(nums)):
        window += nums[right]
        while right - left + 1 != window:
            window -= nums[left]
            left +=1
        ans = max(ans, right- left +1)
    return ans
nums = [1,1,0,1,1,1]
print (max_consecutive_one_1(nums))

# Maximum Number of Vowels in a Substring of Given Length  

def max_no_of_vowels(strn, k):
    cur_count = 0
    max_count = 0
    vowels = ('a', 'i', 'o', 'u', 'e')
    for i in range(k):
        if strn[i] in vowels:
            cur_count +=1
    max_count = cur_count

    for i in range(k, len(strn)):
        if strn[i -k ] in vowels:
            cur_count -=1
        if strn[i] in vowels:
            cur_count +=1
        max_count = max(max_count, cur_count)
    return max_count

strn = 'abciiidef'
k = 3
print (max_no_of_vowels(strn, k))

# Longest Subarray of 1's After Deleting One Element


def longest_sub_ar_del_one(nums):
    cur = 0
    prev = 0
    ans = 0
    for i in range(len(nums)):
        if nums[i] ==1:
            cur +=1
        else:
            ans = max(ans, cur + prev)
            prev = cur
            cur = 0
    return max(ans, cur + prev)

nums = [1,1,0,1]
print (longest_sub_ar_del_one(nums))


def longest_sub_ar_del_one_sliding_window(nums):
    left = 0
    zero_count = 0
    max_length = 0

    for right in range(len(nums)):
        # Count zeros in the current window
        if nums[right] == 0:
            zero_count += 1

        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
            print ("--",left)

        max_length = max(max_length, right - left)
    return max_length
nums = [0,1,1,0,0,1]
print (longest_sub_ar_del_one_sliding_window(nums))