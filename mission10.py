import numpy as np
import matplotlib as mpt
from matplotlib import pyplot as plt
import cv2

img = cv2.imread('Tools/U1_surface.pbm', 0)
img_gaussian = cv2.GaussianBlur(img,(3,3),0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
sobel = sobelx + sobely
edges = cv2.Canny(img,100,200)

#prewitt
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)


cv2.imshow("image", laplacian)
cv2.imshow("sobelx", sobelx)
cv2.imshow("sobely", sobely)
cv2.imshow("sobel", sobel)
cv2.imshow("canny", edges)
cv2.imshow("Prewitt X", img_prewittx)
cv2.imshow("Prewitt Y", img_prewitty)
cv2.imshow("Prewitt", img_prewitty + img_prewittx)
cv2.waitKey(0)
cv2.destroyAllWindows()