'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
https://leetcode.com/problems/3sum/description/

'''

def threeSum(nums, target):
    result = []
    nums.sort()
    for i in range(len(nums) -2):
        if i >0  and nums[i] == nums[i-1]:
            continue
        left = i + i
        right = len(nums) - 1
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            if curr_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                left +=1
                right -=1
                while left < right and nums[left] == nums[left -1]:  
                    left +=1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            
            elif curr_sum < target:
                left += 1
            else:
                right -= 1  
    return result
nums = [-1, 4, 1, 2, -1, -4]
target = 0
result = threeSum(nums, target)
print(result)  # Output: [[-1, -1, 2], [-1, 0, 1]]

#Container With Most Water
'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

https://leetcode.com/problems/container-with-most-water/

'''
def most_water(height):
    left = 0
    max_area = 0
    right = len(height) - 1
    while left < right:
        h = min(height[left], height[right])
        w = right - left
        areas = h * w
        max_area = max(max_area, areas)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area
height = [1,8,6,2,5,4,8,3,7]
print (most_water(height))



'''get next_greater_temperatures'''


def next_greater_temperatures(temperatures):
    n = len(temperatures)
    result = [-1] * n
    stack = []
    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()
            result[prev_index] = temperatures[i]

        stack.append(i)
    return result
        
temperatures = [4, 5, 6, 3, 2, 9]
print(next_greater_temperatures(temperatures))






