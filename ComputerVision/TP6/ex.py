import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import math


def pochhammer(a, k) :
  f = 1
  if k >= 1 :
    for i in range(k) :
      f *= (a + i)
  return f 

def fact(n) :
  f = 1
  if n > 1 : 
    for i in range(1, n + 1) :
      f *= i
  return f 

def squared(n, N) :
  f = (fact(n + N) / ((2 * n + 1) * fact(N - n -1)))
  return f

def polynomial(x, n, M) :
  tnx = 0
  for k in range(n + 1) : 
    c = pochhammer(-n, k)
    d = pochhammer(-x, k)
    e = pochhammer(1 + n, k)
    f = fact(k) ** 2
    g = pochhammer(1 - M, k)
    tnx += (e * d * c) / (f * g)
  a = pochhammer(1 - M, n)
  b = math.sqrt(squared(n, M))
  tnx *= (a / b)
  return tnx

def moment_n_m(F, n, m) :
  M, N = F.shape
  tnm = 0
  for x in range(M) :
    for y in range(N) :
      tnm += polynomial(x, n, M) * polynomial(y, m, N) * F[x, y]
  return tnm

def tchibichef(F, ordre) :      
  v = []
  for n in range(ordre + 1) :
    for m in range(ordre + 1) :
      if n + m <= ordre :
        S = moment_n_m(F, n, m)
        v.append(S) 
        
  return v      

def binarisation(img):
    h, l = img.shape
    S = np.sum(img)
    N = S // img.size
    print(N)
    IM = np.zeros(img.shape)
    for i in range(h):
        for j in range(l):
            if img[i, j] >= N:
                IM[i, j] = 1
    return IM
  

def inversion(img):
    h, l = img.shape
    IV = img.copy()
    for i in range(h):
        for j in range(l):
            if IV[i, j] == 0:
                IV[i, j] = 1
            else:
                IV[i, j] = 0
    return IV
  
  
image = cv.imread("letter.png", 0)
i = cv.resize(image, [200, 200])
binaire = binarisation(i)
# binaire2 = binarisation(image2)
inverse = inversion(binaire)
# inverse2 = inversion(binaire2)
# print(inverse)
phi = tchibichef(inverse, 3)

print(phi)  

# plt.figure(figsize=[10, 10])

# plt.subplot(221)
# plt.imshow(inverse, cmap="grey")

# plt.show()