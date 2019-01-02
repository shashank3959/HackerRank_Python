# https://www.hackerrank.com/challenges/itertools-permutations/problem


import itertools

A, n = input().split(" ")
n = int(n)
lis = list(itertools.permutations(sorted(A),n))

for i in lis:
    print("".join(i))