#!/usr/bin/env python

"""
Creates squares around faces and eyes in images
"""

import numpy as np
import cv2
import sys

def get_outfile(infile):
    idx = infile.rfind(".") 
    #TODO: Will fail if '.' at end of filename
    return infile[:idx] + "_out." + infile[idx+1:]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Error: Too few argument. Exiting...."
        sys.exit(1)
    
    #infer output filename
    elif len(sys.argv) == 2:
        infile = sys.argv[1]
        outfile = get_outfile(infile)
    else:
        infile = sys.argv[1]
        outfile = sys.argv[2]
    
    face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_eye.xml')
    
    img = cv2.imread(infile)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    
    cv2.imshow('img',img)
    cv2.imwrite(outfile,img)
