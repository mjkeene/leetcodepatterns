#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    curr_min, curr_max = scores[0], scores[0]
    min_changes, max_changes = 0, 0

    for idx in range(1, len(scores)):
        curr_score = scores[idx]
        if curr_min > curr_score:
            curr_min = curr_score
            min_changes += 1
        if curr_max < curr_score:
            curr_max = curr_score
            max_changes += 1

    return max_changes, min_changes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
