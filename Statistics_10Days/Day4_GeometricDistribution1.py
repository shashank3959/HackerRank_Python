# 10 Days of Statistics: Day 4: Geometric Distribution

from math import exp


# Factorial through recursion
def fact(x):
    return 1 if x == 0 else x*fact(x-1)


def poisson(k, lam):
    return ((lam ** k) * (exp(-lam))) / fact(k)


if __name__ == "__main__":
    lam = float(input())
    k = int(input())
    print(round(poisson(k, lam), 3))
