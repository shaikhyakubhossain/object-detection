import cv2
import numpy
from utils.helper import showDetectedObject

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0)

detectionFrameColor = (0, 255, 0)
detectionFrameThickness = 1
detectionStrength = 1.1

detectionTextColor = (0, 255, 0)
detectionTextThickness = 1
detectionTextSize = 0.5

while True:
  
    ret, frame = video.read()
    
    if(not ret):
        print("Failed to connect to camera. Exiting ...")
        
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, scaleFactor=detectionStrength, minNeighbors=5)

    if(type(face) == numpy.ndarray):
        # print("face detected")
        showDetectedObject(cv2, face, "Face Detected", frame, detectionFrameColor, detectionFrameThickness, detectionTextColor, detectionTextThickness, detectionTextSize)

    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
video.release()
cv2.destroyAllWindows()