
# can capture in BW

import sys
import cv2
import cv
import time
import numpy
import os
 
cap = cv2.VideoCapture('testLEDDark_cut.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    image_thr = frame.copy()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
       # first is hue, second is saturation
    image_thr[(hsv[...,1]<025) | (hsv[...,2]<115)]=0

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',image_thr)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
