import numpy as np

eps = np.finfo(float).eps


def LU(A: np.ndarray) -> np.ndarray:
    """retourn la decomposition LU du matrice A

    Args:
    -----
      A (np.ndarray): Matrice

    Returns:
    -------
      L : matrice tirangulair sup
      U : matrice tirangulair inf
    """
    n = len(A)
    L = np.identity(n)
    U = A.copy()
    for k in range(0, n - 1):
        if abs(U[k][k]) < eps:
            print("Error 1")
            return 1
        else:
            c = 0
            for i in range(k + 1, n):
                c = U[i][k] / U[k][k]
                U[i][k] = 0
                L[i][k] = c
                for j in range(k + 1, n):
                    U[i][j] = U[i][j] - c * U[k][j]
    if abs(U[n - 1][n - 1]) < eps:
        # print(A[n - 1][n - 1])
        print("Error de A[n][n]")
        return 1
    return L, U
