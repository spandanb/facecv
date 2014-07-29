A collection of scripts that do a bunch of cool things, using opencv or simplecv.

The scripts require opencv, simplecv, and numpy.

simpleFaceRec.py: recognizes faces and draws squares around them.

facialAuth.py: recognizes different users and "authenticates" them
    based on the supplied username. There after only their face can be viewed.
    All other faces are censored out. Requires, there to be a set of user images against
    which to compare (use rec.py to do this).

facesq.py: draws squares around faces and eyes. Accepts images as inputs

play.py: plays a recorded file. Useful for debugging

rec.py: Takes photos to be used against classifier for facial auth system. 

utils.py: Some utility functions and classes

NOTE:

The video.py and common.py file is copied from the opencv-2.4.8 
distribution (opencv-2.4.8./samples/python2/\*.py).

The haar cascade files are copied from the opencv-2.4.8 
distribution (opencv-2.4.8./data/haarcascades).



