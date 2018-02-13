import numpy as np
import matplotlib as mpt
from matplotlib import pyplot as plt
import cv2

img = cv2.imread('Tools/Gliese_581d_V2.pbm', 0)

"""imf = np.float32(img)/255.0
dct = cv2.dct(imf)

shape = dct.shape

for i in range(0, shape[0]):
    for j in range(0, shape[1]):
        if i < 20 and j < 20 and i > 80 and j > 80:
            dct[i][j] = 0

dct = cv2.idct(dct)"""

dct = cv2.medianBlur(img, 3)

cv2.imshow("image", dct)
cv2.waitKey(0)
cv2.destroyAllWindows()