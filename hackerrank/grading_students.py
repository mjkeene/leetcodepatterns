#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.

def gradingStudents(grades):
    res = []
    for grade in grades:
        next_multiple_of_five = ((grade // 5) + 1) * 5
        if grade < 38:
            res.append(grade)
        elif next_multiple_of_five - grade < 3:
            res.append(next_multiple_of_five)
        else:
            res.append(grade)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
