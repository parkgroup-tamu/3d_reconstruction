# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 11:21:21 2019

@author: WSK
@input: Four csv files are required.
        Each file includes information on the total frame number and
        the number of extracted frames from the top angle(xy plane) according to the antenna design.
@output: 1. A plot of the antenna comparison result.

"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import pandas
import matplotlib.pyplot as plt

class ComparisonPlot:
    
    def launch(path, ofilename):
        
        df1 = pandas.read_csv(path + 'Ant1_1W_top_rst.csv')
        df2 = pandas.read_csv(path + 'Ant2_1W_top_rst.csv')
        df3 = pandas.read_csv(path + 'Ant3_1W_top_rst.csv')
        df4 = pandas.read_csv(path + 'Ant4_1W_top_rst.csv')
            
        ant1 = df1['xy_total'][0]
        ant1_xy = df1['xy_calculated'][0]
        ant1_res = ant1_xy/ant1*100
        
        ant2 = df2['xy_total'][0]
        ant2_xy = df2['xy_calculated'][0]
        ant2_res = ant2_xy/ant2*100
        
        ant3 = df3['xy_total'][0]
        ant3_xy = df3['xy_calculated'][0]
        ant3_res = ant3_xy/ant3*100
        
        ant4 = df4['xy_total'][0]
        ant4_xy = df4['xy_calculated'][0]
        ant4_res = ant4_xy/ant4*100
        
        objects = ('1', '2', '3', '4')
        y_pos = np.arange(len(objects))
        performance = [ant1_res, ant2_res, ant3_res, ant4_res]
        
        fig = plt.figure(1)
        plt.bar(y_pos, performance, 0.45, align='center', alpha = 0.8, color = ('red', 'gray','gray','gray'))
        plt.xticks(y_pos, objects)
        plt.ylabel('Detected frame ratio')
        plt.xlabel('Antennas')
        plt.ylim(-10,120)
        
        plt.show()

        fig.savefig(path + ofilename + ".png", transparent=False)