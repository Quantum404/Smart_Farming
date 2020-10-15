# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 21:53:27 2020

@author: bambo
"""

# IMPORT ALL NECESSARY MODULES
import pandas as pd
import numpy as np
import os

# PICK AND READ DATASET DYNAMICALLY 
loc = os.getcwd() + r'/Datasets/Crop_Pred.csv'
table = pd.read_csv(loc)

# DROP DUPLICATE RECORDS (IF ANY)
table = table.drop_duplicates(subset = None, keep = 'first')

# GETTING RID OF ALL UNNECESSARY SYMBOLS OR NAMES
spec_chars = ["!",'"',"#","%","&","'","(",")",
              "*","+",",","-",".","/",":",";","<",
              "=",">","?","@","[","\\","]","^","_",
              "`","{","|","}","~","–"]
for char in spec_chars:
       table['Crop'] = table['Crop'].str.replace(char, ' ')
       table['Crop'] = table['Crop'].str.replace(r"\(.*\)","")

# FIX MORINGA ISSUE IN A SIMPLE MANNER
i = 0
for i in range(0, len(table['Crop'])):
    if(table.Crop[i] == "Drumstick   moringa"):
        table.Crop[i] = "Drumstick"
    else:
        continue


# INTERPOLATION USING NUMPY

table.N = table.N.astype('float64')
for i in range(0, len(table.N)):
    table.N[i] = round(np.interp(table.N[i], [10, 180], [0, 1]), 1)

table.P = table.P.astype('float64')
for i in range(0, len(table.P)):
    table.P[i] = round(np.interp(table.P[i], [10, 125], [0, 1]), 1)

table.K = table.K.astype('float64')
for i in range(0, len(table.K)):
    table.K[i] = round(np.interp(table.K[i], [10, 200], [0, 1]), 1)
    
# delete unnamed

table.drop(['Unnamed: 0'],axis=1,inplace=True)
indexing_Crop = {}    

#indexing each dataset

for index ,value in table.Crop.items():
    index = index+1
    indexing_Crop[index] = value

for index in range(0,len(table.Crop)):
    table.Crop[index] = index + 1
    