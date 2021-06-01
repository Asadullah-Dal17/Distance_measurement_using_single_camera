import cv2 as cv
import time

CONFIDENCE_THRESHOLD = 0.5
NMS_THRESHOLD = 0.5
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

class_names = []
with open("classes.txt", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]


camera = cv.VideoCapture(0)

while True:
    ret, frame = camera.read()
    cv.imshow('frame', frame)

    key = cv.waitKey()
    if key == ord('q'):
        break
cv.destroyAllWindows()
