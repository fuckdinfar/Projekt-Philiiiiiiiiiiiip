# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 14:42:02 2018

@author: Bruger
"""

def roundGrades(grades):
    Values = [-3,0,2,4,7,10,12]
    gradesRounded = []
    for i in range(len(grades)): 
        gradesRounded.append(i)
        if (grades[i] < -1.5 and grades[i]>=-3):
           gradesRounded[i] = -3
        if (grades[i] >-1.5 and grades[i] <1):
           gradesRounded[i]=0
        if (grades[i] >= 1 and grades[i] < 3): 
           gradesRounded[i] = 2 
        if (grades[i] >3 and grades[i]<5.5):
            gradesRounded[i] = 4
        if (grades[i] >= 5.5 and grades[i] < 8.5):
            gradesRounded[i] = 7
        if (grades[i] >= 8.5 and grades[i] <= 11):
            gradesRounded[i] = 10
        if (grades[i] > 11 and grades[i] <= 12) :
            gradesRounded[i] = 12
        if (grades[i]< -3 or grades[i]> 12):
            gradesRounded[i] = 'Invalid grade'
        
    return gradesRounded
print(roundGrades([7.6,5.2,-19,2,1,6,9,10,28,11,12,0,4.5,4.678]))