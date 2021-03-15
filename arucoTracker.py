import cv2 as cv
import numpy as np

 

# Load the predefined dictionary

dictionary = cv.aruco.Dictionary_get(cv.aruco.DICT_6X6_250)

 

# Generate the marker

markerImage = np.zeros((200, 200), dtype=np.uint8)

markerImage = cv.aruco.drawMarker(dictionary, 33, 200, markerImage, 1);

cv.imwrite("marker33.png", markerImage);

#Load the dictionary that was used to generate the markers.
#dictionary = cv.aruco.Dictionary_get(cv.aruco.DICT_6X6_250)

# Initialize the detector parameters using default values
#parameters =  cv.aruco.DetectorParameters_create()

# Detect the markers in the image
#markerCorners, markerIds, rejectedCandidates = cv.aruco.detectMarkers(frame, dictionary, parameters=parameters)


