#!/bin/python3

import math
import os
import random
import re
import sys


def aVeryBigSum(ar):
    a = 0
    for i in range(ar_count):
        a += ar[i]
    return a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
