# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 21:38:47 2018

@author: Frederik, Thomas and Philip
"""
#from dataload import dataLoad
#from DataStatistics import dataStatistics 
#from DataPlot import dataPlot
#from InputFunctions import inputStr,inputNumber,inputLimit,displayMenu,header
#from FilterFunctions import printFilter,filterData
import numpy as np
import pandas as pd
#Initial variables
dataLoaded = False


while True:
    header("MAIN MENU") #Interface
    
    #User Menu
    menu = displayMenu(["Load new data","Check for data errors","Generate plots", "Display list of grades", "Quit"])
    
    #Load data
    if menu == 1:
        #Checks for a valid filename
        header("LOAD DATA MENU") #Header
        print("type 'exit, if you wish to exit'")
        while True:
            try:
                filename = inputStr("Please enter the name of your datafile: ")
                print("") #Add
                
                #Check if user wants to exit
                if filename.lower() != "exit":
                    data = pd.read_csv(filename) #uses dataLoad to load data into our matrix
                    print("\nData was succesfully loaded from",filename)
                    dataLoaded = True # Puts data as loaded for future use
                    dataOld = np.copy(data) #Makes a copy of our data
                    break
                
                #Exits
                else:
                    break
                
            except FileNotFoundError:
                print("File could not be found, please try again")
    
    #Goes into filter data menu
    elif (menu == 2) and dataLoaded:
        while True:
            header("Check for data erros") #Header
            print("Choose one of the following options")
          
            
            menu2 = displayMenu(["Identical studentID","Invalid student grade",'Back'])
            
            #Bacteria type filter
            if menu2 == 1:
                print(data.loc[data.StudentID.duplicated()])
                
            #GR filter
            elif menu2 == 2:
                with open(data, 'rb') as f:
                   reader = csv.DictReader(f)
                   rows = [row for row in reader if row[''] != '0']

                   for row in rows:
                      print(row)
            #Back
            elif menu2 == 3:
                break
                        
    
    #Display statistics
    elif (menu == 3) and dataLoaded:
        header("Generate Plots") # Header for statistics
        gradesPlot(np.genfromtxt(test.csv,delimiter=',',names=true))
        print("")
       
            
    # Generates plot
    elif (menu == 4) and dataLoaded:
        header("Display list of grades")
    #Shows your current data
    #elif (menu == 5) and dataLoaded:
     #   np.set_printoptions(threshold=np.inf)
      #  np.set_printoptions(suppress=True)
       # print(data)
        #np.set_printoptions(threshold=8)
        
        
    #Quit
    elif menu == 5:
        break
    
    #If user has failed to load data, this message will be displayed
    else:
        print("ERROR: No data has been loaded, Please load your data using option 1")