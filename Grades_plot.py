#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 11:38:02 2018

@author: Thomas
"""

#Grades per Assignment plot
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

filelines = pd.read_csv("test.csv")
matrix = np.array(filelines)
almostgrades = np.delete(matrix,0,1)
grades = np.delete(almostgrades,0,1)
    
def gradesPlot(grades): 
    # We use the jitter function to avoid overlapping data points
    jitter_min = -0.2
    jitter_max = 0.2
    
    # Creates an empty array for the mean x and y values
    xmean = []
    ymean = []
    for i in range(np.shape(grades)[1]): 
        x = i + 1 * np.ones(len(grades)) + (jitter_max - jitter_min) * np.random.random(size = len(grades)) + jitter_min  
        y = grades[:,i] 
        
        # Appends the assignment number and corresponding ave. grade to the empty arrays
        xmean = np.append(xmean,[i+1])
        ymean = np.append(ymean,[np.mean(grades[:,i])])
    
        # Plots grades as crosses in the coordinate system
        plt.plot(x, y, 'x')
        # Plots average grade per assignment as a line
        plt.plot(xmean,ymean, "r-", color = 'black', linewidth = 3)
    
    plt.xticks(np.arange(1.0, len(grades[0,:]) + 1))
    plt.yticks(np.array([-3,0,2,4,7,10,12]))

    # Labels the axis
    plt.xlabel('Assignments')
    plt.ylabel('Grades')
    plt.show()
            
print(gradesPlot(grades))