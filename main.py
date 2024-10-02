import cv2
import numpy

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0)
detectionFrameColor = (0, 255, 0)
detectionFrameThickness = 2

while True:
  
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    if(type(faces) == numpy.ndarray):
        print("face detected")
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), detectionFrameColor, detectionFrameThickness)

    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
video.release()
cv2.destroyAllWindows()