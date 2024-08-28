def maximum_jump(number):
    max_jump = 0
    for i, jump in enumerate(number):
        if i > max_jump:
            return False
        max_jump = max(max_jump, i + jump)
        # import pdb;pdb.set_trace()
        if max_jump >= len(number) - 1:
            return True
number = [3,2,1,0,4]
print (maximum_jump(number))



data = 'aaa'

def longest_palindrome(data):
    n = len(data)
    result = []
    for i in range(n , 0 , -1):
        status = False
        for j in range(n-i+1):
            tmp = data[j : j +i]

            if tmp == tmp[::-1]:
                result.append(tmp)
                status = True
        if status:
            break
    return result
        
print (longest_palindrome(data))



def count_palindromes(s):
    n = len(s)
    count = 0
    
    # Create a table to store whether substrings are palindromes
    dp = [[False] * n for _ in range(n)]
    
    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True
        count += 1
    
    # Check substrings of length 2
    for i in range(n - 1):
        
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            count += 1
    
    # Check substrings of length greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                count += 1
    
    return count

# Example usage:
test_string = "aaa"
print(count_palindromes(test_string))  # Output: 5 (palindromic substrings: "a", "b", "c", "b", "a")




from collections import Counter

def top_k_frequent(nums, k):
    frequency_map = Counter(nums)
    sorted_elements = sorted(frequency_map, key=lambda x: frequency_map[x], reverse = True)

    
    return sorted_elements[:k]
nums = [1,1,1,2,2,3]
k = 2
print(top_k_frequent(nums, k))  # Output: [4, 1] or [4, 3]
