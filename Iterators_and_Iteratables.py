# https://www.hackerrank.com/challenges/iterables-and-iterators/problem

from itertools import combinations

N, letters = int(input()), input().split(" ")
list_combo = list(combinations(letters, int(input())))

num_a = 0
for i in list_combo:
    if 'a' in i:
        num_a += 1
print(num_a/len(list_combo))
