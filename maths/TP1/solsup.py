import numpy as np

eps = np.finfo(float).eps


def solsup(U: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Cette focntion resolu l'equation Ax = b

    Args:
    ------
        U: Matrice triangulair sup
        b: vecteur

    Return:
    -------
        x : vecteur        
    """
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
