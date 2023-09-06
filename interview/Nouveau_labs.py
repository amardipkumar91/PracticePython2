# a = [10,11,12,13,14,15]
# a[0],a[-1] = a[-1], a[0]
# print (a)


def prettyPrint(A):
    s = 2 * A -1
    result = []
    for i in range(0, int(s/2) + 1):
        l_r = []
        m = A
        for j in range(0, i):
            l_r.append(m)
            m -= 1
        for k in range(0, s-2*i):
            l_r.append(A -i)
        
        m = A -i +1
        for i in range(0, i):
            l_r.append(m)
            m += 1
        result.append(l_r)
    
    for i in range(int(s/2), -1, -1):
        m = A
        l_r = []
        for j in range(0, i):
            l_r.append(m)
            m -= 1
        for k in range(0, s-2*i):
            l_r.append(A -i)
        
        m = A -i +1
        for i in range(0, i):
            l_r.append(m)
            m += 1
        result.append(l_r)
        
        
    final_result = []
    previous_elem = None
    for elem in result:
        if elem != previous_elem:
            final_result.append(elem)
            previous_elem = elem
    return final_result

print (prettyPrint(3))


# class Solution:
#     # @param A : list of integers
#     # @return a list of integers
#     def solve(self, A):
#         result = []
#         zero_count = 0
#         for i in A:
           
#             if i != 0:
#                 result.append(str(i))
#             else:
#                 zero_count = zero_count + 1
        
#         for i in range(zero_count):
#             result.append(str(0))
        
#         return " ".join(result)+" "

# s = Solution()
# r = s.solve([5,17,0,11])
# print (r)

# def solve(A):
#     size = len(A)
#     result = []
#     for i in range(0, size):
#         for j in range(i + 1, size):
#             if A[i] <= A[j]:
#                 break
#         if j == size -1:
#             result.append(A[i])
#     return result
# ll = [ 4, 8, 45, 46, 18, 17, 78, 40, 27, 34, 74, 52, 31, 35, 19, 42, 47, 73, 67, 5, 25, 13, 62, 26, 22, 69, 43, 65, 79, 57, 80, 71, 54, 10, 29, 64, 1, 56, 41, 6, 9, 38, 77, 39, 48, 12, 33, 24, 75, 63, 21, 20, 72, 32, 68, 7, 28, 16, 14, 60, 2, 3, 59, 49, 37, 70, 50, 51, 44, 30, 55, 53, 11, 66, 58, 15, 36, 76, 23, 61 ]
# print(solve(ll))


#  Find Maximum possible even sum in list 

def maxPossibleEvenSum(A):
        size = len(A)
        pos_sum = sum(A)
        if (pos_sum %2 ==0):
            return pos_sum
        ans = 0
        for i in range(size):
            if (A[i] % 2 != 0):
                if A[i] > 0:
                    ans = max(ans, pos_sum - A[i])
                else:
                    ans = max(ans, pos_sum+ A[i])
        return ans

arr =  [3,4,8,1,5,2,6]
print (maxPossibleEvenSum(arr)) 


