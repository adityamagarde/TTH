# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 16:49:40 2018

@author: ADITYA
"""

#FLOOR CLEANLINESS INDEX PROBLEM

#Way 1: Using a normal CNN

import cv2
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator


#Example
    #tempImagePath = r"images/temp.jpg"

def findSize(tempImagePath):
    tempImage = cv2.imread(tempImagePath)
    height = np.size(tempImage,0)
    width = np.size(tempImage, 1)
    return height, width

tempImagePath = r"images/1.jpg"
height, width = findSize(tempImagePath)

def imgDataGen(model, height, width):
    train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
    test_datagen = ImageDataGenerator(rescale=1./255)
    
    trainingSet = train_datagen.flow_from_directory('data/train', target_size=(height, width), batch_size=32, class_mode='binary')
    testSet = test_datagen.flow_from_directory('data/validation', target_size=(height, width), batch_size=32, class_mode='binary')
    
    return trainingSet, testSet

def convNetCreater(height, width):
    classifier = Sequential()
    classifier.add(Convolution2D(32, (3, 3), input_shape=(height, width, 3), activation='relu'))      #ConvolutionLayer
    classifier.add(MaxPooling2D(pool_size=(2, 2)))
    classifier.add(Convolution2D(64, (3, 3), activation='relu'))
    classifier.add(MaxPooling2D(pool_size=(2, 2)))
    classifier.add(Flatten())
    classifier.add(Dense(units=1024, activation='relu'))
    classifier.add(Dense(units=256, activation='relu'))
    classifier.add(Dense(units=64, activation='relu'))
    classifier.add(Dense(units=1, activation='sigmoid'))
    
    classifier.compile(optimizer="adam", loss="binary_crossentropy", metrics=['accuracy'])
    
    return classifier
 
#Creating and training the classifier
classifier = convNetCreater(height, width)
trainingSet, testSet = imgDataGen(classifier, height, width)
classifier.fit_generator(trainingSet, steps_per_epoch=2000, epochs=75, validation_data=testSet, validation_steps=800)


#Saving the model
classifier.save('floorCleanlinessModel.h5')


    