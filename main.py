# -*- coding: utf-8 -*-
import cv2
import numpy as np

#get video from camera
cap = cv2.VideoCapture(0)

height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_rate = int(cap.get(cv2.CAP_PROP_FPS)/3)

size = (int(width*2/3), int(height*2/3))

while True:
    ret, frame = cap.read()
    #resize and gray scale
    frame = cv2.resize(frame, dsize=size)
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    gray = cv2.GaussianBlur(gray, (33, 33), 1)

    #get circles by Hough-Gradient method
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 80, param1=10, param2=70, minRadius=1, maxRadius=80)

    #draw Pien if there are circles
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            #i[0]=x-axis i[1]=y-axis i[2]=radius
            x = i[0]; y = i[1]; r = i[2]
            #cv2.circle(img, center, radius, color, thickness)
            #cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness)

            #face
            cv2.circle(frame, (x, y), r, (0, 215, 255), -1)
            #right evebrow
            cv2.ellipse(frame, (x+int(r*2/3), y-int(r*2/3)), (int(r/3), int(r/4)), 0, 90, 165, (19, 69, 139), 3)
            #left evebrow
            cv2.ellipse(frame, (x-int(r*2/3), y-int(r*2/3)), (int(r/3), int(r/4)), 0, 15, 90, (19, 69, 139), 3)
            #right tear
            cv2.circle(frame, (x+int(r*2/5), y), int(r*3/10), (255, 255, 255), -1)
            #left tear
            cv2.circle(frame, (x-int(r*2/5), y), int(r*3/10), (255, 255, 255), -1)
            #right brown eye
            cv2.circle(frame, (x+int(r*2/5), y-int(r/15)), int(r*3/10), (0, 0, 0), -1)
            #left brown eye
            cv2.circle(frame, (x-int(r*2/5), y-int(r/15)), int(r*3/10), (0, 0, 0), -1)
            #right big white eye
            cv2.ellipse(frame, ((x+int(r/3), y-int(r/6)), (int(r/3), int(r/4)), 135), (255, 255, 255), -1)
            #left big white eye
            cv2.ellipse(frame, ((x-int(r/2), y-int(r/6)), (int(r/3), int(r/4)), 135), (255, 255, 255), -1)
            #right small white eye
            cv2.ellipse(frame, ((x+int(r/2), y), (int(r/10), int(r/15)), 135), (255, 255, 255), -1)
            #left small white eye
            cv2.ellipse(frame, ((x-int(r/3), y), (int(r/10), int(r/15)), 135), (255, 255, 255), -1)
            #mouse
            cv2.ellipse(frame, (x, y+r), (int(r/4), int(r/2)), 0, 245, 295, (19, 69, 139), 5)

    #display the video
    cv2.imshow('frame', frame)

    #press q to finish
    if cv2.waitKey(1)&0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()