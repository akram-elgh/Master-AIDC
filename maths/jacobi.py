import numpy as np
import math

def norm(x) :
  norm = 0
  n = len(x)
  for i in range(n):
    norm += x[i] ** 2 
  return float(math.sqrt(norm))

def jacobi(A, b, x0, N, eps) : 
  n = len(A)
  nrm = 0
  for k in range(N):
    x = np.zeros(n)
    for i in range(n) :
      S = 0
      for j in range(n) :
        if j != i :
          S += A[i, j] * x0[j]
      x[i] = (b[i] - S) / A[i, i]
    nrm = norm(x - x0) ** 2 / (norm(x) ** 2 )
    if nrm <= eps :
      return x, k
    else :
      x0 = x
      
  print("La methode de jacobi n'est pas converger")   
  return 0, 0
  
A = np.array([[1, -2, 2], [-1, 1, -1], [-2, -2, 1]])
A2 = np.array([[1, -1, 2], [-2, 1, 3], [0, 2, 1]])
x0 = np.array([1, 2, 3])
b = np.array([1, 2, 3])
N = 10
eps = np.finfo(float).eps


x, k = jacobi(A2, b, x0, N, eps)  
print(x, k)