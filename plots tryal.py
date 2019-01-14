# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 17:25:51 2018

@author: ev213
"""
# creating a general plotting function 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# data files
# 'D:\\\Mini\\\18650_un\\\
data =[pd.read_csv('Unbalanced_5cell_2Ah_5deg_ch1_1312 - 001.csv',skiprows = 2,encoding='iso-8859-1'),
       pd.read_csv('Unbalanced_5cell_2Ah_5deg_ch2_1312 - 002.csv',skiprows = 2,encoding='iso-8859-1'),
       pd.read_csv('Unbalanced_5cell_2Ah_5deg_ch3_1312 - 003.csv',skiprows = 2,encoding='iso-8859-1'),
       pd.read_csv('Unbalanced_5cell_2Ah_5deg_ch4_1312 - 004.csv',skiprows = 2,encoding='iso-8859-1'),
       pd.read_csv('Unbalanced_5cell_2Ah_5deg_ch5_1312 - 005.csv',skiprows = 2,encoding='iso-8859-1'),
       ]
           # 2 is a maccor setting to  skip rows
           # can write a function to append more files if needed

#data = []
#i = 0
#for name in inputs:
#    # read csv
#    cell = pd.read_csv(inputs[i],skiprows=inputs[5],encoding='iso-8859-1',sep ='\s+')
#    data.append(cell)    
#    if name == 2:
#        print('done')
#        break
#    i = i+1


# second for loop
data2 = []
h = 0
for dataframe in data:
    # check column headers are strings 
    all(isinstance(column, str) for column in data[h].columns) # checks
    if False:
        # make them strings
        data[h].columns = list(map(str, data[h].columns)) # turns into string
        continue
     # create new dataframe
    #data[h].set_index(columns)
    new_data = data[h].loc[:,['Rec#','Step','Amps','Volts']]
    data2.append(new_data)
#    if isnan():
#        break
    h = h + 1
    
#     # make stepnumbers indices on y axis
#     data[x].set_index('Step')
#     # create new dataframes
     
   
    
    
    
    
    
    # create new dataframes

# make step number the index
# create new dataframe with relevant steps only:
    # make step number col as string and use iloc
    # keep it as a number and use loc
    # delete the unrelevant steps (see how to eliminate empty rows)

# do I need to convert frames into arrays?

