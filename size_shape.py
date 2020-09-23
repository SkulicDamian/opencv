import cv2
import numpy as np

img = cv2.imread("ressources/test.png")
print(img.shape)

imgResize = cv2.resize(img,(300,200))

imgCropped = img[0:200,200:500]

cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image cropped",imgCropped)
cv2.waitKey(0)