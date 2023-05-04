import cv2
import matplotlib.pyplot as plt
img = cv2.imread('media/dan.jpg')

#resize
img = cv2.resize(img,(400,400),interpolation=cv2.INTER_AREA) 

#grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray',gray)

#hsv
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# cv2.imshow('HSV',hsv)

#LAB
lab = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
# cv2.imshow('LAB',lab)

#RGB
rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# cv2.imshow('rgb',rgb)

#hsv to bgr
hsv_bgr = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
# cv2.imshow('hsv_bgr',hsv_bgr)

#lab to bgr
lab_bgr = cv2.cvtColor(lab,cv2.COLOR_LAB2BGR)
# cv2.imshow('lab_bgr',lab_bgr)

# plt.imshow(rgb)
# plt.show()
cv2.waitKey(0)