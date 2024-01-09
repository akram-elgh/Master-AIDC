import numpy as np
import math


def cholesky(A: np.ndarray) -> np.ndarray:
    """ Fair la decomposition de A on de matrice B et Bt

    Parameters : 
    ----------
      A: Matrice

    Retour : 
      B : Matrice triangulair inf
      Bt : Le transpose du matrice B  
    """
    n = len(A)
    B = np.zeros(A.shape)
    for j in range(n - 1):
        S = 0
        for k in range(0, n - 1):
            S += B[j, k] ** 2
        B[j, j] = math.sqrt(A[j, j] - S)
        for i in range(j + 1, n):
            S = 0
            for k in range(0, j):
                S += B[i, k] * B[j, k]
            B[i, j] = (A[i, j] - S) / B[j, j]
    S = 0
    for k in range(0, n):
        S += B[n - 1, k] ** 2
    B[n - 1, n - 1] = math.sqrt(A[n - 1, n - 1] - S)

    return B
