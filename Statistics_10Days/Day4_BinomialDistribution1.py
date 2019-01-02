# 10 Days of Statistics: Day 4: Binomial Distribution


# Factorial through recursion
def fact(x):
    return 1 if x==0 else x*fact(x-1)


def comb(n, x):
    return fact(n)/(fact(x) * fact(n-x))


def binomial(n, p, x):
    return comb(n, x) * (p**x) * ((1-p)**(n-x))


if __name__ == "__main__":
    b, g = map(float, input().split())
    prob_boy = b/(b+g)
    total_prob = 0
    for i in [3, 4, 5, 6]:
        total_prob += binomial(6, prob_boy, i)

    # Rounding to 3 decimal places
    print(round(total_prob, 3))
