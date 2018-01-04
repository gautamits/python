import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt
image=sys.argv[1]
image=cv2.imread(image,1)
h,w=image.shape[:2]
image=cv2.resize(image,((480*w)/h,480))
h,w=image.shape[:2]
rows=3
columns=3
rowsize=h/rows
columnsize=w/columns

blank=np.array([[np.array([255,255,255]) for j in xrange(w+2)] for i in xrange(h+2)])
#blank=np.zeros((h+2,w+2,3),np.uint8)
for i in xrange(rows):
	for j in xrange(columns):
		print i*rowsize,":",(i+1)*rowsize,":",j*columnsize,":",(j+1)*columnsize
		blank[i+i*rowsize:i+(i+1)*rowsize,j+j*columnsize:j+(j+1)*columnsize] = image[i*rowsize:(i+1)*rowsize,j*columnsize:(j+1)*columnsize]
		#cv2.imshow("image"+str(i)+str(j),image[i*rowsize:(i+1)*rowsize,j*columnsize:(j+1)*columnsize])
plt.plot(blank)
plt.show()
cv2.imshow("blank",blank)
cv2.waitKey(0)
