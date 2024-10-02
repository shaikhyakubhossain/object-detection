def showDetectedObject(cv2, detectedObject, showText, localFrame, localDetectionFrameColor = (0, 255, 0), localDetectionFrameThickness = 2, localDetectionTextColor = (0, 255, 0), localDetectionTextThickness = 2, localDetectionTextSize = 1):
    for (x, y, w, h) in detectedObject:
            cv2.rectangle(localFrame, (x, y), (x + w, y + h), localDetectionFrameColor, localDetectionFrameThickness)
            cv2.putText(localFrame, showText, (x, y + (-10)), cv2.FONT_HERSHEY_SIMPLEX, localDetectionTextSize, localDetectionTextColor, localDetectionTextThickness)