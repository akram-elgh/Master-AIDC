from trisup import trisup
from solsup import solsup


def resolG(A, b):
    """resolu l'equation Ax = b par la methode gaussien

    Args:
    -----
        A (np.ndarray): matrice
        b (np.ndarray): vecteur

    Returns:
        x (np.ndarray): vecteur solution du l'equation
    """
    if trisup(A, b) == 1:
        return 0
    U, e = trisup(A, b)
    x = solsup(U, e)
    return x
