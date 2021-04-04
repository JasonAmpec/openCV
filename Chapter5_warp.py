import cv2
import numpy as np

width,height = 200,240

img = cv2.imread("venv/Resources/pokerResize.png")

pts1 = np.float32([[18,46],[214,34],[73,282],[239,278]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("warp",imgOutput)



cv2.waitKey(0)