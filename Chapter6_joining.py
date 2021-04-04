import cv2
import numpy as np
img = cv2.imread("venv/Resources/lena.png")
img2 = cv2.imread("venv/Resources/pokerResize.png")

imgHor = np.hstack((img,img2))
imgVer = np.vstack((imgHor,imgHor))
imgResized = cv2.resize(imgVer,(512,512))


cv2.imshow("horizontal",imgResized)
cv2.waitKey(0)