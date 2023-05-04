#importing libraries
import cv2

#reading image
# img = cv2.imread('media/dan.jpg')
# def rescale(frame,scale = 0.5):
#     height = int(frame.shape[0] * scale)
#     width = int(frame.shape[1] * scale)
#     dimensions = (width,height)
#     return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)
# resized = rescale(img)

# cv2.imshow('image',resized)
# cv2.waitKey(0)

#for recorded videos
 #cap = cv2.VideoCapture('media/road.mp4')

def rescale(frame, scale = 0.5):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width,height)
    return cv2.resize(frame, dimensions,interpolation= cv2.INTER_AREA)
    
#for live videos only
capture = cv2.VideoCapture(0)

def change_res(width,height):
    capture.set(3,width)
    capture.set(4,height)

while True:
    get_frame,frame = capture.read()

    #recorded
    #resized = rescale(frame)

    #live videos only
    resized = change_res()

    cv2.imshow('video',resized)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
