#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k

def superDigit(n, k):
    if len(n) == 1:
        return int(n * k)

    digits = list(n)
    # digit can be huge, so sum digits and then multiply by k rather
    # than building out the digit k times and then summing
    digit_sum = sum([int(n) for n in digits]) * k

    return superDigit(str(digit_sum), 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
