import cv2
import numpy

eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0)
detectionFrameColor = (0, 255, 0)
detectionFrameThickness = 2
detectionStrength = 1.1

detectionTextColor = (0, 255, 0)
detectionTextThickness = 2
detectionTextSize = 1


def showDetected(detectedObject, showText):
    for (x, y, w, h) in detectedObject:
            cv2.rectangle(frame, (x, y), (x + w, y + h), detectionFrameColor, detectionFrameThickness)
            cv2.putText(frame, showText, (x, y + (-10)), cv2.FONT_HERSHEY_SIMPLEX, detectionTextSize, detectionTextColor, detectionTextThickness)

while True:
  
    ret, frame = video.read()
    
    if(not ret):
        print("Failed to connect to camera. Exiting ...")
        
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, scaleFactor=detectionStrength, minNeighbors=5)

    if(type(face) == numpy.ndarray):
        # print("face detected")
        showDetected(face, "Face Detected")

    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
video.release()
cv2.destroyAllWindows()