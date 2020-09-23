import cv2
import numpy as np

img = cv2.imread("ressources/download.jpg")


width,height = 250,350
pts1 = np.float32([[45,37],[127,29],[73,145],[118,153]])   ##got the coordinate from opening paint and getting the number from there
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))




cv2.imshow('Image', img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)