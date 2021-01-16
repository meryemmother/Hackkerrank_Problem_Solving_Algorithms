#!/bin/python3

import math
import os
import random
import re
import sys


def gradingStudents(grades):
    sonuc = []
    for i in grades:
        if i < 38 or i % 5 == 0:
            sonuc.append(i)
        else:
            k = i % 5
            k = 5 - k
            if k >= 3:
                sonuc.append(i)
            else:
                t = i + k
                sonuc.append(t)

    return sonuc


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
