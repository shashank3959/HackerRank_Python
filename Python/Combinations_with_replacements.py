# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem


from itertools import combinations_with_replacement

string, k = input().split(" ")
for i in combinations_with_replacement(sorted(string), int(k)):
    print("".join(i))