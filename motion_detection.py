import cv2 as cv
import numpy as np

stream = cv.VideoCapture(-1)

if not stream.isOpened():
    print("Open CV is unable to open the camera")
    exit()

ret, ima = stream.read()
ret, imb = stream.read()
ret, dst = stream.read()

while True:
    retval, inframe = stream.read()
    ima[:] = imb
    imb[:] = inframe
    dst[:] = 128 + imb//2 - ima//2
    cv.imshow("out",dst)

    if cv.waitKey(1) == ord('q'):
        break


stream.release()
cv.destroyAllWindows()
