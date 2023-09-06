import math
import os
import random
import re
import sys

def rotLeft(a, d):
    n = len(a)
    s = []
    for i in range(n):
        s.append(a[(d + i ) % n])
    return s

if __name__ == '__main__':
    nd = raw_input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = map(int, raw_input().rstrip().split())
    result = rotLeft(a, d)
    print result