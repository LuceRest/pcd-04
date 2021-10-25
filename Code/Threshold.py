import cv2

image = cv2.imread('Res\car.jpg')
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, imgThresh = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, imgThresh2 = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)

cv2.imshow("Citra Asli", image)
cv2.imshow('Citra Hasil Thresholding', imgThresh)
cv2.imshow('Citra Hasil Thresholding2', imgThresh2)

if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()



'''

# Python program to illustrate
# simple thresholding type on an image
	
# organizing imports
import cv2
import numpy as np

# path to input image is specified and
# image is loaded with imread command

image = cv2.imread('Res\car.jpg')
cv2.imshow("Citra Asli", image)

# cv2.cvtColor is applied over the
# image input with applied parameters
# to convert the image in grayscale

# Mengubah warna gambar menjadi grayscale
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# applying different thresholding
# techniques on the input image
# all pixels value above 120 will
# be set to 255

# cv2.threshold(src, tresh value, max value of thresh, type thresh)
ret, imgThresh = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)


# the window showing output images
# with the corresponding thresholding
# techniques applied to the input images
cv2.imshow('Binary Threshold', imgThresh)


# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()




'''