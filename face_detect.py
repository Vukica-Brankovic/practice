import cv2 as cv

cap = cv.VideoCapture("Videos/people.mp4")
while cap.isOpened():
    flag, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    if not flag:
        cv.destroyAllWindows()
        break
    haar = cv.CascadeClassifier("haar_class.xml")
    faces = haar.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=9)
    print("Faces detected:", len(faces))
    for (x,y,w,h) in faces:
        cv.rectangle(frame, (x,y), (x+w, y+h), (56,255,8), 3)
    smaller_frame = cv.resize(frame, (640,480))
    cv.imshow("video", smaller_frame)
    if cv.waitKey(20) == ord('q'):
        cv.destroyAllWindows()
        break
cap.release()
