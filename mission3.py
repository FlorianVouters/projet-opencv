import numpy as np
import cv2

img = cv2.imread('Tools/Europa_surface.pbm', 0)

imgsize = img.shape

for i in range(0, imgsize[0]):
    for j in range(0, imgsize[1]):
        if img[i][j] <= 200:
            img[i][j] = 0
        else:
            img[i][j] = 255


cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()