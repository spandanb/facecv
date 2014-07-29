


haar_face_classifier = ["haarcascade_frontalface_default.xml",      \
                        "haarcascade_frontalface_alt.xml",          \
                        "haarcascade_frontalface_alt2.xml",         \
                        "haarcascade_profileface.xml"]    

getPath = lambda filename: "./haarcascades/" + filename

haar_face_classifier_path = map(getPath, haar_face_classifier)

class Color:
    """
    class representing different colors in opencv
    """
    green = (0,255,0)  
    red   = (0,0,255) 
    blue  = (255,0,0)
   
class Color2:
    """
    class representing different colors in simplecv
    """
    green = (0,255,0)  
    blue  = (0,0,255) 
    red   = (255,0,0)

def get_face_classifier():
    """
    Returns a vector of haar face classifiers
    """
    face_classifier_vect =  [cv2.CascadeClassifier(getPath(classifier)) for classifier in haar_face_classifier]
    return face_classifier_vect


