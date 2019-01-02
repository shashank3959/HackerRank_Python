# 10 Days of Statistics: Day 4: Binomial Distribution 2

# Factorial through recursion
def fact(x):
    return 1 if x==0 else x*fact(x-1)


def comb(n, x):
    return fact(n)/(fact(x) * fact(n-x))


def binomial(n, p, x):
    return comb(n, x) * (p**x) * ((1-p)**(n-x))


if __name__ == "__main__":
    p, n = map(float, input().split())

    # Convert the percentage to probability
    p = p/100

    # No more than 2 rejects
    total_prob = 0
    for i in [0, 1, 2]:
        total_prob += binomial(n, p, i)

    # Rounding to 3 decimal places
    print(round(total_prob, 3))

    # At least 2 rejects
    total_prob = 0
    for i in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
        total_prob += binomial(n, p, i)

    # Rounding to 3 decimal places
    print(round(total_prob, 3))