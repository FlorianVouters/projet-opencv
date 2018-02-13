import numpy as np
import matplotlib as mpt
import cv2

img = cv2.imread('Tools/Gliese_581d_V2.pbm', 0)

img = cv2.medianBlur(img, 3)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()