import numpy as np
import matplotlib as mpt
from matplotlib import pyplot as plt
import cv2

img = cv2.imread("Images/U2_surface.pbm", 0)

canny = cv2.Canny(img, 200, 300)

contour = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) ##Ne fonctionne pas sur mon ordinateur

contour = contour[0] if imutils.is_cv2() else contour[1]

contour = sorted(contour, key = cv2.contourArea, reverse = True)[:10]

cv2.drawContours(image, compt, 0, (0, 255, 0), 3)

cv2.imshow("Canny", canny)
cv2.imshow("Objet non identifie", image)
cv2.waitKey(0)