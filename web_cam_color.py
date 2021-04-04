import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(10,100)

def empty(a):
    pass

def getContours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>0:
            cv2.drawContours(imgContour,cnt,-1,(255,255,255),4)
            peri = cv2.arcLength(cnt,False)
            approx = cv2.approxPolyDP(cnt,0.1*peri,False)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (255, 0, 0), 2)

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

#Blue
B_h_min = 69
B_h_max = 129
B_s_min = 86
B_s_max = 255
B_v_min = 72
B_v_max = 255

#Green
G_h_min = 26
G_h_max = 86
G_s_min = 84
G_s_max = 255
G_v_min = 0
G_v_max = 255


cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar",640,240)
cv2.createTrackbar("MinVal","TrackBar",0,300,empty)
cv2.createTrackbar("MaxVal","TrackBar",300,300,empty)
cv2.createTrackbar("Edge","TrackBar",3,20,empty)
cv2.createTrackbar("Ape","TrackBar",3,20,empty)

while True:
    success,img = cap.read()
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    imgContour = img.copy()

    MinVal = cv2.getTrackbarPos("MinVal", "TrackBar")
    MaxVal = cv2.getTrackbarPos("MaxVal", "TrackBar")
    edge = cv2.getTrackbarPos("Edge","TrackBar")
    ape = cv2.getTrackbarPos("Ape","TrackBar")

    Blue_lower = np.array([B_h_min,B_s_min,B_v_min])
    Blue_upper = np.array([B_h_max,B_s_max,B_v_max])
    Blue_mask = cv2.inRange(imgHSV,Blue_lower,Blue_upper)

    Green_lower = np.array([G_h_min,G_s_min,G_v_min])
    Green_upper = np.array([G_h_max,G_s_max,G_v_max])
    Green_mask = cv2.inRange(imgHSV,Green_lower,Green_upper)

    B_imgResults = cv2.bitwise_and(img,img, mask=Blue_mask)
    G_imgResults = cv2.bitwise_and(img,img, mask=Green_mask)

    imgBlur_B = cv2.GaussianBlur(B_imgResults,(5,5),3)
    imgCanny_B = cv2.Canny(imgBlur_B,50,50)

    imgBlur_G = cv2.GaussianBlur(G_imgResults,(7,7),3)
    G_filter = cv2.bilateralFilter(imgBlur_G, 7, 50, 50)
    imgCanny_G = cv2.Canny(G_filter,MinVal,MaxVal,ape)


    getContours(imgCanny_G)

    imgStack = stackImages(0.6,([img,imgCanny_G],[imgBlur_G,imgContour]))

    cv2.imshow("hsv", imgStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
