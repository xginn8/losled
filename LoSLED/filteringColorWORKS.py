
# can capture in BW

import sys
import cv2
import cv
import time
import numpy as np
import os


cap = cv2.VideoCapture(0)

while(1):
    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lowerYellow = np.array([ 80,100,100])
    upperYellow = np.array([100,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lowerYellow, upperYellow)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
#    img, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#    img = cv2.drawContour(img, contours, -1, (0,255,0), 3)
    cv2.imshow('frame',frame)
    cv2.imshow('thresh', thresh)
#    cv2.imshow('contour', img)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
