import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

image = cv.imread("input.jpg", 0)
image_array = np.array(image)

hauteur, largeur = image_array.shape

# print(hauteur, largeur)

histogramme = np.zeros((256), dtype=int)
histogrammeC = np.zeros((256), dtype=int)

for x in range(hauteur):
    for y in range(largeur):
        histogramme[image_array[x, y]] += 1


for i in range(1, 255):
    histogrammeC[i] = histogrammeC[i-1] + histogramme[i]

plt.figure(figsize=(10, 10))

plt.subplot(221)
plt.imshow(image_array, cmap='gray')
plt.title("image au niv gris")

plt.subplot(223)
plt.plot(histogramme)
plt.title("histogramme")

plt.subplot(224)
plt.plot(histogrammeC)
plt.title("histogramme cimule")

# plt.tight_layout()
plt.show()
