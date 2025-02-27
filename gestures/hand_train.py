import os
import cv2 as cv
import numpy as np

hands = []
DIR = r'/media/vukica/My Adata/Vukica 2024/February 21 Archive - ASUS/VS Code Files/hands'
for gesture in os.listdir(DIR):
    hands.append(gesture)
  

gestures = []
labels = []

def hand_train():

    for gesture in hands:
        path = os.path.join(DIR, gesture)     
        label = hands.index(gesture)
        for hand in os.listdir(path):
            image_path = os.path.join(path, hand)            
            img = cv.imread(image_path)
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            haar = cv.CascadeClassifier("haar_class.xml")
            faces = haar.detectMultiScale(gray, 1.1, 1)
            
            for (x,y,w,h) in faces:
                tiny = gray[y:y+h, x:x+w]
                gestures.append(tiny)
                labels.append(label)



    print(labels)             
            

hand_train()

gestures = np.array(gestures, dtype="object")
labels = np.array(labels)      
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.train(gestures, labels)
recognizer.save("saved_model.yml")
np.save("gestures.npy", gestures)
np.save("labels.npy", labels)
