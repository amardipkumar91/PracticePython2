import os
import re
import sys

# Complete the hourglassSum function below.
arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

def calculatesum(i, j):
    # import pdb;pdb.set_trace()
    return(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])


def hourglassSum(arr):
    sumslist = []
    for i in range(0, 4):
        for x in range(0, 4):
            sum = calculatesum(i,x)    
            sumslist.append(sum)
    return sumslist

if __name__ == '__main__':
    result = hourglassSum(arr)
    print max(result)
