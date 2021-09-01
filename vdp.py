import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)


output=np.zeros((800,800,3),np.uint8)

i=0
while(True):
    ret,frame=cap.read()
    frame=cv.flip(frame,1)
    blurred_frame=cv.GaussianBlur(frame,(5,5),0)
    blurred_frame=cv.flip(blurred_frame,1)
    hsv = cv.cvtColor(blurred_frame, cv.COLOR_BGR2HSV)
    
    lower_range = np.array([85,100,92], dtype=np.uint8) 
    upper_range = np.array([112, 255,255], dtype=np.uint8) 
    mask = cv.inRange(hsv, lower_range, upper_range)

    #morphological transformation
    kernel = np.ones((5,5),np.uint8)
    opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    dilation = cv.dilate(opening,kernel,iterations = 1)
    dilation=cv.flip(dilation,1)

    #finding contours
    contours, _ = cv.findContours(dilation, 1, 2)
    areas = [cv.contourArea(c) for c in contours]
    cnt=contours[np.argmax(areas)]

    M = cv.moments(cnt)
    x = int(M['m10']/M['m00'])
    y = int(M['m01']/M['m00'])
    cv.drawContours(frame,contours,-1,(0,255,0),3)
    cv.circle(frame, (x, y), 5, (0, 0, 255), -1)
    if(i==0):
        x1=x
        y1=y
    else:
        cv.line(output,(x1,y1),(x,y),(0,0,255),10)
        x1=x
        y1=y
    i=i+1
    cv.imshow('virtual drawing pad',output)
    cv.imshow('stylus detected frame',frame)
    if cv.waitKey(1)==ord('q'):
        break

cap.release()
cv.destroyAllWindows()
