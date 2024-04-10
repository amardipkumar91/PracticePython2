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
    dp = [float('inf')]* (amount+1)
    dp[0] = 0
    for i in range(1, amount +1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i-coin] +1)
    if dp[amount] == 'inf':
        return -1
    else:
        return dp[amount]
coins = [1, 2, 5]
amount = 14
result = minCoins(coins, amount)
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
print (combination_sum(nums, target))


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
        import pdb;pdb.set_trace()
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