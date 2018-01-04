import PIL
from PIL import Image, ImageTk
import numpy as np
import easygui
import sys
import os
from shutil import copyfile
index=0
path=easygui.diropenbox("select the folder you want to choose images from")
saved=easygui.enterbox("name of folder where images will be saved")
try:
	saved="/home/amit/"+saved
	os.mkdir(saved)
except:
    easygui.msgbox("insufficient storage in home or user not allowed to create folder")
files = os.listdir(path)
files=sorted(files)
filez = [path+"/"+i for i in files]
for i,j in zip(files,filez):
	print i
	parent=i.split("_")[0]
	try:
		os.mkdir(saved+"/"+parent)
		copyfile(j,saved+"/"+parent+"/"+i)
	except:
		copyfile(j,saved+"/"+parent+"/"+i)
