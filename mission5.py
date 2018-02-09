import numpy as np
import matplotlib as mpt
import cv2

img = cv2.imread('Tools/Gliese_667Cc_surface.pbm', 0)


histEq = cv2.equalizeHist(img)

cv2.imshow("image", histEq)
cv2.waitKey(0)
cv2.destroyAllWindows()
