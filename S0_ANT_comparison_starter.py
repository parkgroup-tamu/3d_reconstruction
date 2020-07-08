# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 16:22:19 2020

@author: WSK
@input: Four mp4 video files which are recorded at the top angle using different antenna types are required.
@output: 1. Two csv files that include x,y,z coordinates and summary of frame numbers from LED(color) detected frame according to each video file.
         2. A plot that results in performance comparison by different antenna types.
"""

from S1_extract_xyz_from_video import Extractxyz
from S2_topview_analysis import TopViewAnalysis
from S3_detected_frames_comp import ComparisonPlot

def main():
    # Add folder path that includes four mp4 videos which can generate Figure 2(e).
    # For example, path= 'C:\\Download\\3d_reconstruction\\01_Antenna_comparison_figure2_data\\'
    path= 'FILE_PATH_HERE\\'

    filename = 'Ant1_1W_top'
    Extractxyz.launch(path, filename + ".mp4", filename, 25, 90)
    TopViewAnalysis.launch(path, filename + ".csv", filename + "_rst.csv")
    
    filename = 'Ant2_1W_top'
    Extractxyz.launch(path, filename + ".mp4", filename, 25, 90)
    TopViewAnalysis.launch(path, filename + ".csv", filename + "_rst.csv")
    
    filename = 'Ant3_1W_top'
    Extractxyz.launch(path, filename + ".mp4", filename, 25, 90)
    TopViewAnalysis.launch(path, filename + ".csv", filename + "_rst.csv")
    
    filename = 'Ant4_1W_top'
    Extractxyz.launch(path, filename + ".mp4", filename, 25, 90)
    TopViewAnalysis.launch(path, filename + ".csv", filename + "_rst.csv")
        
    ComparisonPlot.launch(path, 'Ant_comparison_plot')

if __name__ == "__main__":
    main()
