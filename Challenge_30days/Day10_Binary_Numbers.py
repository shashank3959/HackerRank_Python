# https://www.hackerrank.com/challenges/30-binary-numbers/problem


# !/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n_bin = str(bin(int(input())))[2:]

    max_consec_1, consec_1= 0,0
    for i in range(len(n_bin)):
        if n_bin[i] == "1":
            consec_1 = 1
            for j in range(i + 1, len(n_bin)):
                if n_bin[j] == "1":
                    consec_1 += 1
                else:
                    break
        if consec_1 > max_consec_1:
            max_consec_1 = consec_1

    print(max_consec_1)