#importing libraries
import cv2 

#read images
# img = cv2.imread('media/dan.jpg')
# cv2.imshow('frame',img)
# cv2.waitKey(0)

#read videos
cap = cv2.VideoCapture('media/road.mp4')
while True:
    get_frame,frame = cap.read()
    cv2.imshow('video',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


    