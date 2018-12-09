#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 10:59:39 2018

@author: philip
"""


import numpy as np
#from roundGrade import *

def computeFinalGrades(grades):
    
    GradingMatrix = grades #Stating a zero vector  
    #Input, M x N - matrix
    ##Plugging inputs into the zero vector .FinalGrades
    row = len(GradingMatrix[0,:])
    column = len(GradingMatrix[:,0]) 
    Rounded=np.zeros((column))

    #Fulfilling the 3 conditions of grading. 
    #1) If -3 if present, print -3 ; 2) If only one grade is recieved, print that one grade  
    #3) Remove lowest grade, and print the average of the remaining grades.
    i = 0
    while i < column:
        if row == 1:
            Rounded[i] = GradingMatrix[i,:]
            
        elif np.min(GradingMatrix[i,:]) == -3:
           Rounded[i] = -3
           
        else:
            Rounded[i]=(np.sum(GradingMatrix[i,:])-np.min(GradingMatrix[i,:]))/(len(GradingMatrix[i,:])-1)
        i+=1
         
    gradesFinal=roundGrade(Rounded)
    #Returns the final grades
    return gradesFinal

print(computeFinalGrades(np.array([[4, 10, 2],[-3,2,12],[12,10,2]])))