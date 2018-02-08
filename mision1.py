import numpy as np
import cv2

img = cv2.imread('Tools/Encelade_surface.pbm', 0)

imgsize = img.shape

print(img.shape)

max = 0
compteur = 0
coords = []

for i in range(0, imgsize[0]):
    for j in range(0, imgsize[1]):
        if img[i][j] > max:
            coords.clear()
            max = img[i][j]
            coord = [i, j]
            coords.append(coord)
        elif img[i][j] == max:
            max = img[i][j]
            coord = [i, j, max]
            coords.append(coord)


for coord in coords :
    img = cv2.circle(img, (coord[0], coord[1]), 10, (255,0,0), 1)
    print(coord)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()