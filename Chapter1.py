import cv2
import numpy as np
print("Package Imported")

kernel = np.ones((5,5),np.uint8)

img = cv2.imread("venv/Resources/lena.png")

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(13,13),0)
imgCanny = cv2.Canny(img,150,200,)
imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)
imgResize = cv2.resize(img,(300,200))
imgCropped = img[0:200,100:200]

#cv2.imshow("Original",img)
#cv2.imshow("Gray Image",imgGray)
#cv2.imshow("Blur Image",imgBlur)
#cv2.imshow("Canny Image",imgCanny)
#cv2.imshow("Dilation Image",imgDilation)
cv2.imshow("resized",imgResize)
cv2.imshow("Cropped",imgCropped)
print(img.shape)


cv2.waitKey(0)