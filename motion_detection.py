#Collaboration between Katelyn Danger and Emmy Zero
#Created in about an hour

import cv2 as cv
import numpy as np

stream = cv.VideoCapture(-1)

if not stream.isOpened():
    print("Open CV is unable to open the camera")
    exit()

frameB = np.zeros((480, 640, 3)[:2], np.uint8)


while True:
    ret, frameA = stream.read()
    if not ret:
        print("Stream has ended")
        break

    #print(frameA.shape)
        
    
    blurA = cv.GaussianBlur(frameA, (5,5), cv.BORDER_DEFAULT)
    blurB = cv.GaussianBlur(frameB, (5,5), cv.BORDER_DEFAULT)

    #invert color
    invertB = cv.cvtColor(blurB, cv.COLOR_RGB2BGR)

    movement = cv.bitwise_or(blurA, invertB)


    cv.imshow("Motion", movement)


    ret,frameB = stream.read()
    
    if cv.waitKey(1) == ord('q'):
        break

stream.release()
cv.destroyAllWindows()
