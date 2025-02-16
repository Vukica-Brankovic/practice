import cv2 as cv
import os

dirList = os.listdir("Videos/")
print(dirList)

def resizeFrame(frame, scale = 0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation = cv.INTER_AREA)

for file in dirList:
    cap = cv.VideoCapture(f"Videos/{file}")
    while cap.isOpened():

        flag, frame = cap.read()
        if not flag:
            print("error getting frame")
            break
        resFrame = resizeFrame(frame)
        cv.imshow("dog", resFrame)
        if cv.waitKey(30) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()
    
