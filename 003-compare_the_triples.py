import math
import os
import random
import re
import sys


def compareTriplets(a, b):
    BOB = 0
    ALİCE = 0
    for i in range(len(a)):
        if a[i] < b[i]:
            BOB += 1
        elif a[i] > b[i]:
            ALİCE += 1
        else:
            pass
    return ALİCE, BOB


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
