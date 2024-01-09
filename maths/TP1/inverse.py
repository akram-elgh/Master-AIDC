import numpy as np
# from ex1 import solinf, solsup
from solsup import solsup
from solinf import solinf
from LU import LU


def inverse(A: np.ndarray) -> np.ndarray:
    """retourn l'inverse du matrice A

    Args:
        A (np.ndarray): matrice

    Returns:
        B (np.ndarray): matrice inverse de A
    """
    n = len(A)
    I = np.identity(n)
    # print("I = ", I)
    B = np.zeros(A.shape)
    L, U = LU(A)
    for i in range(n):
        b = np.zeros(n, dtype=int)
        for j in range(n):
            b[j] = I[i, j]
        # print(b)
        y = solinf(L, b)
        x = solsup(U, y)
        B[i] = x
    return B.T
