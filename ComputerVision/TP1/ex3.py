import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

image = cv.imread("input.jpg", 0)
image_array = np.array(image)

hauteur, largeur = image_array.shape

# print(hauteur, largeur)

histogramme = np.zeros((256), dtype=int)
binaire = np.zeros((hauteur, largeur), dtype=int)

for x in range(hauteur):
    for y in range(largeur):
        histogramme[image_array[x, y]] += 1


flattened_list = [element for row in image_array for element in row]
n = len(flattened_list)

tab_tri = sorted(flattened_list)

if n % 2 == 0:
    seuil = (tab_tri[n//2] + tab_tri[n//2 - 1]) / 2
else:
    seuil = tab_tri[n // 2]


for x in range(hauteur):
    for y in range(largeur):
        if image_array[x, y] >= seuil:
            binaire[x, y] = 1


plt.figure(figsize=(10, 10))

plt.subplot(221)
plt.imshow(image_array, cmap='gray')
plt.title("image au niv gris")

plt.subplot(224)
plt.imshow(binaire, cmap='gray')
plt.title("binaire")

plt.subplot(223)
plt.plot(histogramme)
plt.title(f"histogramme seuil : {seuil}")


# plt.tight_layout()
plt.show()
