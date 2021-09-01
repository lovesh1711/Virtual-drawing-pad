import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)
def nothing(x):
    pass
cv.namedWindow('window')
cv.createTrackbar('LH','window',0,255,nothing)
cv.createTrackbar('LS','window',0,255,nothing)
cv.createTrackbar('LV','window',0,255,nothing)
cv.createTrackbar('HH','window',255,255,nothing)
cv.createTrackbar('HS','window',255,255,nothing)
cv.createTrackbar('HV','window',255,255,nothing)

while(True):
    ret,frame=cap.read()
    frame=cv.flip(frame,1)
    blurred_frame=cv.GaussianBlur(frame,(5,5),0)
    blurred_frame=cv.flip(blurred_frame,1)
    hsv = cv.cvtColor(blurred_frame, cv.COLOR_BGR2HSV)
    LH=cv.getTrackbarPos('LH','window')
    LS=cv.getTrackbarPos('LS','window')
    LV=cv.getTrackbarPos('LV','window')
    HH=cv.getTrackbarPos('HH','window')
    HS=cv.getTrackbarPos('HS','window')
    HV=cv.getTrackbarPos('HV','window')
    lower_range = np.array([LH,LS,LV], dtype=np.uint8)  #(85,100,92)
    upper_range = np.array([HH, HS,HV], dtype=np.uint8) #(112,255,255)
    mask = cv.inRange(hsv, lower_range, upper_range)
    
    cv.imshow('mask',mask)
    if cv.waitKey(1)==ord('q'):
        break

cap.release()
cv.destroyAllWindows()