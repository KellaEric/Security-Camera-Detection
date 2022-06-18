import cv2
import winsound

#preparing the image capture
cam = cv2.VideoCapture(0)
# checking whether the camera is on or off e
while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv2.absdiff(frame1,frame2)
#conversions of different color scalese
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5 , 5), 0)
    _, thresh = cv2.threshold(blur, 20, 555, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    #checking contours for detecting larger objectes on the captured on the camera frame.
  
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (255, 255, 23), 2)
        winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
    if cv2.waitKey(10) == ord('e'):
        break
    #camera title.
    cv2.imshow('Main Cam', frame1)
   # print("detect",frame1)
    cv2.imshow('Criminals',blur)
    cv2.imshow('difference',diff)
    
