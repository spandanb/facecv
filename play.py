import cv2
import cv2.cv as cv
import numpy as np
import sys
import video


if __name__ == "__main__":
    if len(sys.argv != 2):
        print "Error: Invalid number of arguments. Exiting...."
        sys.exit(1)
    
    filename = sys.argv[1]
    vid = cv2.VideoCapture(filename)

    while True:
    
        ret, img = vid.read()
        cv2.imshow('img', img )
    
        key = cv.WaitKey(10)
        if key == 27:
            break
        elif key == ord('x'): 
            pass
    
    cv2.destroyAllWindows()
    video.release()
