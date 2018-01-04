#!/usr/bin/python
# USAGE
# python click_and_crop.py --image jurassic_park_kitchen.jpg

# import the necessary packages
import argparse
import cv2
import sys
import os

# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not

refPt = []
cropping = False
ix=0
iy=0
def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global refPt, cropping,ix,iy

	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
		#refPt = [(x, y)]
		ix,iy=x,y
		cropping = True

	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		#refPt.append((x, y))
		cropping = False
		refPt.append((min(ix,x),min(iy,y)))
		refPt.append((max(ix,x),max(iy,y)))
		# draw a rectangle around the region of interest
		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
		

# load the image, clone it, and setup the mouse callback function
f=os.environ.get('NAUTILUS_SCRIPT_SELECTED_FILE_PATHS')
f=f.split()
for path in f:
	image = cv2.imread(path,1)
	h,w,c=image.shape

	original=h/float(w)

	print h,w,c
	ratio=768.0/h
	image=cv2.resize(image,(int(w*ratio),int(h*ratio)))
	clone = image.copy()
	cv2.namedWindow("image",flags=cv2.WINDOW_NORMAL)
	#cv2.namedWindow("image")
	#cv2.setMouseCallback("image", click_and_crop)
	cv2.setMouseCallback("image", click_and_crop)

	# keep looping until the 'q' key is pressed
	while True:
		# display the image and wait for a keypress
		cv2.imshow("image", image)
		key = cv2.waitKey(1) & 0xFF

		# if the 'r' key is pressed, reset the cropping region
		if key == ord("r"):
			ix=0
			iy=0
			refPt=[]
			cropping=False
			image = clone.copy()

		# if the 'c' key is pressed, break from the loop
		elif key == ord('q'):
			exit(0)
		elif key == ord("c"):
			cv2.destroyAllWindows()
			break

	# if there are two reference points, then crop the region of interest
	# from teh image and display it
	if len(refPt) == 2:
		roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
	cv2.imwrite(path,roi)
	cv2.waitKey(0)



