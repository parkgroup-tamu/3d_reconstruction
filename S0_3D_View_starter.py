# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 18:20:47 2020

@input: Nine mp4 video files that are recorded at the top and two sideward angles using three different antenna designs are required.
@output: 1. Four csv files that include x,y,z coordinates and summary of frame numbers from LED(color) detected frame according to each antenna design.
         2. A 3D reconstruction image of traces of an operating indicator LED
         3. Four xy plane reconstruction images in different height of the cage according to each antenna design.
"""

from S1_extract_xyz_from_video import Extractxyz
from S2_3dview_analysis import ThreeDimensionViewAnalysis
from S3_xy_view_z_analysis import ZaxisAnalysis

def main():
    path = 'E:\\Dropbox\\TAMU_ECEN\\Lab\\My Work\\Python_script\\3d_reconstruction\\3D_view_analysis\\'
    
    ifilename = 'a_Proposed_'
    ofilename = 'a_'
    
    Extractxyz.launch(path, ifilename + "top.mp4", ofilename + "top", 25, 90)
    Extractxyz.launch(path, ifilename + "side_w.mp4", ofilename + "side_w", 25, 90)
    Extractxyz.launch(path, ifilename + "side_i.mp4", ofilename + "side_i", 25, 90)
    
    ThreeDimensionViewAnalysis.launch(path, ofilename + "top", ofilename + "side_w", ofilename + "side_i", ofilename + "rst" )
    ZaxisAnalysis.launch(path, ofilename + "rst")
    
    ifilename = 'b_2turn_'
    ofilename = 'b_'
    
    Extractxyz.launch(path, ifilename + "top.mp4", ofilename + "top", 25, 90)
    Extractxyz.launch(path, ifilename + "side_w.mp4", ofilename + "side_w", 25, 90)
    Extractxyz.launch(path, ifilename + "side_i.mp4", ofilename + "side_i", 25, 90)
    
    ThreeDimensionViewAnalysis.launch(path, ofilename + "top", ofilename + "side_w", ofilename + "side_i", ofilename + "rst" )
    ZaxisAnalysis.launch(path, ofilename + "rst")
    
    ifilename = 'c_Singluar_'
    ofilename = 'c_'
    
    Extractxyz.launch(path, ifilename + "top.mp4", ofilename + "top", 15, 40)
    Extractxyz.launch(path, ifilename + "side_w.mp4", ofilename + "side_w", 15, 40)
    Extractxyz.launch(path, ifilename + "side_i.mp4", ofilename + "side_i", 15, 40)
    
    ThreeDimensionViewAnalysis.launch(path, ofilename + "top", ofilename + "side_w", ofilename + "side_i", ofilename + "rst" )
    ZaxisAnalysis.launch(path, ofilename + "rst")

if __name__ == "__main__":
    main()