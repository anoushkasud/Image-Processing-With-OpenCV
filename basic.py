#importing libraries
import cv2

#read image
img = cv2.imread('media/dan.jpg')

#resize
frame = cv2.resize(img,(400,400),interpolation=cv2.INTER_AREA)
cv2.imshow('org',frame)

#grayscale
gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray',gray)

#blur
blur = cv2.GaussianBlur(frame,(3,3),cv2.BORDER_DEFAULT)
# cv2.imshow('blur',blur)

#edge cascade
edge = cv2.Canny(blur,120,170)
# cv2.imshow('edge',edge)         #higher the threshold is lesser the noise is

#dilate
dilated = cv2.dilate(edge,(5,5),iterations=3) 
#with increase in number of iterations dilation(thickness of edge increased)
# cv2.imshow('dil',dilated)

#erode
eroded = cv2.erode(dilated,(5,5),iterations=3)
# cv2.imshow('erode',eroded)

#crop 
cropped = frame[100:200,150:300]
cv2.imshow('Crop',cropped)

cv2.waitKey(0)