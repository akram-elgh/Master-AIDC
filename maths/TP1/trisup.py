import numpy as np

eps = np.finfo(float).eps


def trisup(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Retourne une matrice triangulair sup

    Args:
    -----
        A (np.ndarray): matrice
        b (np.ndarray): vecteur

    Returns:
    --------
        A: la matrice A modifier
        b: le vecteur b modifier
    """
    n = len(A)
    for k in range(0, n - 1):
        if abs(A[k][k]) < eps:
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
        # print(A[n - 1][n - 1])
        print("Error de A[n][n]")
        return 1

    return A, b
