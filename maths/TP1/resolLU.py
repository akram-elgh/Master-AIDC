import numpy as np
from LU import LU
from solinf import solinf
from solsup import solsup

eps = np.finfo(float).eps


def resolLU(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Resolu l'equation Ax = b par la methode LU

    Args:
    -----
      A (np.ndarray): matrice
      b (np.ndarray): vecteur

    Returns:
    -------
      x (np.ndarray): vecteur solution de l'equation
    """
    L, U = LU(A)
    y = solinf(L, b)
    x = solsup(U, y)
    return x
