import cv2
import numpy as np

img = cv2.imread('media/dan.jpg')
#resize
img = cv2.resize(img,(400,400),interpolation=cv2.INTER_AREA) 
#inter_area to shrink, inter_linear,inter_cubic to enlarge

#tanslate (move up,down,right,left)

def translate(img,x,y):
    dimensions = (img.shape[1],img.shape[0])
    transMat = np.float32([[1,0,x],[0,1,y]])
    return cv2.warpAffine(img,transMat,dimensions)

# +x = right, -x = left, +y = down, -y = up
translated = translate(img,100,100) #right and down
#cv2.imshow('translated',translated)

#rotation
def rotate(img, angle, rotPoint = None):
    (height,width) = img.shape[:2]
    if(rotPoint == None):
        rotPoint = (width//2,height//2)
    rotMat = cv2.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)
    return cv2.warpAffine(img,rotMat,dimensions)

#-angle clockwise, +angle anti-clockwise
rotated = rotate(img,45) #rotate 45 degree anticlockwise
#cv2.imshow('rotated',rotated)

#flip
flip = cv2.flip(img,0) #use 0 to flip verticlly, 1 to flip horizontally, -1 to flip both ways
#cv2.imshow('flip',flip)

#crop
cropped = img[200:300,200:400]
cv2.imshow('cropped', cropped)

cv2.waitKey(0)
