#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 14:59:26 2018

@author: Thomas
"""
import numpy as np
import matplotlib.pyplot as plt

def gradesPlot(gradesFinal):
    
    grds = ('-3','00','02','4','7','10','12')
    x_pos = np.arange(len(grds))
    
    minus3 = gradesFinal == -3
    minus3 = np.extract(minus3,gradesFinal)
    A = np.size(minus3)
    
    zero = gradesFinal == 0
    zero = np.extract(zero,gradesFinal)
    B = np.size(zero)
    
    two = gradesFinal == 2
    two = np.extract(two,gradesFinal)
    C = np.size(two)
    
    four = gradesFinal == 4
    four = np.extract(four,gradesFinal)
    D = np.size(four)
    
    seven = gradesFinal == 7
    seven = np.extract(seven,gradesFinal)
    E = np.size(seven)
    
    ten = gradesFinal == 10
    ten = np.extract(ten,gradesFinal)
    F = np.size(ten)
    
    twelve = gradesFinal == 12
    twelve = np.extract(twelve,gradesFinal)
    G = np.size(twelve)
    
    occurences = [A,B,C,D,E,F,G]
    
    #Plots the data
    plt.bar(x_pos, occurences, align='center', alpha=1, color=['chocolate', 'indianred', 'dimgrey', 'springgreen', 'dodgerblue', 'fuchsia', 'gold'], width = 0.7, edgecolor = "k")
    plt.xticks(x_pos, grds,)
    plt.title('Grade Occurences')
    plt.xlabel('Grades', fontsize = 10)
    plt.ylabel('Occurences', fontsize = 10)
    plt.show()
    
    # We define jitter-min/max so the same grades does not overlap each other in the plot




grades = np.array([[7,7,7,7],[4,4,2,2],[-3,0,12,10]])

    
print(gradesPlot(grades))   
    
