# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

X = int(input())
shoe_sizes = Counter(map(int, input().split(" ")))
total = 0

for _ in range(int(input())):
    size, sp = map(int, input().split())
    if shoe_sizes[size] != 0:
        total += sp
        shoe_sizes[size] -= 1

print(total)
