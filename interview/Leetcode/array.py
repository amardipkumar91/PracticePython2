'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.'''

def two_sum(nums, target):
    no_to_index = {}
    for index, i in enumerate(nums):
        x = target - i
        if x in no_to_index:
            return [no_to_index[x], index]
        no_to_index[i] = index

nums = [3,2,4]
target = 6
print (two_sum(nums, target))

'''Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

'''
def max_profit(prices):
    min_price = float('inf')
    max_profit =  0
    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
    return max_profit
prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))

'''Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/
'''

def product_except_self(nums):
    n = len(nums)
    output = [1] * n
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n-1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]
    return output
nums = [3,2,3]
print (product_except_self(nums))

def product_except_self_nxt(nums):
    from functools import reduce
    nums = [-1,1,0,-3,3]
    tp = reduce(lambda x, y : x*y, nums)
    return [tp//num for num in nums]



#extra candies

def get_candies(candies, extraCandies):
    max_candies = max(candies)
    return [(candy + extraCandies) >= max_candies for candy in candies]

candies = [2,3,5,1,3]
extraCandies = 3
print (get_candies(candies, extraCandies))



