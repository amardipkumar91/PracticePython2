# Longest substring in python


def longest_substring(s):
    if not s:
        return 0, ""

    # Initialize variables
    max_length = 0
    max_substring = ""
    start = 0
    seen = set()

    # Iterate through the string using two pointers
    for end in range(len(s)):
        # If the character at 'end' is already in the 'seen' set
        # Move the 'start' pointer to the right until the duplicate character is no longer in the 'seen' set
        while s[end] in seen:
            
            seen.remove(s[start])
            start += 1
        
        # Add the character at 'end' to the 'seen' set
        seen.add(s[end])
        # Update max_length and max_substring if necessary
        if end - start + 1 > max_length:
            max_length = end - start + 1
            max_substring = s[start:end+1]

    return max_length, max_substring
if __name__ == '__main__':
    # data = input("enter the string :   ")
    data = "amardip"
    print (longest_substring(data))



# Longest Repeating Character Replacement
def characterReplacement(s, k):
    max_len = 0
    max_count = 0
    count = {}
    left = 0
    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) +1
        max_count = max(max_count, count[s[right]])
        if (right - left +1) - max_count > k:
            count[s[left]] -= 1
            left += 1
        max_len = max(max_len, right - left +1)
    return max_len
s = "AABABBA"
k = 1
print(characterReplacement(s, k))

# Minimum Window Substring
from collections import Counter
def min_window_substr(ss, t):
    if not t:
        return ""

    countT = Counter(t)
    window = {}
    have = 0
    need  = len(countT)
    res = [-1,-1]
    res_len = float("inf")

    left = 0
    for right in range(len(ss)):
        cc = ss[right]
        window[cc] = window.get(cc, 0) +1
        if cc in countT and window[cc] == countT[cc]:
            have += 1
        
        while have == need:
            if (right -left +1) < res_len:
                res = [left, right]
                res_len = right -left +1
            window[ss[left]] -= 1
            if ss[left] in countT and window[ss[left]] < countT[ss[left]]:
                have -=1
            left +=1
    left, right = res
    return s[left: right+1]  

s = "ADOBECODEBANC"
t = "ABC"
print (min_window_substr(s, t))


# Group Anagrams
def group_anagram(strs):
    from collections import defaultdict
    anagram = defaultdict(list)
    for i in strs:
        key = "".join(sorted(i))
        anagram[key].append(i)
    return list(anagram.values())
strs = ["eat","tea","tan","ate","nat","bat"]
print (group_anagram(strs))


#Valid Prantheses

def is_valid_paranth(s):
    closeToOpen = {'}': '{', ')': '(', ']': '['}
    stack = []
    for i in s:
        if i in closeToOpen:
            if stack and stack[-1] == closeToOpen[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    return True if not stack else False
s = "()[]{}"
print (is_valid_paranth(s))


#Merge Strings Alternately

def merge_string(str1,str2):
    len1 = len(str1)
    len2= len(str2)
    min_len = min(len1, len2)
    result = ""
    for i in range(0, min_len):
        result = result + str1[i] + str2[i]
    if len1 > len2:
        result = result + str1[min_len:]
    if len2 > len1:
        result = result + str2[min_len:]
    return result
str1 = "abcd"
str2 = "xyzqui"
print (merge_string(str1,str2))

#Greatest Common Divisor of Strings


def gcd(x,y):
    while y:
        x,y = y , x%y
    return x

def get_string_gcd(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    if str1 + str2 != str2+ str1:
        return None
    gc = gcd(len1, len2)
    return str1[:gc]

str1 = 'ABCABC'
str2= 'ABC'
print (get_string_gcd(str1, str2))


#Reverse Vowels of a String

def get_reverse_vowels(strr):
    volwes = ['a', 'i', 'o', 'u', 'e']
    all_vowels = [i for i in strr if i in volwes]
    reverse_vowels = all_vowels[::-1]
    result = []
    n = len(strr)
    index = 0
    for i in range(n):
        if strr[i] in reverse_vowels:
            result.append(reverse_vowels[index])
            index += 1
        else:
            result.append(strr[i])
    return "".join(result)


strr = "leetcode"
print (get_reverse_vowels(strr))


strr = "leetcode"
print (get_reverse_vowels(strr))


#Increasing Triplet Subsequence
def increasingTriplet(nums):
    first = second = float('inf')
    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
            
    return False
nums = [1,2,3,4,5]
print (increasingTriplet(nums))


class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    

    def __add__(self, other):
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        return ComplexNumber(new_real, new_imag)
    
    def __str__(self):
        sign = "+" if self.imag >= 0 else "-"
        return f"{self.real} {sign} {abs(self.imag)}i"
    
a = ComplexNumber(real = 3, imag=7)
b = ComplexNumber(real=4, imag= 8)
print (a+b)


#Can Place Flowers

def can_place_flowers(flowerbed, n):
    length = len(flowerbed)
    count = 0  # Counter for how many flowers we can plant

    for i in range(length):
        # Check if the current plot is empty and the adjacent plots are either empty or out of bounds
        if flowerbed[i] == 0:
            empty_left = (i == 0 or flowerbed[i - 1] == 0)
            empty_right = (i == length - 1 or flowerbed[i + 1] == 0)
            if empty_left and empty_right:
                # Plant a flower here
                flowerbed[i] = 1
                count += 1
                
                if count >= n:
                    return True
    
    return count >= n

flowerbed = [1, 0, 0, 0, 1]
n = 2
print(can_place_flowers(flowerbed, n))
