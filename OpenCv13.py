import numpy as np
import cv2

cap = cv2.VideoCapture('opencv-python-foreground.mp4')
fgbg = cv2.BackgroundSubtractorMOG()

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow('original',frame)
    cv2.imshow('fg',fgmask)

    k=cv2.waitKey(30) & 0xFF
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()
