import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import math
image = cv.imread("letter_K.png", 0)
image = cv.resize(image, [256, 256])


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


def moment(img, p, q):
    h, l = img.shape
    imgarr = np.array(img)
    mpq = 0
    for i in range(h):
        for j in range(l):
            mpq += float((i ** p) * (j ** q) * imgarr[i, j])
    return mpq


def mmnt_cent(img, p, q):
    xbar = float(moment(img, 1, 0) / moment(img, 0, 0))
    ybar = float(moment(img, 0, 1) / moment(img, 0, 0))
    h, l = img.shape
    upq = 0
    imgarr = np.array(img)
    for i in range(h):
        for j in range(l):
            upq += float(((i - xbar) ** p) * ((j - ybar) ** q) * imgarr[i, j])
    return upq


def mmnt_cent_norm(img, p, q):
    h, l = img.shape
    gama = float(((p + q) / 2 ) + 1)
    alpha = mmnt_cent(img, p, q) / (mmnt_cent(img, 0, 0) ** gama)
    return alpha


def mmts_HU(img):
    phi = np.zeros(7)
    # phi[0] = mmnt_cent_norm(img, 2, 0) - mmnt_cent_norm(img, 0, 2)
    # phi[1] = (mmnt_cent_norm(img, 2, 0) - mmnt_cent_norm(img, 0, 2)) ** 2 +  4 * (mmnt_cent_norm(img, 1, 1) ** 2)
    # phi[2] = (mmnt_cent_norm(img, 3, 0) - mmnt_cent_norm(img, 1, 2) ** 2) + (3 * mmnt_cent_norm(img, 1, 2) - mmnt_cent_norm(img, 0, 3)) ** 2
    # phi[3] = (mmnt_cent_norm(img, 3, 0) + mmnt_cent_norm(img, 1, 2)) ** 2 + (mmnt_cent_norm(img, 2, 1) + mmnt_cent_norm(img, 0, 3)) ** 2
    # phi[4] = ((mmnt_cent_norm(img, 3, 0) - 3 * mmnt_cent_norm(img, 1, 2)) * (mmnt_cent_norm(img, 3, 0) + mmnt_cent_norm(img, 1, 2))) * ((mmnt_cent_norm(img, 3, 0) + mmnt_cent_norm(img,1, 2)) ** 2 - (3 * (mmnt_cent_norm(img) + mmnt_cent_norm(img, 0, 3)) ** 2)) + ((3 * ))
    a_0_2 = mmnt_cent_norm(img, 0, 2)
    a_0_3 = mmnt_cent_norm(img, 0, 3)
    a_1_1 = mmnt_cent_norm(img, 1, 1)
    a_1_2 = mmnt_cent_norm(img, 1, 2)
    a_2_0 = mmnt_cent_norm(img, 2, 0)
    a_2_1 = mmnt_cent_norm(img, 2, 1)
    a_3_0 = mmnt_cent_norm(img, 3, 0)
    phi[0] = a_2_0 - a_0_2
    phi[1] = (a_2_0 - a_0_2) ** 2 + (4 * a_1_1) ** 2
    phi[2] = (a_3_0 - a_1_2) ** 2 + (3 * a_1_2 - a_0_3) ** 2
    phi[3] = (a_3_0 + a_1_2) ** 2 + (a_2_1 + a_0_3) ** 2
    phi[4] = (a_3_0 - 3 * a_1_2) * (a_3_0 + a_1_2) * ((a_3_0 + a_1_2) ** 2 - 3 * (a_2_1 + a_0_3) ** 2 )
    + (3 * a_2_1 - a_0_3) * (a_2_1 + a_0_3) * (3 * (a_3_0 + a_1_2) ** 2 - ((a_2_1 + a_0_3) ** 2))
    phi[5] = (a_2_0 * a_0_2) * ((a_3_0 + a_1_2) ** 2 - (a_2_1 + a_0_3) ** 2 ) + 4 * a_1_1 * (a_3_0 + a_1_2) * (a_2_1 
+ a_0_3)
    phi[6] = (3 * a_2_1 - a_0_3) * (a_3_0 + a_1_2) * ((a_3_0 + a_1_2) ** 2 - 3 * ((a_2_1 + a_0_3) **2 )) + ( 3 * a_1_2 - a_0_3) * (a_2_1+ a_0_3 ) * ((3 * (a_3_0 + a_1_2) **2 ) - ((a_2_1 + a_0_3) ** 2))
    
    return phi

# IM = np.array(image)
image2 = cv.imread("a.jpeg", 0)
binaire = binarisation(image)
binaire2 = binarisation(image2)
inverse = inversion(binaire)
inverse2 = inversion(binaire2)
phi = mmts_HU(inverse)
phi2 = mmts_HU(inverse2)

print(phi)
print(phi2)

# im = cv.imread("letter_K.png",cv.IMREAD_GRAYSCALE)
# _,im = cv.threshold(im, 128, 255, cv.THRESH_BINARY)
# # Calculate Moments 
# moments = cv.moments(im) 
# # Calculate Hu Moments 
# huMoments = cv.HuMoments(moments)
# print(huMoments)


# plt.figure(figsize=[10, 10])

# plt.subplot(221)
# plt.imshow(IM, cmap='gray')
# plt.title("image au niv gris")

# plt.subplot(222)
# plt.imshow(binaire, cmap='gray')
# plt.title("binaire")

# plt.subplot(223)
# plt.imshow(inverse, cmap='gray')
# plt.title("inverse")


# plt.show()
