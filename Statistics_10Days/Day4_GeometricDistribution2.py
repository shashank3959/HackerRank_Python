# 10 Days of Statistics: Day 4: Geometric Distribution 2


def geometric(n, p):
    return ((1-p)**(n-1)) * p


if __name__ == "__main__":
    num, den = map(int, input().split())
    n = int(input())
    p = num/den

    total_prob = 0
    for i in [1, 2, 3, 4, 5]:
        total_prob += geometric(i, p)

    print(round(total_prob, 3))
