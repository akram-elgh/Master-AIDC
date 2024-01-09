import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

image = cv.imread("test.png", 0)
IM = np.array(image)


def hist(IM):
    h, l = IM.shape
    hist = np.zeros((256))
    for x in range(h):
        for y in range(l):
            hist[IM[x, y]] += 1

    return hist


# def segment(IM):
#     IST = []
#     hist = cv.calcHist([IM], [0], None, [256], [0, 256])
#     h, l = IM.shape
#     for k in range(256):
#         if hist[k] > 0 and k != 255:
#             I = np.zeros(IM.shape)
#             for i in range(h):
#                 for j in range(l):
#                     if IM[i, j] != k:
#                         I[i, j] = 255
#                     else:
#                         print(k)
#                         I[i, j] = k
#             IST.append(I)
#     return IST


def segment(IM):
    IST = []
    hist = cv.calcHist([IM], [0], None, [256], [0, 256])
    h, l = IM.shape
    for k in range(256):
        if hist[k] > 0 and k != 255:
            I = IM.copy()  # Create a copy of the original image
            I[IM != k] = 255
            I = cv.cvtColor(I, cv.COLOR_GRAY2BGR)
            IST.append(I)
    return IST


hist = cv.calcHist([IM], [0], None, [256], [0, 255])

IST = segment(IM)

# print(IST[1])

plt.figure(figsize=(10, 10))

plt.subplot(221)
plt.imshow(IM, cmap='gray')
plt.title("image au niv gris")


plt.subplot(222)
# plt.plot(hist)
plt.imshow(IST[0], cmap='gray')
plt.title("image au niv gris")

plt.subplot(223)
plt.imshow(IST[1], cmap='gray')
plt.title("image au niv gris")

plt.subplot(224)
plt.imshow(IST[2], cmap='gray')
plt.title("image au niv gris")

plt.show()
