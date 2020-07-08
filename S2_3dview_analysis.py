# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 18:58:04 2019

@author: WSK
@input: Three csv files from different angles (top and two sidewards) are required.
        Each file should include information of x,y,z coordinates and number of detected frames.
@output: 1. Figure in 3-D view shows traces of mouse movement(operating indicator LED).
         2. A csv file that includes summary information of recorded data according to each planes.
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas
import numpy as np

class ThreeDimensionViewAnalysis:
    
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
    
    def launch(path, ifilenamet, ifilenamew, ifilenamei, ofilename):

        # put into the .csv file whith is obtained using 'S1_extract_xyz_from_video.py'
        df_top = pandas.read_csv(path + ifilenamet + '.csv') # top view
        df_sidew = pandas.read_csv(path + ifilenamew + '.csv') # side view 1
        df_sidei = pandas.read_csv(path + ifilenamei + '.csv') # side view 2
        
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
            
        
        sorted_top = ThreeDimensionViewAnalysis.Sort_fxya(top_f,top_x, top_y, top_a)
        sorted_sidew = ThreeDimensionViewAnalysis.Sort_fxya(sw_f, sw_x, sw_y, sw_a)
        sorted_sidei = ThreeDimensionViewAnalysis.Sort_fxya(si_f, si_x, si_y, si_a)

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
        sorted_side = ThreeDimensionViewAnalysis.Sort_fxya(sm_f, sm_x, sm_y, sm_a)
        
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
        merge_xyz = ThreeDimensionViewAnalysis.Sort_fxya(m_f, m_x, m_y, m_a)
        
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
        
        fxmin = min(fX)
        fxmax = max(fX)
        fymin = min(fY)
        fymax = max(fY)
        fzmin = min(fZ)
        fzmax = max(fZ)
        
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.plot3D(fX, fY, fZ,'red', ls='None', marker='.')
        #ax.grid(b=None)
        #ax.axis('off')
        ax.set_xlim3d(fxmin-50,fxmax+50)
        ax.set_ylim3d(fymin-50,fymax+50)
        ax.set_zlim3d(fzmin-50,fzmax+50)
        fig.savefig(path + ofilename + "_3d.png", transparent=True)
        
        plt.show()
        
        xyz_rst_list=[]
        xyz_rst_list.append(['x','y','z','xy_total','yz_total','xy_calculated','yz_calculated','xyz_calculated','xy_or_yz'])
        i=0
        for i in range(xyz_Num):
            xyz_rst_list.append([fX[i], fY[i], fZ[i], 0, 0, 0, 0, 0, 0])
        
        xyz_rst_list[1][3] = xy_frmNum
        xyz_rst_list[1][4] = yz_frmNum
        xyz_rst_list[1][5] = xy_Num
        xyz_rst_list[1][6] = yz_Num
        xyz_rst_list[1][7] = xyz_Num
        xyz_rst_list[1][8] = len(merge_xyz)
        
        np.savetxt(path + ofilename + ".csv", xyz_rst_list ,delimiter=",", fmt='%s')
        
              