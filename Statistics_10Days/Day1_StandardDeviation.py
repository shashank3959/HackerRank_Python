# 10 Days of Statistics: Day 1: Standard Deviation
from math import sqrt


def calc_mean(inputs):
    return sum(inputs)/len(inputs)


if __name__ == "__main__":
    n = int(input())
    inputs = list(map(int, input().split()))

    # Doing from scratch
    mean = calc_mean(inputs)

    sq = []
    for i in inputs:
        sq.append((i-mean)**2)
    sq_sum_mean = sum(sq)/len(inputs)
    std_dev = sqrt(sq_sum_mean)
    print(std_dev)