
import cv2
import numpy as np

def backgroundSubtract():
    cap = openWebcamFeed() 
    fgbg = cv2.createBackgroundSubtractorMOG()
    while(1):
        ret, frame = cap.read()
        fgmask = fgbg.apply(frame)
        cv2.imshow('frame',fgmask)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


def openWebcamFeed():
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)
    if(vc.isOpened()): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False
    while rval:
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if(key == 27): # exit on ESC
            break
    cv2.destroyWindow("preview")

backgroundSubtract()
