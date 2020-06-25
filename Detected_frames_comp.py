# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 11:21:21 2019

@author: WSK
@input: A csv file is required.
        The file includes information on the total frame number and
        the number of extracted frames in each view of different antennas.
@output: 1. A plot of comparison results in the detected frame ratio with different antennas.
         2. A plot of comparison results in the detected frame number and total frame number with different antennas.
"""


import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import pandas
import matplotlib.pyplot as plt

def typeTransfer(in_df):
    out = []
    in_df = in_df.dropna()
    out = int(in_df.values)
    return out

path = 'FILE PATH'
df = pandas.read_csv(path + 'INPUT FILE NAME.csv')
    
ant1 = typeTransfer(df['ANT1'])
ant1_xy = np.array(typeTransfer(df['ANT1_xy']))
ant1_res = ant1_xy/ant1*100

ant2 = np.array(typeTransfer(df['ANT2']))
ant2_xy = np.array(typeTransfer(df['ANT2_xy']))
ant2_res = ant2_xy/ant2*100

ant3 = np.array(typeTransfer(df['ANT3']))
ant3_xy = np.array(typeTransfer(df['ANT3_xy']))
ant3_res = ant3_xy/ant3*100

ant4 = np.array(typeTransfer(df['ANT4']))
ant4_xy = np.array(typeTransfer(df['ANT4_xy']))
ant4_res = ant4/ant4*100

ant5 = np.array(typeTransfer(df['ANT5']))
ant5_xy = np.array(typeTransfer(df['ANT5_xy']))
ant5_res = ant5_xy/ant5*100

objects = ('1', '2', '3', '4', '5')
y_pos = np.arange(len(objects))
performance = [ant1_res, ant2_res, ant3_res, ant4_res, ant5_res]

plt.figure(1)
plt.bar(y_pos, performance, 0.45, align='center', alpha = 0.8, color = ('red', 'gray','gray','gray', 'gray'))
plt.xticks(y_pos, objects)
plt.ylabel('Detected frame ratio')
plt.xlabel('Antennas')
plt.ylim(-10,120)

# data to plot
n_groups = 5
total_frm = [ant1, ant2, ant3, ant4, ant5]
xy_frm = [ant1_xy, ant2_xy, ant3_xy, ant4_xy, ant5_xy]

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, xy_frm, bar_width,
alpha=opacity,
color='r',
label='xy')

rects2 = plt.bar(index + bar_width, total_frm, bar_width,
alpha=opacity,
color='b',
label='total')

plt.xlabel('Antennas')
plt.ylabel('frame number')
plt.xticks(index + bar_width, ('1', '2', '3', '4', '5'))
plt.ylim(-100,3000)

#plt.legend()

plt.show()