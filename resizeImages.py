import cv2 as cv

def resizeFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_CUBIC)

img = cv.imread("Images/cat1.jpg")
print(img.shape[1])
cv.imshow("Cat", img)
resizedImg = resizeFrame(img)
cv.imshow("Resized", resizedImg)
print(resizedImg.shape[1])
print(resizedImg.shape[0])
key = cv.waitKey(0)
if key == 27:
    cv.destroyAllWindows()
