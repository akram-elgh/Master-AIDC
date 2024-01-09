import random
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

image = cv.imread("input.jpg", 0)
IG = np.array(image)

def noisy(image, to) :
  IB = image.copy()
  hauteur , largeur = image.shape
  for i in range(to) :
    x = random.randint(0, hauteur - 1)
    y = random.randint(0, largeur - 1)
    intensite = random.randint(0, 255)
    IB[x, y] = intensite
    
  return IB

def filtrage(IB, F):
  IF = IB.copy()
  h, l = IB.shape 
  hf , lf = F.shape
  pas = hf // 2
  sm = np.sum(F)
  
  
  for x in range(pas, h-pas):
    for y in range(pas, l-pas):
      a = 0
      S = 0
      for i in range(-pas, pas + 1) :
        b = 0
        for j in range (-pas, pas + 1) :
          S += IF[x + i, y + j] * F[a, b]
          b += 1
        a += 1
    IF[x, y] = S//sm
    
  return IF
   
IB = noisy(IG, 5000)
FG = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
FM = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
FB = np.array([[1, 4, 6, 4, 1], [4, 16, 24, 16, 4], [6, 24, 36, 24, 6], [4, 16, 24, 16, 4], [1, 4, 6, 4, 1]])
# FG = np.multiply(FG, 1 // 16)
IFM = filtrage(IB, FM)
IFG = filtrage(IB, FG)
IFB = filtrage(IB, FB)

plt.figure(figsize=(10, 10))

plt.subplot(321)
plt.imshow(IG, cmap='gray')
plt.title("image au niv gris")

plt.subplot(322)
plt.imshow(IB, cmap='gray')
plt.title("Image bruite")    

plt.subplot(323)
plt.imshow(IFG, cmap='gray')
plt.title("Image filtre gaussien")    

plt.subplot(324)
plt.imshow(IFM, cmap='gray')
plt.title("Image filtre median")  

plt.subplot(325)
plt.imshow(IFB, cmap='gray')
plt.title("Image filtre binomial")  

plt.show()