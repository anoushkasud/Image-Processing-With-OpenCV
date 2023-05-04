import cv2
import numpy as np

img = cv2.imread('media/dan.jpg')
img = cv2.resize(img,(400,400),interpolation=cv2.INTER_AREA) 

blank = np.zeros((400,400),'uint8')

masked = cv2.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),150,255,-1)
#both mask and img should be of same size

image = cv2.bitwise_and(img,img,mask = masked)
cv2.imshow('image',image)
cv2.waitKey(0)