#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar

def sockMerchant(n, ar):
    # Frequency mapping, floor division
    c = Counter(ar)

    return sum(val // 2 for _, val in c.items())

    # # Naive, basic solution
    # sorted_ar = sorted(ar)
    # num_pairs = 0
    # i = 1

    # while i <= len(sorted_ar) - 1:
    #     if sorted_ar[i-1] == sorted_ar[i]:
    #         num_pairs += 1
    #         i += 2
    #     else:
    #         i += 1
    # return num_pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
