#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 12:21:17 2020

@author: elemhunt
"""


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#------------------------------------------------------------------------#
# Conversion Factors
# Note: route of csv files may need to be changes depending on directory
#------------------------------------------------------------------------#

micro = 1E-6
mili = 1E-3

#------------------------------------------------------------------------#
# Load in Data
# Note: route of csv files may need to be changes depending on directory
#   and how many idex row you must skip.
#------------------------------------------------------------------------#

df = pd.read_csv('/Users/elemhunt/Desktop/Supercap Results Analysis - Data.csv',skiprows=[i for i in range(1,2)])

df_sorted = df.sort_values(by=["a"], ascending=True)
df_Rsorted = df_sorted.reset_index()

#------------------------------------------------------------------------#
# Set x and y values for the scatter plot.
# Note: Imput use there column labels. Convert values to be the same.
#------------------------------------------------------------------------#

All_x_values = df_Rsorted['Warea']
All_y_values = df_Rsorted['Parea']

x_05_Supercap = All_x_values[0:25] 
y_05_Supercap = All_y_values[0:25]
x_05_Supercap_NN = x_05_Supercap.dropna() * micro
y_05_Supercap_NN = y_05_Supercap.dropna() * mili
x_05_Final = x_05_Supercap_NN.drop([22])
y_05_Final = y_05_Supercap_NN.drop([22])

x_1_Supercap = All_x_values[25:41]
y_1_Supercap = All_y_values[25:41]
x_1_Supercap_NN = x_1_Supercap.dropna() * micro
y_1_Supercap_NN = y_1_Supercap.dropna() * mili
x_1_Final = x_1_Supercap_NN.drop([35])
y_1_Final = y_1_Supercap_NN.drop([35])

x_Microsup = All_x_values[41:]
y_Microsup = All_y_values[41:]
x_Microsup_NN = x_Microsup.dropna() * micro
y_Microsup_NN = y_Microsup.dropna() * mili


#------------------------------------------------------------------------#
# Plot
# Note: Legend and line color/width may need to be changed accrodingly
#------------------------------------------------------------------------#


# #fig.plot(x_values,y_values,'.', linewidth=2.0)
# #ax1.legend(['Fresh Gel','Day Old Gel'],loc='upper left', prop={'size': 7})

fig, ax = plt.subplots()
# ax.scatter(x_05_Supercap_NN,y_05_Supercap_NN,linewidth= 0.025)
# ax.scatter(x_1_Supercap_NN,y_1_Supercap_NN,linewidth= 0.025)

ax.scatter(x_05_Final,y_05_Final,marker = '.', color='lightgreen')
ax.scatter(x_1_Final,y_1_Final,marker = '.', color='purple')
ax.scatter(x_Microsup_NN,y_Microsup_NN,marker = '.', color='orange')
ax.set_xscale('log')
ax.set_yscale('log')


ax.legend(['0.5 $cm^2$ Supercapacitor','1.0 $cm^2$ Supercapacitor', 'Micro-supercapacitor'],loc='upper left', prop={'size': 7})
plt.title ('Ragone Plot of Synthesized Devices')
plt.xlabel("Specific Energy Density (Wh/$cm^2$)")
plt.ylabel("Specific Power Density (W/$cm^2$)")


plt.savefig('Ragone Plot.png', dpi = 1000)