import numpy as np


def doolittle(A):
    n = len(A)
    U = np.zeros((n, n), dtype=float)
    L = np.identity(n)

    for i in range(0, n - 1):
        for j in range(i, n):
            S = 0
            for k in range(0, i - 1):
                S += L[i, k] * U[k, j]
            U[i, j] = A[i, j] - S

        for j in range(i + 1, n):
            S = 0
            for k in range(0, i):
                S += L[j, k] * U[k, i]
            L[j, i] = (1 / U[i, i]) * (A[j, i] - S)

    S = 0
    for k in range(1, n-1):
        S += L[n - 1, k] * U[k, n - 1]
    U[n - 1, n - 1] = A[n - 1, n - 1] - S

    return L, U
