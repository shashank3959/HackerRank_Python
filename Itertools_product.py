# https://www.hackerrank.com/challenges/itertools-product/problem


import itertools
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))

list = itertools.product(A,B)
for i in list:
    print(i, end=' ')
