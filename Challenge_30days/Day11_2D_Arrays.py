# https://www.hackerrank.com/challenges/30-2d-arrays/problem

# !/bin/python3

import math
import os
import random
import re
import sys

# !/bin/python3

import math
import os
import random
import re
import sys


def givesum(arr, i, j):
    return (arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] +
            arr[i + 2][j + 2])


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    hourglass_sum = 0
    max_hourglass_sum = givesum(arr, 0, 0)

    for i in range(4):
        for j in range(4):
            hourglass_sum = givesum(arr, i, j)
            if hourglass_sum > max_hourglass_sum:
                max_hourglass_sum = hourglass_sum

    print(max_hourglass_sum)
