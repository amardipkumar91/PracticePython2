# Find contiguous subarray within it which has the largest sum
#-------------------------------
# def sub_array_largest_sum(A):
#     maxSoFar = 0
#     maxEndingHere = 0
#     for i in A:
#         maxEndingHere = maxEndingHere + i
#         maxEndingHere = max(maxEndingHere, 0)
#         maxSoFar = max(maxSoFar, maxEndingHere)
#     return maxSoFar

# if __name__ == '__main__':
#     A = [-2, -3, 4, -1, -2, 1, 5, -3]
#     print ("The sum of contiguous sublist with the largest sum is",sub_array_largest_sum(A))

# Maximum Prime Factor
#-------------------------------
# import math
# def maxPrimeFactor(n):
#     max_prime = -1
#     while n % 2 == 0:
#         max_prime = 2
#         n >>= 1    
#     for i in range(3, int(math.sqrt(n)) +1, 2 ):
#         while n %i ==0:
#             max_prime = i
#             n = n / i
#     if n > 2:
#         max_prime = n
#     return int(max_prime)

# if __name__ == "__main__":
#     n = 50
#     print(maxPrimeFactor(n))

#-------------------------------
# Length of the largest subarray with contiguous elements

# def get_min(x, y):
#     return x if (x < y) else y

# def get_max(x, y):
#     return x if (x > y) else y

# def findMaxLength(arr, n):
#     max_len = 1
#     for i in range(n-1):
#         mn = arr[i]
#         mx = arr[i]
#         for j in range(i+1, n):
#             mn = get_min(mn, arr[j])
#             mx = get_max(mx, arr[j])
#             if (mx - mn) == (j - i):
#                 max_len = max(max_len, mx - mn + 1)
#     return max_len
# arr = [10,12,12]
# n = len(arr)
# print (findMaxLength(arr, n))

#-----------------------------
#Find the length of largest subarray with 0 sum

def maxLen(arr):
    max_len = 0
    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i , len(arr)):
            curr_sum += arr[j]
            if curr_sum == 0:
                max_len = max(max_len, j - i + 1)
    return max_len
                
arr = [15, -2, 2, -8, 1, 7, 10, 13] 
print (maxLen(arr))