# 10 Days of Statistics: Day 7: Pearson Correlation Coefficient
from math import sqrt

mean = lambda X: sum(X)/len(X)


# Calculate the covariance
def cov_calc(X, Y):
    mean_X = mean(X)
    mean_Y = mean(Y)
    cov = 0
    for x, y in zip(X, Y):
        cov += (x - mean_X) * (y - mean_Y)

    return cov/len(X)


def calc_std(X):
    sq = []
    mean_X = mean(X)
    for i in X:
        sq.append((i-mean_X)**2)
    std_dev = sqrt(sum(sq)/len(X))
    return std_dev


def pearson_corr_coff(X, Y):
    cov = cov_calc(X, Y)
    stdx = calc_std(X)
    stdy = calc_std(Y)
    return cov/(stdx * stdy)


if __name__ == "__main__":
    n = int(input())
    X = list(map(float, input().split()))
    Y = list(map(float, input().split()))
    print("{:.3f}".format(pearson_corr_coff(X, Y)))
