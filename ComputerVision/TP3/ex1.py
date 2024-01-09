import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import math


def EQM(IO, IC):
    N, M = IO.shape
    S = 0
    for i in range(N):
        for j in range(M):
            S += math.sqrt(IO[i, j] - IC[i, j])
    EQM = (1 / N * M) * S


def PSNR(IO, IC):
    EQM = EQM(IO, IC)
    PSNR = 10 * math.log10(math.sqrt(255) / EQM)
    return PSNR


def coef_haar(A):
    N, M = A.shape
    for i in range(N):
        for j in range(M):
            if j <= N / 2 and i == 2 * (j + 1) or i == 2 * j:
                A[i, j] = 1 / 2
            elif j > N / 2 and j <= N and i == 2 * (j - N / 2) - 1:
                A[i, j] = 1 / 2
            elif j > N / 2 and j <= N and i == 2 * (j - N / 2):
                A[i, j] = -1/2
            elif i > N:
                A[i, j] = 1
            else:
                A[i, j] = 0
                # print(i, j)

    return A


def compression_haar(IM, A, niv):
    # tA = np.transpose(A)
    print("tA : ", A.T.shape)
    print("A : ", A.shape)
    # print("tA : " , tA.shape)
    for i in range(niv):
        B = np.dot(A.T, IM)
        print("B : ", B.shape)
        IC = np.dot(B, A)
    return IC


def decompression_haar(IM, A, niv):
    ID = IM.copy()
    invA = np.linalg.pinv(A)
    invAt = np.linalg.pinv(np.transpose(A))
    for k in range(niv):
        ID = np.dot(invAt, np.dot(ID, invA))
    return ID


image = cv.imread("input.jpg", 0)
IM = np.array(image)
print("IM : ", IM.shape)
# IM = np.resize(IM, [600, 600])
A = np.zeros(IM.shape)
A = coef_haar(A)
IC = compression_haar(IM, A, 1)
ID = decompression_haar(IM, A, 1)

plt.figure(figsize=(10, 10))

plt.subplot(321)
plt.imshow(IM, cmap='gray')
plt.title("image au niv gris")

plt.subplot(322)
plt.imshow(IC, cmap='gray')
plt.title("Image compresse")

plt.subplot(323)
plt.imshow(ID, cmap='gray')
plt.title("Image decompresse")

plt.show()
