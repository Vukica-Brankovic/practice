import cv2 as cv

cap = cv.VideoCapture("Videos/dog2.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    canny = cv.Canny(gray, 100, 200)
    contours, hierarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    draw = cv.drawContours(frame, contours, -1, (0, 255, 0), 1)
    cv.imshow("video", frame)
    if cv.waitKey(40) == ord("q"):
        cv.destroyAllWindows()
        break
    if not ret:
        cv.destroyAllWindows()
        break
cap.release()    
