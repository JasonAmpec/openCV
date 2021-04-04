import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#img[:]= 0,255,0
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,255),3)
cv2.rectangle(img,(0,0),(250,250),(0,255,255),cv2.FILLED)
cv2.circle(img,(400,50),30,(255,255,0),5)
cv2.putText(img,"Vagina",(300,100),cv2.FONT_HERSHEY_SIMPLEX,1,(120,150,230))



cv2.imshow("Image",img)

cv2.waitKey(0)