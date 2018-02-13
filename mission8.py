import numpy as np
import matplotlib as mpt
from matplotlib import pyplot as pyp
import cv2

img = cv2.imread('Tools/pucar.jpg', 0)

imgsize = img.shape

img2 = np.fft.fft2(img)
imgshift = np.fft.fftshift(img2)
magn_spectr = 20*np.log(np.abs(imgshift))

print(img.shape)

for i in range(0, imgsize[0]):
    for j in range(0, imgsize[1]):
        if i <= 200 or i > imgsize[0] - 200:
            imgshift[i][j] = 255
        if j <= 200 or j > imgsize[1] - 200:
            imgshift[i][j] = 255

ishiftback = np.fft.ifft2(imgshift)
ishiftback = np.abs(ishiftback)


pyp.subplot(131),pyp.imshow(img, cmap = 'gray')
pyp.title('Input Image'), pyp.xticks([]), pyp.yticks([])
pyp.subplot(132),pyp.imshow(magn_spectr, cmap = 'gray')
pyp.title('Magnitude Spectrum'), pyp.xticks([]), pyp.yticks([])
pyp.subplot(133),pyp.imshow(ishiftback, cmap = 'gray')
pyp.title('shiftback'), pyp.xticks([]), pyp.yticks([])
pyp.show()