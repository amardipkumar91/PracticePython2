#find nth smallest number from a list in python using binary search


def count_less_or_equal(arr, n):
    count = 0
    for i in arr:
        if i<=n:
            count += 1
    return count

def nth_smallest(arr, n):
    low = min(arr)
    high = max(arr)
    while low < high:
        mid = low + (high - low) //2
        count = count_less_or_equal(arr, mid)
        if count < n :
            low = mid +1
        else:
            high = mid
    return low

arr = [7, 10, 4, 3, 20, 15]
n = 3
print (nth_smallest(arr, n))

#find nth Larget number from a list in python using binary search

def count_greater_or_equal(arr, n):
    count = 0 
    for i in arr:
        if i >=n:
            count = count +1
    return count

def nth_largest(arr,n):
    low = min(arr)
    high = max(arr)
    while low < high:
        mid = low + (high - low) //2
        count = count_greater_or_equal(arr, mid)
        if count < n :
            high = mid
        else:
            low = mid + 1
    return low - 1

arr = [7, 10, 4, 3, 20, 15]
n = 3
print (nth_largest(arr, n))



# Maximum Sum Circular Subarray
'''
Input:  {2, 1, -5, 4, -3, 1, -3, 4, -1} Output: Subarray with the largest sum is 
{4, -1, 2, 1} with sum 6.  Input:  {-3, 1, -3, 4, -1, 2, 1, -5, 4}
 Output: Subarray with the largest sum is {4, -1, 2, 1} with sum 6.
'''

#Example 1
def kadane_algo_with_list(A):
    max_so_far = max_ending_here = A[0]
    start = end = temp_start = 0
    for i in range(1, len(A)):
        if A[i] > max_ending_here + A[i]:
            
            max_ending_here = A[i]
            temp_start = i
        else:
            max_ending_here += A[i]
        
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = temp_start
            end = i
    return max_so_far , arr[start:end + 1]
A = [2, 1, -5, 4, -3, 1, -3, 4, -1]
print (kadane_algo_with_list(A))

# Now start

def kadane_algo(A):
    max_so_far = 0
    max_ending_here = 0
    for i in range(len(A)):
        max_ending_here = max_ending_here + A[i]
        max_ending_here = max(max_ending_here, 0)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def runCircularKadane(A):
    
    ''' return the maximum of the following:
        1. Sum returned by Kadanes algorithm on the original list.
        2. Sum returned by Kadanes algorithm on modified list +
           the sum of all elements in the list.
    '''
        
    if len(A) ==0:
        return 0
    
    maximum = max(A)
    if maximum < 0:
        return maximum
    
    for i in range(len(A)):
        A[i] = -A[i]
    
    neg_max_sum = kadane_algo(A)

    for i in range(len(A)):
        A[i] = -A[i]

    return max(kadane_algo(A), sum(A) + neg_max_sum)



if __name__ == '__main__':
 
    A = [2, 1, -5, 4, -3, 1, -3, 4, -1]
 
    print("The sum of the sublist with the largest sum is", runCircularKadane(A))


# Three Sum proble

def threeSum(nums):

    nums.sort()
    res = []
    for i, a in enumerate(nums):
        if i >0 and a == nums[i-1]:
            continue
        l = i +1
        r = len(nums) -1
        while l < r:
            total = a + nums[l] + nums[r]
            if total > 0:
                r -= 1
            elif total <0:
                l += 1
            else:
                res.append([a,nums[l], nums[r]])
                l +=1
                while nums[l] == nums[l-1] and l < r:
                    l +=1
    return res



nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))  



nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))  