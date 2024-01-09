import numpy as np

eps = np.finfo(float).eps


def solinf(U: np.ndarray, b: np.ndarray) -> np.ndarray[float]:
    """Cette focntion resolu l'equation Ax = b

    Args:
    ------
        U: Matrice triangulair inf
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

    x[0] = (b[0] / U[0][0])
    for i in range(1, n):
        S = 0
        for j in range(0, i):
            S += U[i][j] * x[j]
        x[i] = ((b[i] - S) / U[i][i])
    return x
