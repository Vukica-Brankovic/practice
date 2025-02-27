import cv2 as cv
import numpy as np

cap = cv.VideoCapture("Videos/dog2.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        cv.destroyAllWindows()
        break

    blank = np.zeros((frame.shape[0], frame.shape[1]), "uint8")
    circle = cv.circle(blank.copy(), (blank.shape[1] // 2 - 80, blank.shape[0] // 2 - 12), 150, 255, -1)

    mask = cv.bitwise_and(frame, frame, mask=circle)

    
    cv.imshow("image", mask)

    if cv.waitKey(40) == ord("q"):
        cv.destroyAllWindows()
        break

cap.release()    
