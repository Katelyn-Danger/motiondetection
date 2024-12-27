#Emmy Zero's Version

import cv2 as cv
import numpy as np

stream = cv.VideoCapture(-1)

if not stream.isOpened():
    print("Open CV is unable to open the camera")
    exit()


_, new_frame = stream.read()
old_frame = np.zeros_like(new_frame)
dst = np.zeros_like(new_frame)

while True:
    old_frame[:] = new_frame #copy previous frame into "old_frame"
    stream.read(new_frame) #read the camera INTO "new_frame"

    dst[:] = 128
    dst[:] += new_frame//2
    dst[:] -= old_frame//2

    cv.imshow("bongo", dst)
    if cv.waitKey(1) == ord('q'):
        break
