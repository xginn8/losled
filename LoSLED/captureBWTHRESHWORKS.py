
# can capture in BW

import sys
import cv2
import time
import numpy
import os
 
 ##
 # Opens a video capture device with a resolution of 800x600
 # at 30 FPS.
 ##
def open_camera(cam_id = 0):
    cap = cv2.VideoCapture(cam_id)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 600);
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 800);
    cap.set(cv2.cv.CV_CAP_PROP_FPS, 30);
    return cap

##
# Gets a frame from an open video device, or returns None
# if the capture could not be made.
##
def get_frame(device):
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
def new_rgb_image(width, height):
    image = numpy.zeros( (height, width, 3), numpy.uint8)
    return image

########### Main Program ###########

if __name__ == "__main__":
# Camera ID to read video from (numbered from 0)
    camera_id = 0
    dev = open_camera(camera_id) # open the camera as a video capture device

    while True:
        img_orig = get_frame(dev) # Get a frame from the camera
        if img_orig is not None: # if we did get an image
            gray = cv2.cvtColor(img_orig, cv2.COLOR_RGB2GRAY)
            hsv = cv2.cvtColor(img_orig, cv2.COLOR_RGB2HSV)
            (thresh, im_bw) = cv2.threshold(gray, 18, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            cv2.imshow("thres", im_bw) # display the image in a window named "video"
        else: # if we failed to capture (camera disconnected?), then quit
            break
    
        if (cv2.waitKey(2) >= 0): # If the user presses any key, exit the loop
            break
        
    cleanup(camera_id) # close video device and windows before we exit

