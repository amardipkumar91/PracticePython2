def climbStrains(n):
    if n ==1:
        return 1
    if n ==2:
        return 2
    dp =[0] * (n+1)
    dp[1] = 1
    dp[2] =2
    for i in range(3, n +1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
n = 5
print (climbStrains(n))


# Coin Change problem 
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

def minCoins(coins, amount):
    dp = [999]* (amount+1)
    dp[0] = 0
    
    for i in range(1, amount +1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i-coin] +1)

    if dp[amount] == 999:
        return -1
    else:
        return dp[amount]

coins = [1, 2, 5]
amount = 11
result = minCoins(coins, amount)
print ("---", result)
if result != -1:
    print("Minimum number of coins required to make {amount} is {result}")
else:
    print("It's not possible to make {amount} with the given coin denominations.")


#Longest Increasing Subsequence

def find_lis(nums):
    if not nums:
        return []
    n = len(nums)
    list_length = [1]*n
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                list_length[i] = max(list_length[i], list_length[j]+1)
    return max(list_length)
nums = [0,1,0,3,2,3]
print (find_lis(nums))

def word_break_problem(wordDict,input_str):
    n = len(input_str)
    dp = [False] * (n+1)
    dp[0] = True
    
    for i in range(1, n+1):
        for j in range(i):
            if dp[j] and input_str[j:i] in wordDict:
                
                dp[i] = True
                break
    return dp[n]
          
wordDict = ["leet","code"]
input_str = "leetcode"
print (word_break_problem(wordDict,input_str))

#combination sum
def combination_sum(nums, target):
    dp = [0] * (target +1)
    dp[0] = 1
    for i in range(1, target+ 1):
        for num in nums:
            if i - num >= 0:
                dp[i] += dp[i-num]
    
    return dp[target]

nums = [1,2,3]
target = 4
print ("--?comp", combination_sum(nums, target))


def rob(nums):
    if not nums:
        return 0

    n = len(nums)
    if n == 1:
        return nums[0]
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    return dp[-1]
nums = [2, 7, 9, 3, 1]
print("Maximum amount of money robbed:", rob(nums))


#Unique Paths

def unique_paths(m, n):
    dp = [[0]*n for _  in range(m)]
    for i in range(m):
        dp[i][0] = 1
    
    for j in range(n):
        dp[0][j] = 1
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j-1]
    return dp[m-1][n-1]

m = 3
n = 7
print (unique_paths(m, n))


def can_jump(nums):
    max_reachable = 0
    n = len(nums)

    for i in range(n):
        # If the current index is beyond the maximum reachable index, return False
        if i > max_reachable:
            return False
        # Update the maximum reachable index based on the current position and jump length
        max_reachable = max(max_reachable, i + nums[i])
        # If the maximum reachable index exceeds or equals the last index, return True
        if max_reachable >= n - 1:
            return True

    return False

# Example usage:
nums = [2, 3, 1, 1, 4]
print("Can jump to the last index?", can_jump(nums))



# GET element of longest increasing subsequence

def longest_increasing_subsequence(nums):
    if not nums:
        return 0, []

    # Initialize a list to store the length of the longest increasing subsequence ending at each index
    dp = [1] * len(nums)
    # Initialize a list to store the index of the previous element contributing to the LIS ending at each index
    prev_index = [-1] * len(nums)

    # Iterate through each index in the array
    for i in range(1, len(nums)):
        # Check all previous indices for increasing subsequences
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                # Update dp[i] with the maximum length of increasing subsequence ending at index i
                dp[i] = dp[j] + 1
                # Update prev_index[i] to j to keep track of the previous element contributing to the LIS ending at index i

    # Find the index of the maximum value in dp, which represents the end index of the LIS
    end_index = dp.index(max(dp))
    # Initialize a list to store the elements of the LIS
    lis = [nums[end_index]]

    # Traverse backwards from end_index to retrieve the elements of the LIS
    while prev_index[end_index] != -1:
        end_index = prev_index[end_index]
        lis.append(nums[end_index])

    # Reverse the lis list to get the elements in increasing order
    lis.reverse()

    # Return the length of the LIS and the elements of the LIS
    return max(dp), lis

# Example usage:
nums = [10, 9, 2, 5, 3, 7, 101, 18]
length, lis_elements = longest_increasing_subsequence(nums)
print("Length of LIS:", length)
print("Elements of LIS:", lis_elements)






#rob11 problem



def rob_linear(nums):
    if not nums:
        return 0
    n = len(nums)
    if n == 1:
        return nums[0]
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    return dp[-1]

def rob(numbers):
    if not numbers:
        return 0
    if len(numbers) ==1:
        return numbers[0]
    if len(numbers) ==2:
        return max(numbers[0], numbers[1])
    max1 = rob_linear(numbers[1:])
    max2 = rob_linear(numbers[:-1])
    return max(max1, max2)
numbers = [2, 7, 9, 3, 1]
print("Maximum amount of money robbed:", rob(numbers))


def jump_game_next_solutions(nums):
    n = len(nums)
    final_position = n - 1
    for i in range(n-2, -1, -1):
        if i + nums[i] >= final_position:
            final_position = i
    return final_position ==0
nums = [3,2,1,0,4]
print("Can jump to the last index?", jump_game_next_solutions(nums))
nums = [2,3,1,1,4]
print("Can jump to the last index?", jump_game_next_solutions(nums))



