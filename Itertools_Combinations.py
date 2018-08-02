# https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations

if __name__ == "__main__":
    strin, n  = input().split(" ")
    for i in range(1, int(n)+1):
        for i in combinations(sorted(strin),i):
            print("".join(i))
