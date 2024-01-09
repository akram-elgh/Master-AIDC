import numpy as np
import math

def norm(x) :
  norm = 0
  n = len(x)
  for i in range(n):
    norm += x[i] ** 2 
  print(norm)
  return math.sqrt(norm)

def gausseidel(A, b, x0, N, eps) : 
  n = len(A)
  nrm = 0
  for k in range(N):
    x = x0.copy()
    for i in range(n) :
      S1 = 0
      S2 = 0
      for j in range(n) :
        if j != i :
          if j < i :
            S1 += A[i, j] * x[j]
          else : 
            S2 += A[i, j] * x0[j]
      x[i] = (b[i] - S1 - S2) / A[i, i]
    nrm = ((norm(x - x0) ** 2) / norm(x) ** 2 )
    if nrm < eps :
      return x, k
    else :
      x0 = x
      
  print("La methode de gaussiedel n'est pas converger")   
  return 0, 0
  
A = np.array([[1, -2, 2], [-1, 1, -1], [-2, -2, 1]])
A2 = np.array([[1, -1, 2], [-2, 1, 3], [0, 2, 1]])
x0 = np.array([1, 2, 3])
b = np.array([1, 2, 3])
N = 7
eps = np.finfo(float).eps


x, k = gausseidel(A2, b, x0, N, eps)  
print(x, k)