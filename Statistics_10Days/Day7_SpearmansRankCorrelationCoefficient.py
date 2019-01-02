# 10 Days of Statistics: Day 7: Spearman's Rank Correlation Coefficient

from math import sqrt


def spearman(X, Y, n):
    disq = [(x-y)**2 for x, y in zip(X, Y)]
    r = 1 - (6 * sum(disq))/(n*(n * n - 1))
    return r


def get_rank(X, n):
    x_rank = dict((x, i+1) for i, x in enumerate(sorted(set(X))))
    return [x_rank[x] for x in X]


if __name__ == "__main__":
    n = int(input())
    X = list(map(float, input().split()))
    Y = list(map(float, input().split()))
    rankX = get_rank(X, n)
    rankY = get_rank(Y, n)
    print('%.3f' % spearman(rankX, rankY, n))
