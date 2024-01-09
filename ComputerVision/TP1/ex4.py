import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

image = cv.cvtColor(cv.imread("input.jpg"), cv.COLOR_BGR2RGB)
image_gris = cv.imread("input.jpg", 0)
image_array = np.array(image)
image_gris_array = np.array(image_gris)

hauteur, largeur = image_gris_array.shape

image_array_lum = np.zeros(image_gris_array.shape, dtype=np.uint8)
image_array_cont = np.zeros(image_gris_array.shape, dtype=np.uint8)

for i in range(hauteur) :
  for j in range(largeur) :
      new_value = image_gris_array[i, j] + 50
      if new_value > 255 :
        new_value = 255
      image_array_lum[i, j] = new_value

min = np.min(image_gris_array)
max = np.max(image_gris_array)
for i in range(hauteur) :
  for j in range(largeur) :
      new_value = ( (image_gris_array[i, j] - min) // (max - min) ) * 255
      image_array_cont[i, j] = new_value

plt.figure(figsize=(10, 10))

plt.subplot(221)
plt.imshow(image_array)
plt.title("image RGb")

plt.subplot(222)
plt.imshow(image_gris_array, cmap='gray')
plt.title("image au niv gris")

plt.subplot(223)
plt.imshow(image_array_lum, cmap='gray')
plt.title("Image avec amelioration de lum")

plt.subplot(224)
plt.imshow(image_array_cont, cmap='gray')
plt.title("Image avec amelioration de cont")

plt.show()