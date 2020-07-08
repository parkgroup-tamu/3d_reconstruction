# 3d_reconstruction
This project includes sample videos and codes that can generate figures and several processed data files with csv format.

[01_Antenna_comparison_figure2_data] includes 4 video files which are source data for generating a bar graph that represents comparison result of wireless coverage corresponds to different antenna designs.

[02_3D_View_supplimentary_figure10_data] includes 9 video files which are source data for generating 3D reconstructed figures that trace an operating indicator LED and the cross-sectional view of it at each range of height for the three different antenna designs, respectively.


Users should install OpenCV before running codes.

Users should download all video files.

Users should download all codes in the same folder.


1. To generate a Antenna comparison figure,

	a. Open "S0_ANT_comparison_starter.py"
  
	b. Edit line 18, path = 'FILE_PATH_HERE\\'. FILE_PATH means path of the folder which includes 4-video files in 01_Antenna_comparison_figure2_data
  
  	c. User should insert double back-slashes('\\') when divide into directories.
  
  	d. Run "S0_ANT_comparison_starter.py"
  
  	e. If this code run correctly, user can find following files in the data folder.
	
Ant_comparison_plot.png, Ant1_1W_top.csv, Ant1_1W_rst.csv, Ant2_1W_top.csv, Ant2_1W_rst.csv, Ant3_1W_top.csv, Ant3_1W_rst.csv, Ant4_1W_top.csv, Ant4_1W_rst.csv
  
	
2. To generate 3D reconstruction figures,

  	a. Open "S0_3D_View_starter.py"
  
  	b. Edit line 18, path = 'FILE_PATH_HERE\\'. FILE_PATH means path of the folder which includes 9-video files in 02_3D_View_supplimentary_figure10_data
  
  	c. User should insert double back-slashes('\\') when divide into directories.
  
  	d. Run "S0_3D_View_starter.py"
  
  	e. If this code run correctly, user can find following files in the data folder.
	
a_rst_3d.png, a_rst_xy_1layer.png, a_rst_xy_2layer.png, a_rst_xy_3layer.png, a_rst_xy_4layer.png, a_rst.csv, a_top.csv, a_side_i.csv, a_side_w.csv
b_rst_3d.png, b_rst_xy_1layer.png, b_rst_xy_2layer.png, b_rst_xy_3layer.png, b_rst_xy_4layer.png, b_rst.csv, b_top.csv, b_side_i.csv, b_side_w.csv
c_rst_3d.png, c_rst_xy_1layer.png, c_rst_xy_2layer.png, c_rst_xy_3layer.png, c_rst_xy_4layer.png, c_rst.csv, c_top.csv, c_side_i.csv, c_side_w.csv
