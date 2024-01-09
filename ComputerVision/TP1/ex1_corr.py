import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

image = cv.cvtColor(cv.imread("input.jpg"), cv.COLOR_BGR2RGB)
image_array = np.array(image)
hauteur, largeur, canal = image_array.shape
R = np.zeros(image_array.shape, dtype=np.uint8)
G = np.zeros(image_array.shape, dtype=np.uint8)
B = np.zeros(image_array.shape, dtype=np.uint8)

for x in range(hauteur):
    for y in range(largeur):
        R[x, y, 0] = image_array[x, y, 0]


for x in range(hauteur):
    for y in range(largeur):
        G[x, y, 1] = image_array[x, y, 1]

for x in range(hauteur):
    for y in range(largeur):
        B[x, y, 2] = image_array[x, y, 2]

plt.figure(figsize=(10, 10))

plt.subplot(221)
plt.imshow(image_array)
plt.title("image RGB")

plt.subplot(222)
plt.imshow(R)
plt.title("image R")

plt.subplot(223)
plt.imshow(G)
plt.title("image G")

plt.subplot(224)
plt.imshow(B)
plt.title("image B")

plt.tight_layout()
plt.show()
