#!/bin/python3

import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    ilktoplam = 0
    ikincitoplam = 0
    ilkliste = []
    ikinci = []
    for i in range(n):
        ilkliste.append(arr[i][i])
    for m in range(n):
        ikinci.append(arr[-m - 1][m])

    cevap = abs(sum(ilkliste) - sum(ikinci))

    return cevap


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
