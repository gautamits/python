import numpy as np
import cv2
import matplotlib.pyplot as plt

i = cv2.imread("testing.jpg" , 0) 
#thresh , im_bw = cv2.threshold( i , 128, 255 , cv2.THRESH_BINARY | cv2.THRESH_OTSU )
ret , thresh = cv2.threshold( i, 128 , 255 , 0 )
contours = cv2.findContours ( thresh , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
k = cv2.findContours ( thresh , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE )
cv2.drawContours( i , k[1] , 0 , ( 64,64,255 ) , -1 )
cv2.imshow("result",i)
cv2.waitKey(0)