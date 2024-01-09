import numpy as np
import matplotlib.pyplot as plt

eps = np.finfo(float).eps


def afficheMatrice(M):
    n = len(M)
    for i in range(n):
        for j in range(n):
            print(f"|{M[i][j]}|", end=" ")
        print()


def afficheVecteur(b):
    n = len(b)
    for i in range(n):
        print(f"|{b[i]}|")


def saisirMatrice():
    n = int(input("Donner la taille du matrice : "))
    U = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            U[i][j] = int(input(f"Donner l'element U[{i}][{j}] : "))

    for i in range(n):
        for j in range(n):
            print(f"|{U[i][j]}|", end=" ")
        print()

    return U

# A = saisirMatrice()


def saisirVecteur(U):
    n = len(U)
    b = np.zeros(n, dtype=int)
    for i in range(n):
        b[i] = int(input(f"Donner l'element b[{i}] : "))

    return b

# b = saisirVecteur(A)


def solsup(U, b):
    n = len(U)
    x = np.zeros(n)
    for i in range(n):
        if abs(U[i][i]) < eps:
            return 0

    x[n - 1] = (b[n - 1] / U[n-1][n-1])
    for i in range(n-1, -1, -1):

        S = 0
        for j in range(i+1, n):
            S += U[i][j] * x[j]
        x[i] = ((b[i] - S) / U[i][i])
    return x


def trisup(A, b):
    n = len(A)
    for k in range(0, n - 1):
        if abs(A[k][k]) < eps:
            # print(f"A[{k}] = {A[k][k]}")
            print("Error 1")
            return 1
        else:
            c = 0
            for i in range(k + 1, n):
                c = A[i][k] / A[k][k]
                b[i] = b[i] - c * b[k]
                A[i][k] = 0
                for j in range(k + 1, n):
                    A[i][j] = A[i][j] - c * A[k][j]
    if abs(A[n - 1][n - 1]) < eps:
        print(A[n - 1][n - 1])
        print("Error de A[n][n]")
        return 1

    return A, b


def resolG(A, b):
    U, e = trisup(A, b)
    return solsup(U, e)


def LU(A):
    n = len(A)
    L = np.identity(n)
    for k in range(0, n - 1):
        if abs(A[k][k]) < eps:
            print("Error 1")
            return 1
        else:
            c = 0
            for i in range(k + 1, n):
                c = A[i][k] / A[k][k]
                A[i][k] = 0
                L[i][k] = c
                for j in range(k + 1, n):
                    A[i][j] = A[i][j] - c * A[k][j]
    if abs(A[n - 1][n - 1]) < eps:
        print(A[n - 1][n - 1])
        print("Error de A[n][n]")
        return 1

    return L, A


def solinf(U, b):
    n = len(U)
    x = np.zeros(n)
    for i in range(n):
        if abs(U[i][i]) < eps:
            return 0

    x[0] = (b[0] / U[0][0])
    for i in range(1, n):
        S = 0
        for j in range(0, i):
            S += U[i][j] * x[j]
        x[i] = ((b[i] - S) / U[i][i])
    return x


def resolLU(A, b):
    L, U = LU(A)
    y = solinf(L, b)
    x = solsup(U, y)
    return x

# L , U = LU(A)
# print(L)
# print(U)

# U, b = trisup(A,b)
# print(U)
