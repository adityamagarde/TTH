# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 23:28:28 2018

@author: ADITYA
"""

import cv2
import numpy as np
from floorCleanlinessIndex import findSize
from keras.models import load_model
from keras.preprocessing import image

#Loading the saved classifier
classifier = load_model('floorCleanlinessModel.h5')
classifier.compile(optimizer="adam", loss="binary_crossentropy", metrics=['accuracy'])


#Feed from the surveillance camera
videoCapture = cv2.VideoCapture(0)


#Function for continuous monitoring of the floor
while(True):
    
    ret, frame = videoCapture.read()
    cv2.imwrite('FloorImage.png', frame)
    
    picturePath = r"FloorImage.png"
    height, width = findSize(picturePath)
    
    test_image= image.load_img(picturePath, target_size = (width, height)) 
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    test_image = test_image.reshape(width, height)
    result = classifier.predict(test_image)  
    
    if(result == 0.5):
        print('The floor is dirty')
    else:
        print('The floor is clean')