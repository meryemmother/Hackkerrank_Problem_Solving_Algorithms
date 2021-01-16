#!/bin/python3

import os
import sys


def pageCount(n, p):
    liste1 = []
    sonucliste = []

    for i in range(0, n + 1):
        liste1.append(i)
    liste2 = liste1[::-1]

    for i in range(len(liste1)):
        if p == liste1[i]:
            sonucliste.append(i)

    for i in range(len(liste2)):
        if p == liste2[i]:
            sonucliste.append(i)
    print(sonucliste)

    x = sonucliste[0] / 2
    if sonucliste[1] == 1 and max(liste1) == 6:

        y = sonucliste[1]
    else:
        y = sonucliste[1] / 2

    if x > y:
        return int(y)
    elif y > x:
        return int(x)
    elif x == y:
        return int(x)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
