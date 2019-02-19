# -*- coding: utf-8 -*-

"""
Created on Sat Feb  3 01:04:46 2018
@author: RD
"""

import cv2
import os

def ronak(frame):
    path=os.getcwd()
    path=path+"\label"
    a=0
    for x,y,names in os.walk(path):
        a=a+1

    max_match=0
    match_name=""
    match_ext=""
    for i in names:
       
       img_rgb = cv2.imread('./label/'+i)
       img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
       template = img_gray
       w, h = template.shape[::-1]
       res = cv2.matchTemplate(img_gray,frame,cv2.TM_CCOEFF_NORMED)
       min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

       if max_match<max_val:
           max_match=max_val
           match_name,match_ext = i.split(".")
     
    return match_name

       
img_rgb = cv2.imread('sample.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = img_gray
w, h = template.shape[::-1]


cap = cv2.VideoCapture(0)
i=0

while(1):
    
    ret, frame1 = cap.read()
    frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    
    res = cv2.matchTemplate(img_gray,frame,cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(frame1,top_left, bottom_right, 255, 2)
    
    name=ronak(frame)
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    cv2.putText(frame1,name,max_loc, font, 2,(255,255,255),2,cv2.LINE_AA)
    cv2.imshow('res.jpg',frame1)

    if cv2.waitKey(200) & 0xFF == ord('q'):
        print(name)
        break



cap.release()
cv2.destroyAllWindows()
