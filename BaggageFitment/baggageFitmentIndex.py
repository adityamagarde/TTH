# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 19:17:43 2018

@author: ADITYA
"""

#BAGGAGE FITMENT INDEX:

import cv2
import serial
import numpy as np

#as soon as the bag crosses IR
arduinoData = serial.Serial('com29', 9600)      #Here com29 is the port and 9600 is the baud rate

while(1 == 1):
    myData = (arduinoData.readline().strip())
    detectString = myData.decode('utf-8')
    
    if(detectString == 'Motion Detected'):
        capFront = cv2.VideoCapture(0)
        capSide = cv2.VideoCapture(1)
        
        _, imageFront = capFront.read()
        _, imageSide = capSide.read()
        
        cv2.imwrite('FrontView.png', imageFront)
        cv2.imwrite('SideView.png', imageSide)
        
        del(capFront)
        del(capSide)
        
    
    #Since we know the distance between camera and the bagagge(It will be premeasured), 
    #we can decide the scale i.e. for example if 5px = 1cm, then we can calculate the length,
    #breadth and height of the bag
    
    # We then use SSD(Single shot multibox detection) algorithm in order to draw bounding box around the baggages.
    # We obtain the boundaries and then find the length and breadth of the boundaries and use our relation (5px = 1cm, say)
    # in order to obtain the length, breadth and height of the baggage.
    
    