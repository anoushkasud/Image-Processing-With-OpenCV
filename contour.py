import cv2
import numpy as np

img = cv2.imread('media/dan.jpg')
#resize
img = cv2.resize(img,(400,400),interpolation=cv2.INTER_AREA)

#grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#blur
blur = cv2.GaussianBlur(gray,(5,5),cv2.BORDER_DEFAULT)

#edges
canny = cv2.Canny(gray,125,255)

#threshold
ret,thresh = cv2.threshold(gray,125,255,cv2.THRESH_BINARY) 
#converts image into binary if pixel value is less than 125 make it black otherwise make it white upto pixel value 255

#find contours
contours,heirarchy = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
print(len(contours))
#3 modes 
# retr_list --- gives the list of all contours
# retr_tree --- gives the contours that are in hierarchy
# retr_external -- gives the external contours

#methods
# chain_approx_none --- gives all the contour points
# chain approx_simple --- gives the poins of boundary

blank = np.zeros(img.shape,dtype='uint8')

#draw contours
cv2.drawContours(blank,contours,-1,(0,255,255),1) #-1 to draw all counters
cv2.imshow('drawn',blank)
cv2.waitKey(0)
