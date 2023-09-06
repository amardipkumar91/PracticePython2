# Find the pairs in a list that sum is given number.
def findPair(lst, total_sum):
    res = []
    while lst:
        num = lst.pop()
        diff = total_sum - num
        if diff in lst:
            res.append((num, diff))
    return res

lst = [1,2,3,4,5,6]
total_sum = 7
print (findPair(lst, total_sum))

