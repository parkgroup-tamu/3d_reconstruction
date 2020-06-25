# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 09:39:48 2019

@author: WSK
@input: A csv file is required. The file should include summary of x,y,z coordinates array corresponds to each antenna.
@output: Figures in x-y veiw by layers corresponds to each antenna.
"""

import matplotlib.pyplot as plt
import pandas

def typeTransfer(in_df):
    out = []
    in_df = in_df.dropna()
    
    for i in range(len(in_df)):
        out.append(in_df[i])

    return out

def DrawFig(i, x, y, xmin, xmax, ymin, ymax):
    
    xvar = xmax-xmin
    yvar = ymax-ymin
    
    
    plt.figure(i)
    plt.plot(x, y,'red', ls='None', marker='.')
    plt.xlim(xmin-xvar/25,xmax+xvar/25)
    plt.ylim(ymin-yvar/16,ymax+yvar/16)

    return 0

path = 'FILE PATH'

df = pandas.read_csv(path + 'FILE NAME.csv')

tx = typeTransfer(df['DATA1.x'])
txmin = min(tx)
txmax = max(tx)

ty = typeTransfer(df['DATA1.y'])
tymin = min(ty)
tymax = max(ty)

sx = typeTransfer(df['DATA2.x'])
sxmin = min(sx)
sxmax = max(sx)

sy = typeTransfer(df['DATA2.y'])
symin = min(sy)
symax = max(sy)

dx = typeTransfer(df['DATA3.x'])
dxmin = min(dx)
dxmax = max(dx)

dy = typeTransfer(df['DATA3.y'])
dymin = min(dy)
dymax = max(dy)

t1x = typeTransfer(df['DATA11.x'])
t1y = typeTransfer(df['DATA11.y'])
t2x = typeTransfer(df['DATA12.x'])
t2y = typeTransfer(df['DATA12.y'])
t3x = typeTransfer(df['DATA13.x'])
t3y = typeTransfer(df['DATA13.y'])
t4x = typeTransfer(df['DATA14.x'])
t4y = typeTransfer(df['DATA14.y'])

s1x = typeTransfer(df['DATA21.x'])
s1y = typeTransfer(df['DATA21.y'])
s2x = typeTransfer(df['DATA22.x'])
s2y = typeTransfer(df['DATA22.y'])
s3x = typeTransfer(df['DATA23.x'])
s3y = typeTransfer(df['DATA23.y'])
s4x = typeTransfer(df['DATA24.x'])
s4y = typeTransfer(df['DATA24.y'])

d1x = typeTransfer(df['DATA31.x'])
d1y = typeTransfer(df['DATA31.y'])
d2x = typeTransfer(df['DATA32.x'])
d2y = typeTransfer(df['DATA32.y'])
d3x = typeTransfer(df['DATA33.x'])
d3y = typeTransfer(df['DATA33.y'])
d4x = typeTransfer(df['DATA34.x'])
d4y = typeTransfer(df['DATA34.y'])

DrawFig(1, d1x, d1y, dxmin, dxmax, dymin, dymax)
DrawFig(2, d2x, d2y, dxmin, dxmax, dymin, dymax)
DrawFig(3, d3x, d3y, dxmin, dxmax, dymin, dymax)
DrawFig(4, d4x, d4y, dxmin, dxmax, dymin, dymax)

DrawFig(5, t1x, t1y, txmin, txmax, tymin, tymax)
DrawFig(6, t2x, t2y, txmin, txmax, tymin, tymax)
DrawFig(7, t3x, t3y, txmin, txmax, tymin, tymax)
DrawFig(8, t4x, t4y, txmin, txmax, tymin, tymax)

DrawFig(9, s1x, s1y, sxmin, sxmax, symin, symax)
DrawFig(10, s2x, s2y, sxmin, sxmax, symin, symax)
DrawFig(11, s3x, s3y, sxmin, sxmax, symin, symax)
DrawFig(12, s4x, s4y, sxmin, sxmax, symin, symax)

plt.show()
