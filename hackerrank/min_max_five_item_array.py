#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.

def miniMaxSum(arr):
    arr_sum = sum(arr)
    min_sum = arr_sum - max(arr)
    max_sum = arr_sum - min(arr)

    print(min_sum, max_sum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
