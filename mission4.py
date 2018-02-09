
import numpy as np
import matplotlib as mpt
import cv2

img = cv2.imread('Tools/Jupiter1.pbm', 0)

imgsize = img.shape

img = cv2.medianBlur(img, 3)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()