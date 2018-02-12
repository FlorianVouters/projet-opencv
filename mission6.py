import numpy as np
import matplotlib as mpt
import cv2

img = cv2.imread('Tools/GD61.pbm', 0)

norm = cv2.normalize(img, img, 0, 255, norm_type=cv2.NORM_MINMAX)

cv2.imshow("image", norm)
cv2.waitKey(0)
cv2.destroyAllWindows()
