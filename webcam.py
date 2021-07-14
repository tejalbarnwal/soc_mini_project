#! usr/bin/python3

import cv2

face_cascade = cv2.CascadeClassifier("haarcasde.xml")

cap = cv2.VideoCapture(0)

while cap.isOpened():
    __, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiscale(gray, scaleFactor = 1.3, minNeighbors = 3, minSize=(30,30))

    for (x,y,w,,h) in faces:
        cv.rectangle(image, (x, y), (x+w, y+h), (255,0,0), 3)

    cv2.imshow("img", img)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()

