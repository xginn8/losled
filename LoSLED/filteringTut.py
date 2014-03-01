
# can capture in BW

import sys
import cv2
import cv
import time
import numpy
import os
 
 ##
 # Opens a video capture device with a resolution of 800x600
 # at 30 FPS.
 ##
def openCamera(camId = 0):
    cap = cv2.VideoCapture(camId)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 600);
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 800);
    cap.set(cv2.cv.CV_CAP_PROP_FPS, 30);
    return cap

##
# Gets a frame from an open video device, or returns None
# if the capture could not be made.
##
def getFrame(device):
    ret, img = device.read()
    if (ret == False): # failed to capture
        print >> sys.stderr, "Error capturing from video device."
        return None
    return img

##
# Closes all OpenCV windows and releases video capture device
# before exit.
##
def cleanup(cam_id = 0): 
    cv2.destroyAllWindows()
    cv2.VideoCapture(cam_id).release()

##
# Creates a new RGB image of the specified size, initially
# filled with black.
##
def newRGBImage(width, height):
    image = numpy.zeros( (height, width, 3), numpy.uint8)
    return image

########### Main Program ###########
def capture(hue, threshold):
    if __name__ == "__main__":
    # Camera ID to read video from (numbered from 0)
        cameraId = 0
        dev = openCamera(cameraId) # open the camera as a video capture device
    
        while True:
            imgOrig = getFrame(dev) # Get a frame from the camera
            hsv = cv2.cvtColor(imgOrig
            else: 
                break
        
            if (cv2.waitKey(2) >= 0): # If the user presses any key, exit the loop
                break
            
        cleanup(camera_id) # close video device and windows before we exit

capture(010, 220)
