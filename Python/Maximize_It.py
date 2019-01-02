# https://www.hackerrank.com/challenges/maximize-it/problem

import itertools

def compute_result(inputs, M):
    total = 0
    for i in inputs:
        total += i ** 2
    return total % M


if __name__ == "__main__":
    N, M = input().split()
    lis = []
    for i in range(int(N)):
        temp = list(map(int, input().split(" ")))
        lis.append(temp[1:])

    result, max_result = 0, 0
    for i in list(set(list(itertools.product(*lis)))):
        result = compute_result(i, int(M))
        if result > max_result:
            max_result = result

    print(max_result)
