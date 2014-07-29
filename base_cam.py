import cv2.cv as cv
import cv2
import numpy as np
import sys
import video


if __name__ == '__main__':
    cam = video.create_capture()
    #cam = cv2.VideoCapture(1)
    ret, img = cam.read()
    while True:
        
        ret, img = cam.read() #img is numpy 3-array
        invimg = np.fliplr(img) #inverted 
        
        cv2.imshow('img', img )
        
        key = cv.WaitKey(10)
        if key == 27:
            break
        elif key == ord('x'): 
            pass
    
    cv.DestroyAllWindows()
