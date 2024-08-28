#Find a pair with the given sum in an array
def findPair(nums, target):
    for i in nums:
        remain = target - i
        if remain in nums:
            pair = (i, remain)
    if pair:
        return pair
    else:
        return "No available"
nums = [8, 7, 2, 5, 3, 1]
target = 10
print ("------------findPair------------------")
print (findPair(nums, target))

#Check if a subarray with 0 sum exists or not

def hasZeroSumSublist(nums):
    s = set()
    total = 0
    for i in nums:
        total += i
        if total in s:
            return True
        s.add(total)
nums = [4, -6, 3, -1, 4, 2, 7]
print ("------------hasZeroSumSublist------------------")
print (hasZeroSumSublist(nums))

#Print all subarrays with 0 sum

def allSubList(nums):
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            if total ==0:
                print ('sublist', nums[i:j+1])

nums = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
print ("------------allSubList------------------")
allSubList(nums)

#Sort binary array in linear time

def sortBinaryArray(ba):
    k = 0
    for i in range(len(ba)):
        if ba[i] ==0:
            ba[k] =0
            k = k+1
    for i in range(k,len(ba)):
        ba[k] = 1
        k = k+1
    return ba
ba = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
print ("------------sortBinaryArray------------------")
print (sortBinaryArray(ba))


#Find the largest subarray having an equal number of 0’s and 1’s
def findLargestSublist(nums):
    d = {}
    d[0] = -1
    length = 0
    ending_index = -1
    total = 0
    for i in range(len(nums)):
        total += -1 if (nums[i] == 0) else 1
        if total in d:    
            if length < i-d.get(total):
                length = i - d.get(total)
                ending_index = i
        else:
            d[total] = 1
        
    if ending_index != -1:
        print((ending_index - length + 1, ending_index))
    else:
        print('No sublist exists')
nums = [0, 0, 1, 0, 1, 0, 0]
findLargestSublist(nums)

#Find maximum length subarray having a given sum

def find_subarray_with_sum(nums, target):
    start = 0
    current_sum = 0
    for end in range(len(nums)):
        current_sum += nums[end]
        while current_sum > target and start < end:
            current_sum -= nums[start]
            start += 1
            
        if current_sum == target:
            return nums[start, end]




nums = [1, 4, 20, 3, 10, 5]
target = 33
result = find_subarray_with_sum(nums, target)
print("Indices of contiguous subarray with target sum:", result) 



