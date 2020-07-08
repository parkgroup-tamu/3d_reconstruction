# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 08:27:13 2019

@author: WSK
@input: A csv file that includes x, y, z coordinates, and the number  of frames that LED detected from the top angle of the cage is required.
@output: 1. A csv file that includes summary information of recorded data at top angle.
"""

import pandas
import numpy as np

class TopViewAnalysis:

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
    
    def launch(path, ifilename, ofilename):
        
        df_top = pandas.read_csv(path + ifilename)
        
        top_f = df_top['f']
        top_x = df_top['x']
        top_y = df_top['y']
        top_a = df_top['a']
        top_frmNum = df_top['FrmNum']
        
        sorted_top = TopViewAnalysis.Sort_fxya(top_f,top_x, top_y, top_a)
        
        top_frmNum = top_frmNum[0] - sorted_top[0][0]
        xy_Num = len(sorted_top)
        
        xy_rst_list=[]
        xy_rst_list.append(['xy_total','xy_calculated'])
        xy_rst_list.append([top_frmNum, xy_Num])
        
        np.savetxt(path + ofilename, xy_rst_list ,delimiter=",", fmt='%s')
      