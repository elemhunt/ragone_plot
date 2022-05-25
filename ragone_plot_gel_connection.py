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

# micro = 1E-6
# mili = 1E-3

#------------------------------------------------------------------------#
# Load in Data
# Note: route of csv files may need to be changes depending on directory
#   and how many idex row you must skip.
#------------------------------------------------------------------------#

df = pd.read_csv('/Users/elemhunt/Desktop/Ragone Plot Data - Microsupercap.csv',skiprows=[i for i in range(1,2)])

#------------------------------------------------------------------------#
# Set x and y values for the scatter plot.
# Note: Imput use there column labels. Convert values to be the same.
#------------------------------------------------------------------------#

All_x_values = df['Warea.1']
All_y_values = df['Parea.1']

x_h2s04_liq = All_x_values[0:2] 
y_h2s04_liq = All_y_values[0:2]

x_h3p04_liq = All_x_values[2:4] 
y_h3p04_liq = All_y_values[2:4]

x_h2s04_liq_PVA = All_x_values[4:6] 
y_h2s04_liq_PVA = All_y_values[4:6]

x_h2s04_PVA = All_x_values[6:14] 
y_h2s04_PVA = All_y_values[6:14]

x_h3p04_PVA = All_x_values[14:18] 
y_h3p04_PVA = All_y_values[14:18]

x_h2s04_PVA_wire = All_x_values[18:] 
y_h2s04_PVA_wire = All_y_values[18:]

#------------------------------------------------------------------------#
# Plot
# Note: Legend and line color/width may need to be changed accrodingly
#------------------------------------------------------------------------#


# #fig.plot(x_values,y_values,'.', linewidth=2.0)
# #ax1.legend(['Fresh Gel','Day Old Gel'],loc='upper left', prop={'size': 7})

fig, ax = plt.subplots()
# ax.scatter(x_05_Supercap_NN,y_05_Supercap_NN,linewidth= 0.025)
# ax.scatter(x_1_Supercap_NN,y_1_Supercap_NN,linewidth= 0.025)

ax.scatter(x_h2s04_liq,y_h2s04_liq,marker = '.', color='orangered')

ax.scatter(x_h3p04_liq,y_h3p04_liq,marker = '.', color='gold')

ax.scatter(x_h2s04_liq_PVA,y_h2s04_liq_PVA,marker = '.', color='yellowgreen')

ax.scatter(x_h2s04_PVA,y_h2s04_PVA,marker = '.', color='lightskyblue')

ax.scatter(x_h3p04_PVA,y_h3p04_PVA,marker = '.', color='orchid')

ax.scatter(x_h2s04_PVA_wire,y_h2s04_PVA_wire,marker = '.', color='mediumblue')

ax.set_xscale('log')
ax.set_yscale('log')


ax.legend(['$H_2$S$O_4$ Liq','$H_3$P$O_4$ Liq', '$H_2$S$O_4$ Liq + PVA','$H_2$S$O_4$ PVA','$H_3$P$O_4$ PVA','$H_2$S$O_4$ PVA + Ag wire'],loc='upper left', prop={'size': 7})
plt.title ('Ragone Plot of Mirco-Supercapacitor Devices')
plt.xlabel("Specific Energy Density (Wh/$cm^2$)")
plt.ylabel("Specific Power Density (W/$cm^2$)")


plt.savefig('Ragone - MicroEleComp Plot.png', dpi = 1000)