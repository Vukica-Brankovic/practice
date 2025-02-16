import cv2 as cv

cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)

width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
print(width, height)
while cap.isOpened():
    flag, frame = cap.read()
    if not flag:
        print("error fetching frame")
        break
    
    cv.imshow("feed", frame)
    if cv.waitKey(20) == ord('q'):
        print("exiting...")
        break
cap.release()
cv.destroyAllWindows()    
