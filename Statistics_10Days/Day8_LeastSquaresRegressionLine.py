# 10 Days of Statistics: Day 8: Least Squares Regression Line


# Method 1: Using Numpy and Sklearn

# import numpy as np
# from sklearn import linear_model
#
# X = np.array([95, 85, 80, 70, 60]).reshape(-1, 1)
# Y = np.array([85, 95, 70, 65, 70])
#
# lm = linear_model.LinearRegression()
# lm.fit(X, Y)
#
# # Calculation of y=mx+c with x=80
# print('%.3f' % (lm.coef_[0]*80 + lm.intercept_))


# Method 2: Using Pearson Correlation Coefficient
# from math import sqrt
#
# mean = lambda X: sum(X)/len(X)
#
#
# # Calculate the covariance
# def cov_calc(X, Y):
#     mean_X = mean(X)
#     mean_Y = mean(Y)
#     cov = 0
#     for x, y in zip(X, Y):
#         cov += (x - mean_X) * (y - mean_Y)
#
#     return cov/len(X)
#
#
# def calc_std(X):
#     sq = []
#     mean_X = mean(X)
#     for i in X:
#         sq.append((i-mean_X)**2)
#     std_dev = sqrt(sum(sq)/len(X))
#     return std_dev
#
#
# def pearson_corr_coff(X, Y):
#     cov = cov_calc(X, Y)
#     stdx = calc_std(X)
#     stdy = calc_std(Y)
#     return cov/(stdx * stdy)
#
#
# if __name__ == "__main__":
#     x, y = [], []
#     for i in range(5):
#         student = [int(i) for i in input().split()]
#         x += [student[0]]
#         y += [student[1]]
#
#     # for y = a + bx => a = y - bx
#     b = (pearson_corr_coff(x, y) * calc_std(x) / calc_std(y))
#     a = mean(y) - (b * mean(x))
#
#     # prediction
#     print(round(a + b*80, 3))

# Method 3: Direction calculation of slope
def sum_xy(x, y, n):
    sumxy = 0
    for i in range(n):
        sumxy += x[i]*y[i]

    return sumxy


mean = lambda X: sum(X)/len(X)

if __name__ == "__main__":
    n = 5
    x, y = [], []
    for i in range(n):
        student = [int(i) for i in input().split()]
        x += [student[0]]
        y += [student[1]]

    sumxy = sum_xy(x, y, n)
    xsq = [i * i for i in x]
    ysq = [i * i for i in y]

    b = (n * sumxy - sum(x)*sum(y)) / (n*sum(xsq) - sum(x)*sum(x))
    a = mean(y) - (b * mean(x))

    # prediction
    print(round(a + b*80, 3))