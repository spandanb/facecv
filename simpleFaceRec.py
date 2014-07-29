import cv2
import cv2.cv as cv
import numpy as np
import sys
import video
import os.path
#Creates squares around faces
from utils import get_face_classifier, Color

if __name__ == '__main__':
    
    cam = None
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        if not os.path.isfile(filepath):
            print "Error: {} file does not exist. Exiting....".format(filename)
            sys.exit(1)
        cam = cv2.VideoCapture(filepath) #Read file
    else:        
        cam = video.create_capture()     #Read camera
    
    face_cascade_vect = get_face_classifier()
    found = False   #if one of the haar cascades found a face  
    while True:
        
        ret, img = cam.read() #img is numpy 3-array
        try:
            invimg = np.fliplr(img) #inverted 
        except ValueError:
            print "ValueError; continuing...."
            continue
            
        found = False
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        for face_cascade in face_cascade_vect:
            if found: break
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                #cv2.rectangle(img, (x,y), (x+w,y+h), Color.red, cv.CV_FILLED) #Alternative face highlighting 
                cv2.rectangle(img, (x,y), (x+w,y+h), Color.green, 2)           
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                found = True            
        
        #Poll and check if user wants to exit
        cv2.imshow('img', img )        
        key = cv.WaitKey(10)
        if key == 27:
            break
        elif key == ord('x'): 
            pass
    print "Cleaning up...."
    cv.DestroyAllWindows()
