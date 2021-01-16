import math
import os
import random
import re
import sys


def plusMinus(arr):
    pozitif = []
    negatif = []
    sıfır = []
    for i in (arr):
        if i > 0:
            pozitif.append(i)
        elif i < 0:
            negatif.append(i)
        elif i == 0:
            sıfır.append(i)

    print("""{}
{}
{}""".format(len(pozitif) / n, len(negatif) / n, len(sıfır) / n))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
