import numpy as np
import matplotlib as mpt
import cv2

img = cv2.imread('Tools/HD215497.pbm', 0)
img2 = cv2.imread('Tools/HD215497.pbm', 1)

imgsize = img.shape

for i in range(0, imgsize[0]):
    for j in range(0, imgsize[1]):
        if img[i][j] < 64:
            img2[i][j] = [0, 53, 84]
        elif img[i][j] < 128:
            img2[i][j] = [148, 0, 0]
        elif img[i][j] < 192:
            img2[i][j] = [0, 0, 192]
        elif img[i][j] < 256:
            img2[i][j] = [0, 192, 192]

cv2.imshow("image", img)
cv2.imshow("imagecolor", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()