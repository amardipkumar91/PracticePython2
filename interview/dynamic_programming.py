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
    print(f"Minimum number of coins required to make {amount} is {result}")
else:
    print(f"It's not possible to make {amount} with the given coin denominations.")


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

    