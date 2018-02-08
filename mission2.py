import numpy as np
import cv2

img = cv2.imread('Tools/Mars_surface.pbm', 0)

imgsize = img.shape

gaz = 0
compteur = 0
coords = []

for i in range(0, imgsize[0]):
    for j in range(0, imgsize[1]):
        gaz += img[i][j]


print(gaz, " unités de méthane")

cv2.waitKey(0)
cv2.destroyAllWindows()