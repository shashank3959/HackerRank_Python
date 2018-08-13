# https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque

if __name__ == "__main__":
    d = deque()
    n = int(input())
    for i in range(n):
        inp = input().split()
        exec("d.{0}({1})".format(*inp, ""))

    print(*d)

