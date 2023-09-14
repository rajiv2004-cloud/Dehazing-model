import cv2
import numpy as np

# Import the image_dehazer class from your existing code
from  image_dehazer import image_dehazer

# Initialize the dehazer
dehazer = image_dehazer(airlightEstimation_windowSze=15, boundaryConstraint_windowSze=3, C0=20, C1=300,
                        regularize_lambda=0.1, sigma=0.5, delta=0.85, showHazeTransmissionMap=False)

# Open a connection to the webcam 
cap = cv2.VideoCapture(0)

#just in case of any external webcams use 1 or -1.
#cap = cv2.VideoCapture(1)
while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        break

    # Apply the dehazing model to the frame
    dehazed_frame, _ = dehazer.remove_haze(frame)

    # Display the dehazed frame
    cv2.imshow('Dehazed Video', dehazed_frame)

    # Press 'q' to exit the loop and close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()