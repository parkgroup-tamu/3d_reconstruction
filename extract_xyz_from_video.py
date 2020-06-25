# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:26:01 2019

@author: WSK
@input: A mp4 video file is required.
@output: 1. A csv file which includes x,y,z coordinates and frame number from LED(color) detected frame
"""

import numpy as np
import time
import math
import cv2

path = 'FILE PATH'
cap = cv2.VideoCapture(path + 'INPUT FILE NAME.mp4')

time.sleep(2.0)


def nothing(x):
    #any operation
    pass

cv2.namedWindow("Trackbars")
cv2.createTrackbar("L-B","Trackbars", 120, 255, nothing) #90
cv2.createTrackbar("L-G","Trackbars", 120, 255, nothing) #90
cv2.createTrackbar("L-R","Trackbars", 90, 255, nothing) #150
cv2.createTrackbar("U-B","Trackbars", 255, 255, nothing)
cv2.createTrackbar("U-G","Trackbars", 255, 255, nothing)
cv2.createTrackbar("U-R","Trackbars", 255, 255, nothing)

font = cv2.FONT_HERSHEY_COMPLEX
bboxes = []
areas = []
frm_num = 0
frm = []
x_list = []
y_list = []
centroid_list=[]
centroid_list.append([0,0,0,0,0])

while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    l_b = cv2.getTrackbarPos("L-B", "Trackbars")
    l_g = cv2.getTrackbarPos("L-G", "Trackbars")
    l_r = cv2.getTrackbarPos("L-R", "Trackbars")
    u_b = cv2.getTrackbarPos("U-B", "Trackbars")
    u_g = cv2.getTrackbarPos("U-G", "Trackbars")
    u_r = cv2.getTrackbarPos("U-R", "Trackbars")
    
    lower = np.array([l_b,l_g,l_r])
    upper = np.array([u_b,u_g,u_r])
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(hsv, lower, upper)
    output = cv2.bitwise_and(frame, frame, mask = mask)
    
    cnts, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    idx = 0
    
    # initialize an array of input centroids for the current frame
    for cnt in cnts:
        area = cv2.contourArea(cnt)

        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]
        
        if 25 < area :
            cv2.drawContours(frame, [approx], 0, (255,255,255), 1)
            rect = cv2.boundingRect(cnt)
            p1 = (int(rect[0]), int(rect[1]))
            p2 = (int(rect[0] + rect[2]), int(rect[1] + rect[3]))
            cv2.rectangle(frame, p1,p2, (255,0,0), 2, 1)
            
            rotatedRect = cv2.minAreaRect(cnt)
            vertices = cv2.boxPoints(rotatedRect)
            vertices = np.int0(vertices)
            centroidX = math.ceil((vertices[0][0]+vertices[1][0]+vertices[2][0]+vertices[3][0])/4)
            centroidY = math.ceil(
                    (vertices[0][1]+vertices[1][1]+vertices[2][1]+vertices[3][1])/4)
            
            cv2.drawContours(frame,[vertices],0,(0,0,255),1)
            cv2.circle(frame,(centroidX,centroidY), 3, (0,255,0), -1)
            
            bboxes.append(rect)
            areas.append(area)
            idx = idx + 1    
            text = "ID {}".format(area);
            cv2.putText(frame,text,(x,y), font, 1, (255,255,255))
            centroid_list.append([frm_num, centroidX, centroidY, area, 0])

    cv2.imshow('frame', np.hstack([frame, output]))
    frm.append(frm_num)
    frm_num = frm_num + 1
        
    if cv2.waitKey(1) == ord('p'):
        cv2.waitKey(-1)
	
    if cv2.waitKey(10) == ord('q'):
        break

centroid_list[0]=['f','x','y','a','FrmNum']
centroid_list[1][4] = frm_num

cap.release()
cv2.destroyAllWindows()

np.savetxt(path + "OUTPUT FILE NAME.csv", centroid_list,delimiter=",", fmt='%s')

