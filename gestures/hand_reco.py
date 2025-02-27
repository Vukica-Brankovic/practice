import cv2 as cv
import numpy as np
import os

haar = cv.CascadeClassifier("haar_class.xml")
features = np.load("gestures.npy", allow_pickle = True)
labels = np.load("labels.npy", allow_pickle = True)
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read("saved_model.yml")

hands = []
DIR = r'/media/vukica/My Adata/Vukica 2024/February 21 Archive - ASUS/VS Code Files/hands'
for gesture in os.listdir(DIR):
    hands.append(gesture)


img = cv.imread("Images/eval4.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
found = haar.detectMultiScale(gray, 1.1, 4)
for (x,y,w,h) in found:
    crop = gray[y:y+h, x:x+w]
    label, confidence = recognizer.predict(crop)
    print(hands[label], confidence)
    cv.putText(img, str(hands[label]), (50, 50), cv.FONT_HERSHEY_COMPLEX, 2.0, (255, 0, 0), 2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 1)

smaller_frame = cv.resize(img, (640,480))
cv.imshow("eval", smaller_frame)
cv.waitKey(0)            

