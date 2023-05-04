import cv2
import numpy as np

blank = np.zeros((400,400),dtype = 'uint8')

rec = cv2.rectangle(blank.copy(),(70,70),(330,330),255,-1)
cir = cv2.circle(blank.copy(),(200,200),170,255,-1)

cv2.imshow('rec',rec)
cv2.imshow('cir',cir)

#bitwise and
b_and = cv2.bitwise_and(rec,cir)
# cv2.imshow('b_and',b_and)

#bitwise or
b_or = cv2.bitwise_or(rec,cir)
# cv2.imshow('b_or',b_or)

#bitwise xor
b_xor = cv2.bitwise_xor(rec,cir)
# cv2.imshow('b_xor',b_xor)

#bitwise not
b_not = cv2.bitwise_not(rec)
# cv2.imshow('b_not',b_not)

c_b_not = cv2.bitwise_not(cir)
cv2.imshow('c_b_not',c_b_not)

cv2.waitKey(0)