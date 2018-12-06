# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 15:31:49 2018

@author: frederik
"""

#Plot for Grades per Assignment
import numpy as np
import matplotlib.pyplot as plt


    
def gradesPlot(grades): 
    # We define jitter-min/max so the same grades does not overlap each other in the plot
    jitter_min = -0.2
    jitter_max = 0.2
    grades=grades.transpose()
    
    # We use the function enumerate since we want our x(assigments) and y(grades) to be in the same dimension
    for n,grade in enumerate(grades):
    # We create an array so the different number 👎 of assignments has the same dimensions as the grade.
    # We also add jitter so the same grade does not overlap.    
        x =n*np.ones(len(grades)) + (jitter_max-jitter_min)*np.random.random(size=len(grades))+jitter_min+1
    
       # newGrade = grade   + jitter*(np.random.random(size=len(grade))-0.5)
        
        plt.plot(x,grades, 'o', label = 'Assignment #{:d}'.format(n),clip_on = False)
        
    plt.xticks(np.arange(1.0,len(grades)+1,1.0))
    plt.yticks(np.array([-3,0,2,4,7,10,12]))
    # Create names on the x-axis
    plt.xlabel('Assignments')
    # Create names on the y-axis
    plt.ylabel('Grades')
    
    plt.show()
    
print(gradesPlot(np.array([[7,7,7,7],[4,4,2,2],[-3,0,12,10]])))