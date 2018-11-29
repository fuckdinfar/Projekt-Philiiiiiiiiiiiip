#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 10:59:39 2018

@author: philip
"""
import numpy as np
#from roundGrade import roundGrade

def computeFinalGrades(grades):
    
    GradingMatrix = grades #Stating a zero vector
    

    N = len(GradingMatrix[:,0]) 
    M = len(GradingMatrix[0,:])
    vectorRounded=np.zeros((N))
    
    #Plugging inputs into the zero vecto .FinalGrades
    #Fulfilling the 3 conditions of grading. 
    i=0
    while i < N:
        if M == 1:
            vectorRounded[i] = GradingMatrix[i,:]
        elif np.min(GradingMatrix[i,:]) == -3:
           vectorRounded[i]=-3
        else:
            vectorRounded[i]=(np.sum(GradingMatrix[i,:])-np.min(GradingMatrix[i,:]))/(len(GradingMatrix[i,:])-1)
        i+=1
         
    gradesFinal=roundGrade(vectorRounded)
    #Returns final grades
    return gradesFinal

print(computeFinalGrades(np.array([[4, 10, 2],[-3,2,12]])))