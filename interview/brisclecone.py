def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def countWays(s):
    return fib(s + 1)
 
# Driver program
s = 4
print ("Number of ways = ",countWays(s))


# import unittest
# class Testing(unittest.TestCase):
#     def test_string(self):
#         s1 = (2!=2)
#         s2 = 0
#         self.assertEqual(s1, s2)
#     def test_boolean(self):
#         s1 = False
#         s2 = 'False'
#         self.assertEqual(s1, s2)

# if __name__ == '__main__':
#     unittest.main()

# def make_secure(func):
#     print ("hi")
#     def secure_function(*args):
#         print ("hh")
#         func(*args)
#         print ('hhggg')
#     print ('mmmm'   )        
#     return secure_function    

# @make_secure
# def foo():
#     print ('fun')
# foo()

#---------- merge two sorted list -------
# A = [4,5,7,9]
# B  = [3,6,7,10]
# len_A = len(A)
# len_B = len(B)
# i, j = 0,0
# result = []
# while i < len_A and j < len_B:
#     if A[i] > B[j]:
#         result.append(B[j])
#         j += 1
#     else:
#         result.append(A[i])
#         i += 1

# print (result + A[i:] + B[j:])


#---------------- Merge Sort ----

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        print ("hh")
    return arr

print (mergeSort([2,5,4,7,2,8,3,9]))



