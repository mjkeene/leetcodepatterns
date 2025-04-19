#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

def timeConversion(s):
    # AM stays same, unless 12 AM, then it becomes 00
    # PM add 12 to first digit, unless 12PM, leave it
    # Remove the AM/PM at the end of string after converting
    am_or_pm = s[-2:]
    hour = s[:2]
    if am_or_pm == 'AM' and hour == '12':
        return '00' + s[2:-2]
    elif am_or_pm == 'PM' and hour != '12':
        return str(int(hour) + 12) + s[2:-2]

    # Unchanged if numbers already in military time, remove AM/PM at end of str
    return s[:-2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
