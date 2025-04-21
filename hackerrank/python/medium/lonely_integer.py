#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.

def lonelyinteger(a):
    # O(1) space XOR solution — still O(n) time:
    result = 0
    for num in a:
        result ^= num
    return result

    # O(n) time and space, readable solution with collections.Counter
    # c = Counter(a)
    # for key, val in c.items():
    #     if val == 1:
    #         return key
    # return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
