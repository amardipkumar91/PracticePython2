# def friendGrouping(N,A):
#     result=0
#     while A:
#         chr = A[0][0]
#         count = 0
#         for i in A:
#             if chr in i:
#                 count = count + 1
#         if count > result:
#             result = count
#         A.pop(0)
 
#     return result
# N=int(input())
# A=[]
# for i in range(N):
#     A.append(input())

# print(friendGrouping(N,A))


def getJn(N, a, b):
    print (N)
    result= -404
    if N == 0 or N == 1:
        return 1
    else:
        # return a * getJn(N-1, a, b) + b * (N-2, a, b)
        return a * getJn(N-1,a,b) + b* getJn(N-2,a,b)
N = int(input())
a = int(input())
b = int(input())
print (getJn(N, a, b))