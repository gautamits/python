import matplotlib.pyplot as plt
import cv2
import numpy as np
import os
path="/home/amit/Desktop/abhishek"
emotions={}
emotions[0]="angry"
emotions[1]="disgust"
emotions[2]="fear"
emotions[3]="happy"
emotions[4]="sad"
emotions[5]="surprise"
emotions[6]="neutral"
k=1
for i in os.listdir(path):
  image=path+'/'+i
  vec=cv2.imread(image,1)
  vec=cv2.resize(vec,(40,40))
  plt.subplot(5,5,k)
  plt.axis("off")
  plt.imshow(cv2.cvtColor(vec, cv2.COLOR_BGR2RGB))
  plt.title(i)
  k+=1
plt.show()
