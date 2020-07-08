# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 09:39:48 2019

@author: WSK
@input: A csv file is required. The file should include summary of x,y,z coordinates array corresponds to each antenna.
@output: Figures in x-y veiw by layers corresponds to each antenna.
"""

import matplotlib.pyplot as plt
import pandas
import numpy as np
from operator import itemgetter 

class ZaxisAnalysis:
    
    def typeTransfer(in_df):
        out = []
        in_df = in_df.dropna()
        
        for i in range(len(in_df)):
            out.append(in_df[i])
    
        return out
    
    def DrawFig(i, x, y, xmin, xmax, ymin, ymax, fname):
        
        xvar = xmax-xmin
        yvar = ymax-ymin
        
        
        fig = plt.figure(i)
        plt.plot(x, y,'red', ls='None', marker='.')
        plt.xlim(xmin-xvar/25,xmax+xvar/25)
        plt.ylim(ymin-yvar/16,ymax+yvar/16)
        
        fig.savefig(fname + str(i) + "layer.png", transparent=False)
    
        return 0
    
    def launch(path, filename):

        df = pandas.read_csv(path + filename +'.csv')
        
        x = ZaxisAnalysis.typeTransfer(df['x'])
        y = ZaxisAnalysis.typeTransfer(df['y'])
        z = ZaxisAnalysis.typeTransfer(df['z'])
        xmin = min(x)
        xmax = max(x)
        
        ymin = min(y)
        ymax = max(y)
        
        zmin = min(z)
        zmax = max(z)
        zgap = int((zmax - zmin)/4)
        
        xyz = np.transpose([x, y, z])
        sortedlist = sorted(xyz, key = itemgetter(2))
        
        x1 = []
        x2 = []
        x3 = []
        x4 = []
        y1 = []
        y2 = []
        y3 = []
        y4 = []
        z1 = []
        z2 = []
        z3 = []
        z4 = []
        i=0
        for i in range(len(sortedlist)):
            if sortedlist[i][2] <= zmin + zgap*1:
                x4.append(sortedlist[i][0])
                y4.append(sortedlist[i][1])
                z4.append(sortedlist[i][2])
            elif sortedlist[i][2] <= zmin + zgap*2:
                x3.append(sortedlist[i][0])
                y3.append(sortedlist[i][1])
                z3.append(sortedlist[i][2])
            elif sortedlist[i][2] <= zmin + zgap*3:
                x2.append(sortedlist[i][0])
                y2.append(sortedlist[i][1])
                z2.append(sortedlist[i][2])
            else :
                x1.append(sortedlist[i][0])
                y1.append(sortedlist[i][1])
                z1.append(sortedlist[i][2])
        
        ZaxisAnalysis.DrawFig(1, x1, y1, xmin, xmax, ymin, ymax, path + filename + "_xy_")
        ZaxisAnalysis.DrawFig(2, x2, y2, xmin, xmax, ymin, ymax, path + filename + "_xy_")
        ZaxisAnalysis.DrawFig(3, x3, y3, xmin, xmax, ymin, ymax, path + filename + "_xy_")
        ZaxisAnalysis.DrawFig(4, x4, y4, xmin, xmax, ymin, ymax, path + filename + "_xy_")

        plt.show()
