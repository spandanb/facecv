"""
Initialization for facial auth system
"""


#Save 10 photos as a sample
def saveSample(n=10):
    #TODO: Allow user to specify where to save photos
    for i in range(n):
        image = cam.getImage() 
        faces = image.findHaarFeatures(faceHaarFile)
        faces.draw()
        face = faces[-1]
        password = face.crop().save("passdir/tmp/password"+str(i)+".jpg")
        raw_input("Continue?")


if __name__ == "__main__":

    saveSample()

