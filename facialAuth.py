from SimpleCV import Camera, Display
import SimpleCV as scv
import sys
import numpy as np
import glob
from utils import Color2, getPath, haar_face_classifier_path
import argparse
import os.path


pass_root_dir = "passdir/" #password image file dir
quality = 400  
minMatch = 0.3 
minDist = 0.30

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("username", help="name of user to be authenticated") #positional argument
    parser.add_argument("-f", "--filepath", help="path to video file")       #optional argument
    args = parser.parse_args()

    #Directory containing the images
    passdir = pass_root_dir + "/" + args.username

    #list of face Image objects used for authentication
    pw_vect = [scv.Image(f) for f in glob.glob(passdir +"*.jpg")] 
    
    cam = None
    if args.filepath:
        if not os.path.isfile(args.filepath):
            print "Error: filepath is invalid. Exiting...."
            sys.exit(1)
        cam = scv.VirtualCamera(args.filepath, 'video')
    else:
        cam = Camera()
        
    disp = Display()
    while disp.isNotDone():
        img = cam.getImage()
        
        match = False
        
        faces = None
        for classifier in haar_face_classifier_path:
            faces = img.findHaarFeatures(classifier)
            if faces:
                break
        
        if faces:
            for face in faces: #iterate over all the faces               
                
                match = False
                
                facelayer = scv.DrawingLayer((img.width, img.height))
                template = face.crop()
                
                for password in pw_vect:
                    keypoints = password.findKeypointMatch(template,quality,minDist,minMatch)
                
                    if keypoints:
                        facebox = facelayer.rectangle(face.topLeftCorner(), (face.width(), face.height()), color=Color2.green, width=5)  #allow
                        match = True
                        break
                        
                if not match:     
                    facebox = facelayer.rectangle(face.topLeftCorner(), (face.width(), face.height()), color=Color2.red, filled=True) #block
                  
                img.addDrawingLayer(facelayer)
                img.applyLayers()
                
        img.show()
