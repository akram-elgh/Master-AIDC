import numpy as np
from cholesky import cholesky
from solinf import solinf
from solsup import solsup


def resolchol(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Resolution du system Ax = b par la methode de cholesky

    Args:
    -----
        A (np.ndarray): Matrice symetrique definie positive
        b (np.ndarray : Vecteur

    Returns:
    --------
        x (np.ndarray : Vecteur
    """

    n = len(A)
    x = np.zeros(n)
    y = np.zeros(n)
    B = cholesky(A)
    y = solinf(B, b)
    x = solsup(B.T, y)
    return x
