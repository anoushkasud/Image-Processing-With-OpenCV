import cv2
from matplotlib.pyplot import imshow
import numpy as np
img = cv2.imread('media/dan.jpg')

#resize
img = cv2.resize(img,(400,400),interpolation=cv2.INTER_AREA)

blank = np.zeros(img.shape[:2],dtype='uint8')

#split
b,g,r = cv2.split(img)
#dark = no color, light = more color
# cv2.imshow('blue',b)
# cv2.imshow('green',g)
# cv2.imshow('red',r)

#merge
merge = cv2.merge([b,g,r])
# cv2.imshow('merge',merge)

#show channels in their color not in grayscale
blue = cv2.merge([b,blank,blank])
green = cv2.merge([blank,g,blank])
red = cv2.merge([blank,blank,r])

cv2.imshow('blue',blue)
cv2.imshow('green',green)
cv2.imshow('red',red)

cv2.waitKey(0)