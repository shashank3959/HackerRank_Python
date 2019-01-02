# 10 Days of Statistics: Day 5: Poisson Distribution 2


def Poisson(n, p):
    return ((1-p)**(n-1)) * p


def second_moment(lam):
    return lam + (lam ** 2)

if __name__ == "__main__":
    m1, m2 = map(float, input().split())
    print(round(160 + 40*second_moment(m1), 3))
    print(round(128 + 40 * second_moment(m2), 3))