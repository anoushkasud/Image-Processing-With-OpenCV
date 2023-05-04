import cv2
img = cv2.imread('media/dan.jpg')
img = cv2.resize(img,(400,400),interpolation=cv2.INTER_AREA)
cv2.imshow('img',img)

#averaging
average = cv2.blur(img,(3,3))
cv2.imshow('average',average)

#gaussian blur
gauss = cv2.GaussianBlur(img,(3,3),0)
cv2.imshow('guass',gauss)

#median
median = cv2.medianBlur(img,3,0)
cv2.imshow('median',median)

#bilateral blur
bilateral = cv2.bilateralFilter(img,5,10,10)
cv2.imshow('bilateral',bilateral)

cv2.waitKey(0)