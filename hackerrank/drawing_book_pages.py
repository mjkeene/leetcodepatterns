#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p

def pageCount(n, p):
    # from front
    front = p // 2

    # from back
    back = (n // 2) - (p // 2)
    # Note: (n - p) // 2 fails when n is odd and p is one page from last, incorrectly giving 0

    return min(front, back)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
