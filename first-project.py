import cv2
import numpy as np

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

color = 'original'

while True:
    ret, frame = cam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    k = cv2.waitKey(1) 

    hsv =  cv2.cvtColor(frame,  cv2.COLOR_BGR2HSV)

    lower_green =  np.array([45 , 100 , 100 ]) 
    upper_green =  np.array([100, 255 , 255 ]) 

    res =  cv2.bitwise_and(frame, frame,  mask = cv2.inRange(hsv,  lower_green,  upper_green)) 

    if color == 'original':
      cv2.imshow("test", frame)
    elif color == 'gray':
      cv2.imshow("test", gray)
    elif color == 'green_spectrum':
      cv2.imshow("test", res)
    
    if k%256 == 27:
        # ESC
        break
    elif k%256 == 32:
        # SPACE
        img_name = "img_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        img_counter += 1
    elif k%256 == 49:
        # 1
        color = 'gray'
        cv2.waitKey(1)
    elif k%256 == 50:
        # 2
        color = 'green_spectrum'
        cv2.waitKey(1)
    elif k%256 == 51:
        # 3
        color = 'original'
        cv2.waitKey(1)


cam.release()

cv2.destroyAllWindows()