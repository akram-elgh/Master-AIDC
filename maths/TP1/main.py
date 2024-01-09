from doolittle import doolittle
import numpy as np
from inverse import inverse
from resolG import resolG
from LU import LU
from solsup import solsup
from solinf import solinf
from resolchol import resolchol

# ex1 : solsup()
from solsup import solsup
# A = np.array([[1, 2, 3, 4], [1, 4, 9, 16], [1, 8, 27, 64], [1, 16, 81, 256]])
# b = np.array([2, 10, 44, 190])
A = np.array([[4, 8, 12], [3, 8, 13], [2, 9, 18]])
# A = np.array([[1, 2, 3], [5, 2, 1], [3, -1, 1]])

b = np.array([4, 5, 11])
# L, U = LU(A1)
# y = solinf(L, b1)
# x = solsup(U, y)
# print("L = \n", L)
# print("U = \n", U)
# B = inverse(A)
# print("B = \n", B)
print(resolchol(A, b))
