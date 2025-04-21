#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.

def diagonalDifference(arr):
    # coordinates left_to_right -> (0,0), (1,1), (2,2,)...
    # increment both by 1 each time
    # coordinates right_to_left -> (0,2), (1,1), (0,2)
    # increment row coord, decrement column coord
    n = len(arr)
    left_to_right = 0
    right_to_left = 0

    for idx in range(n):
        left_to_right += arr[idx][idx]
        right_to_left += arr[idx][n - idx - 1]

    return abs(left_to_right - right_to_left)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
