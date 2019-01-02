# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict

if __name__ == "__main__":
    n = int(input())
    d = OrderedDict()
    for i in range(n):
        f = input().split(" ")
        p = int(f[-1])
        name = " ".join(f[:len(f) - 1])
        if name in d:
            d[name] += p
        else:
            d[name] = p

    for i in d:
        print(i, d[i])
