# 10 Days of Statistics: Day 8: Multiple Linear Regression

import numpy as np


if __name__ == "__main__":
    #  m (the number of observed features) and n (the number of feature sets Andrea studied),
    m, n = map(int, input().split())
    X, Y = [], []
    for i in range(n):
        inp = list(map(float, input().split()))
        X.append(inp[:m])
        Y.append(inp[m:])

    # Number of queries
    q = int(input())
    query_x = []
    for i in range(q):
        data = list(map(float, input().split()))
        query_x.append(data)

    X = np.array(X, float)
    Y = np.array(Y, float)
    query_x = np.array(query_x, float)

    # Center the data
    X_R = X - np.mean(X, axis=0)
    Y_R = Y - np.mean(Y)

    # Calculate xTranspose * x
    xtx = np.dot(X_R.T, X_R)
    xty = np.dot(X_R.T, Y_R)
    B = np.dot(np.linalg.inv(xtx), xty)

    # Prediction
    x_new_R = query_x - np.mean(X, axis=0)
    y_new_R = np.dot(x_new_R, B)
    y_new = y_new_R + np.mean(Y)

    for i in y_new:
        print(round(float(i), 2))