# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 18:58:04 2019

@author: WSK
@input: Three csv files from different angles are required.
        Each file should include information of x,y,z coordinates, and frame number.
@output: 1. Figure in 3-D view shows traces of mouse movement.
         2. Summary of information as each angle.
"""

import matplotlib.pyplot as plt
import pandas
import numpy as np

def Comparision(input1, input2):
    if input1 == input2:
        return 1

    else:
        return 0

def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 

def Sort_fxya(f, x, y, a):
    
    def Sort(i,cnt):
        tmpA = a[i+cnt]
        result_cnt = cnt
        while(cnt):
           if(tmpA > a[i+cnt-1]):
               cnt = cnt-1
           else:
               tmpA = a[i+cnt-1]
               cnt = cnt-1
               result_cnt = cnt
               
        return result_cnt
    
    sorted_val = []
    cnt = 1
    det = 1
    fix = 0
    i = 0
    while (i < len(f)):
        while(det):
           if (i+cnt) == len(f):
               cnt = cnt-1
               det = 0
               break
           else:
               if f[i] == f[i+cnt]:
                   cnt = cnt + 1
               else:
                   cnt = cnt - 1
                   det = 0
        if cnt == 0:
            sorted_val.append([f[i], x[i], y[i], a[i]])
        else:
            fix = Sort(i, cnt)
            sorted_val.append([f[i+fix], x[i+fix], y[i+fix], a[i+fix]])
        det = 1
        i = i + cnt + 1
    return sorted_val

path = 'FILE_PATH\\'
folderName = 'FOLDER_NAME'
path = path + folderName
df_top = pandas.read_csv(path + '\\FILE1_NAME.csv')
df_sidew = pandas.read_csv(path + '\\FILE2_NAME.csv')
df_sidei = pandas.read_csv(path + '\\FILE3_NAME.csv')

top_f = df_top['f']
top_x = df_top['x']
top_y = df_top['y']
top_a = df_top['a']
top_frmNum = df_top['FrmNum']

sw_f = df_sidew['f']
sw_x = df_sidew['x']
sw_y = df_sidew['y']
sw_a = df_sidew['a']
sw_frmNum = df_sidew['FrmNum']

si_f = df_sidei['f']
si_x = df_sidei['x']
si_y = df_sidei['y']
si_a = df_sidei['a']
si_frmNum = df_sidei['FrmNum']
    

sorted_top = Sort_fxya(top_f,top_x, top_y, top_a)
sorted_sidew = Sort_fxya(sw_f, sw_x, sw_y, sw_a)
sorted_sidei = Sort_fxya(si_f, si_x, si_y, si_a)


merge_side = sorted_sidew + sorted_sidei

merge_side.sort(key=lambda x: x[0])

sm_f = []
sm_x = []
sm_y = []
sm_a = []

for i in range(len(merge_side)):
    sm_f.append(merge_side[i][0])
    sm_x.append(merge_side[i][1])
    sm_y.append(merge_side[i][2])
    sm_a.append(merge_side[i][3])
sorted_side = Sort_fxya(sm_f, sm_x, sm_y, sm_a)

idx = 0
for i in range(0, len(sorted_top)):
    for j in range(0, len(sorted_side)):
        if sorted_top[i][0] == sorted_side[j][0]:
            k = i
            l = j
            idx = 1
            break
    if idx == 1:
        break
xy_frmNum = top_frmNum[0] - sorted_top[k][0]
if sw_frmNum[0] > si_frmNum[0] :
    yz_frmNum = sw_frmNum[0]-sorted_side[l][0]
else:
    yz_frmNum = si_frmNum[0]-sorted_side[l][0]

del sorted_top[0:k]
del sorted_side[0:l]

xy_Num = len(sorted_top)
yz_Num = len(sorted_side)

merge_xyz = sorted_top + sorted_side
merge_xyz.sort(key=lambda x: x[0])
m_f = []
m_x = []
m_y = []
m_a = []

for i in range(len(merge_xyz)):
    m_f.append(merge_xyz[i][0])
    m_x.append(merge_xyz[i][1])
    m_y.append(merge_xyz[i][2])
    m_a.append(merge_xyz[i][3])
merge_xyz = Sort_fxya(m_f, m_x, m_y, m_a)

sorted_xyz = []
x = []
y = []
z = []

i = 0
for i in range(len(sorted_top)):
   for j in range(len(sorted_side)):
       if sorted_top[i][0] == sorted_side[j][0]:
           sorted_xyz.append([sorted_top[i][0], sorted_top[i][1], sorted_top[i][2], sorted_side[j][2]])
           x.append(sorted_top[i][1])
           y.append(sorted_top[i][2])
           z.append(sorted_side[j][2])
           break

xyz_Num = len(sorted_xyz)

fX = np.array(x)
fY = np.array(y)
fZ = np.array(z)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(fX, fY, fZ,'red', ls='None', marker='.')
ax.grid(b=None)
ax.axis('off')
ax.set_xlim3d(60,780)
ax.set_ylim3d(0,480)
ax.set_zlim3d(150,360)
fig.savefig(path + "\\3d.png", transparent=True)

plt.show()

np.savetxt(path + "\\" + folderName + ".csv", np.column_stack((fX, fY, fZ)),delimiter=",", fmt='%s')

file1 = open(path + "\\" + folderName + ".txt","w") 
L1 = "Total xy and yz frames are {}, {}".format(xy_frmNum,yz_frmNum)
L2 = "Calculated xy, yz, and xyz frames are {}, {}, {}".format(xy_Num, yz_Num, xyz_Num)
L3 = "xy or yz frames {}".format(len(merge_xyz))

file1.writelines(L1)
file1.write("\n")
file1.writelines(L2)
file1.write("\n")
file1.writelines(L3)
file1.close()
      