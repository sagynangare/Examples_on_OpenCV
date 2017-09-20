import cv2
import numpy as np

img =cv2.imread('watch.jpg',cv2.IMREAD_COLOR)
cv2.line(img, (0,0),(150,150),(255,0,0),12)
cv2.rectangle(img, (15,25), (100,100),(0,255,0),5)
cv2.circle(img, (100,56),55,(0,0,255),-1)

#Polygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
cv2.polylines(img,[pts],True,(0,255,255),5)

font =cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(0,255,255),2,cv2.CV_AA)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
