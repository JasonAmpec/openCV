import cv2
import numpy as np
print("Package Imported")

def empty(a):
    pass

cap = cv2.VideoCapture(0)
cap.set(10,100)

cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar",640,240)
cv2.createTrackbar("Hue Min","TrackBar",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBar",179,179,empty)
cv2.createTrackbar("Sat Min","TrackBar",0,255,empty)
cv2.createTrackbar("Sat Max","TrackBar",255,255,empty)
cv2.createTrackbar("Val Min","TrackBar",0,255,empty)
cv2.createTrackbar("Val Max","TrackBar",255,255,empty)

while True:
    success,img = cap.read()
    imgBlur = cv2.GaussianBlur(img, (15, 15), 0)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    imgLUV = cv2.cvtColor(img,cv2.COLOR_BGR2LUV)

    h_min = cv2.getTrackbarPos("Hue Min", "TrackBar")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBar")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBar")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBar")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBar")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBar")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResults = cv2.bitwise_and(img,img,mask=mask)
    #imgHor = np.hstack((img,mask,imgLUV))
    #imgResized = cv2.resize(imgHor, (640+320, 240))
    #cv2.imshow("Video",imgResized)
    cv2.imshow("hsv",imgResults)
    cv2.imshow("original",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


#Blue
#hue min 51, max 135
#sat min 99, max 255
#val min 87,255