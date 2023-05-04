##importing libraries
import cv2
import numpy as np
from numpy.lib.index_tricks import fill_diagonal

##read a blank image
blank = np.zeros((400,500,3), dtype = 'uint8')

#show blank image
cv2.imshow('blank',blank)

#color half of image red
blank[0:400,0:250] = (0,0,255)
cv2.imshow('red',blank)

#color the centre of image green
blank[150:250,200:300] = 0,255,0
#cv2.imshow('green',blank)

#draw a line
cv2.line(blank,(0,0),(500,400),(255,255,255),thickness=2)
cv2.imshow('line',blank)

#draw a rectangle
cv2.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,0),thickness=cv2.FILLED)
cv2.imshow('rectangle',blank)

#draw a circle
cv2.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),60,(0,255,255),thickness=-1)
cv2.imshow('circle',blank)

# put text
cv2.putText(blank,'dandalion',(0,200),fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,fontScale=4,color = (255,0,255),thickness=5)
cv2.imshow('text',blank)

cv2.waitKey(0)
