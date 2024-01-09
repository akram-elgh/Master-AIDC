import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
# from ex1 import noisy
import random 

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

IB = noisy(IG, 5000)

def filtreM(IB, ord) :
  IM = np.copy(IB)
  h, l = IB.shape
  pas = ord // 2
  # tmp = []
  for x in range(pas, h - pas):
    for y in range(pas, l - pas) :
      tmp = []
      for i in range(-pas , pas + 1) :
        for j in range(-pas, pas + 1) :
          tmp.append(IB[ x + i, y + j])
      tmp.sort()
      IM[x, y] = np.uint8(tmp[ord * ord // 2])
      
  return IM

def filtreMax(IB, ord) :
  IM = np.copy(IB)
  h, l = IB.shape
  pas = ord // 2    
  for x in range(pas, h - pas):
    for y in range(pas, l - pas) :
      min = 0
      max = 0
      tmp = []
      for i in range(-pas , pas + 1) :
        for j in range(-pas, pas + 1) :
          if x != 0 or j != 0 :
            tmp.append(IB[ x + i, y + j])
      tmp.sort()
      min = tmp[0]
      max = tmp[len(tmp) - 1]
      if IM[x, y ] > max or IM[x, y] < min :
        IM[x, y] = max 
    
    
  return IM  
  
      
   
IM = filtreM(IB, 5)
IFM = filtreMax(IB, 5)
   
plt.figure(figsize=(10, 10))

plt.subplot(321)
plt.imshow(IG, cmap='gray')
plt.title("image au niv gris")

plt.subplot(322)
plt.imshow(IB, cmap='gray')
plt.title("Image bruite")    

plt.subplot(323)
plt.imshow(IM, cmap='gray')
plt.title("Image filtre median")    

plt.subplot(324)
plt.imshow(IFM, cmap='gray')
plt.title("Image filtre maximum")  

# plt.subplot(325)
# plt.imshow(IFB, cmap='gray')
# plt.title("Image filtre binomial")  

plt.show()
