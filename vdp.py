import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)


output=np.zeros((800,800,3),np.uint8)

i=0
while(True):
    # capturing the frame 
    ret,frame=cap.read()
    frame=cv.flip(frame,1) 
    blurred_frame=cv.GaussianBlur(frame,(5,5),0) # Blurring the frame to reduce noise during contour detection
    blurred_frame=cv.flip(blurred_frame,1)
    #conversion from rgb to hsv fro color thresholding
    hsv = cv.cvtColor(blurred_frame, cv.COLOR_BGR2HSV)
    
    # lower and upper hsv ranges for blue color
    lower_range = np.array([85,100,92], dtype=np.uint8) 
    upper_range = np.array([112, 255,255], dtype=np.uint8) 
    
    # Appling the mask
    mask = cv.inRange(hsv, lower_range, upper_range)

    #morphological transformation to remove the noise
    kernel = np.ones((5,5),np.uint8)
    opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    dilation = cv.dilate(opening,kernel,iterations = 1)
    dilation=cv.flip(dilation,1)

    #finding contours and selecting the contour with maximum area which would be my marker or stylus
    contours, _ = cv.findContours(dilation, 1, 2)
    areas = [cv.contourArea(c) for c in contours]
    cnt=contours[np.argmax(areas)]
    
    # Finding the centroid of object detected
    M = cv.moments(cnt)
    x = int(M['m10']/M['m00'])
    y = int(M['m01']/M['m00'])
    
    # Drawing the contour in the original frame
    cv.drawContours(frame,contours,-1,(0,255,0),3)
    cv.circle(frame, (x, y), 5, (0, 0, 255), -1)# making a small circle at the centroid as a centre
    if(i==0):
        x1=x
        y1=y
    else:
        cv.line(output,(x1,y1),(x,y),(0,0,255),10) # making a line between the former and present point
        x1=x
        y1=y
    i=i+1
    cv.imshow('virtual drawing pad',output) # displaying the virtual pad
    cv.imshow('stylus detected frame',frame) # displaying the original frame with marker detected as stylus
    
    if cv.waitKey(1)==ord('q'): # assigning 'q' as a exit button
        break

# destroying all the current windows 
cap.release()  
cv.destroyAllWindows()
