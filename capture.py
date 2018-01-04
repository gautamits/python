import cv2
import os
import sys
import numpy as np
counter = 0
print "enter subject name"
name=raw_input()
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
os.mkdir(name)
os.chdir(name)
camera=cv2.VideoCapture(0)
while counter < 200:
	ret,frame=camera.read()
	r,c=frame.shape[:2]
	gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(frame,1.8,2)
	if len(faces)==0:
		
		frame=np.rot90(frame)
		faces = faceCascade.detectMultiScale(frame,1.8,2)
		if len(faces)==0:
			frame=np.rot90(frame)
			faces = faceCascade.detectMultiScale(frame,1.8,2)
			if len(faces)==0:
				frame=np.rot90(frame)
				faces = faceCascade.detectMultiScale(frame,1.8,2)
				#os.remove(images)
	cv2.imshow("result",frame)

	for(x,y,w,h) in faces:
		x1=x+w
	        y1=y+h
		result = frame[y:y+h,x:x+w]
		#result=cv2.resize(result,(240,240))
		#csv.write(images+';'+str(index)+'\n')
		#data.append(result)
		#labels.append(index)
		cv2.imwrite(str(counter)+".jpg",result);
		counter+=1
cv2.waitKey(0)

	
	
