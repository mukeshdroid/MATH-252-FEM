# FRAME3DD ANALYSIS RESULTS  http://frame3dd.sf.net/ VERSION 20140514+ 
# Input Data file for Verification-I - 2D structural frame analysis (N m Kg) 
# Tue Apr 19 14:19:30 2022
# G N U P L O T   S C R I P T   F I L E 
set autoscale
unset border
set pointsize 1.0
set xtics; set ytics; set ztics; 
unset zeroaxis
unset key
unset label
set size ratio -1    # 1:1 2D axis scaling 
# set view equal xyz # 1:1 3D axis scaling 
# NODE NUMBER LABELS
set label ' 1' at   0.0000e+00,   0.0000e+00,   0.0000e+00
set label ' 2' at   2.0000e+00,   0.0000e+00,   0.0000e+00
set label ' 3' at   4.0000e+00,   0.0000e+00,   0.0000e+00
set label ' 4' at   6.0000e+00,   0.0000e+00,   0.0000e+00
set label ' 5' at   8.0000e+00,   0.0000e+00,   0.0000e+00
set label ' 6' at   8.0000e+00,   2.9180e+00,   0.0000e+00
set label ' 7' at   6.0000e+00,   2.1840e+00,   0.0000e+00
set label ' 8' at   4.0000e+00,   1.4560e+00,   0.0000e+00
set label ' 9' at   2.0000e+00,   7.2800e-01,   0.0000e+00
# ELEMENT NUMBER LABELS
set label ' 1' at   1.0000e+00,   0.0000e+00,   0.0000e+00
set label ' 2' at   3.0000e+00,   0.0000e+00,   0.0000e+00
set label ' 3' at   5.0000e+00,   0.0000e+00,   0.0000e+00
set label ' 4' at   7.0000e+00,   0.0000e+00,   0.0000e+00
set label ' 5' at   8.0000e+00,   1.4590e+00,   0.0000e+00
set label ' 6' at   7.0000e+00,   2.5510e+00,   0.0000e+00
set label ' 7' at   5.0000e+00,   1.8200e+00,   0.0000e+00
set label ' 8' at   3.0000e+00,   1.0920e+00,   0.0000e+00
set label ' 9' at   1.0000e+00,   3.6400e-01,   0.0000e+00
set label ' 10' at   2.0000e+00,   3.6400e-01,   0.0000e+00
set label ' 11' at   3.0000e+00,   7.2800e-01,   0.0000e+00
set label ' 12' at   4.0000e+00,   7.2800e-01,   0.0000e+00
set label ' 13' at   5.0000e+00,   7.2800e-01,   0.0000e+00
set label ' 14' at   6.0000e+00,   1.0920e+00,   0.0000e+00
set label ' 15' at   7.0000e+00,   1.4590e+00,   0.0000e+00
# set parametric
# set view 60, 70,  1.00 
# set view equal xyz # 1:1 3D axis scaling 
# unset key
# set xlabel 'x'
# set ylabel 'y'
# set zlabel 'z'
set title "Input Data file for Verification-I - 2D structural frame analysis (N m Kg) \nanalysis file: mainproblem.3dd   deflection exaggeration: 5.0   load case 1 of 2 "
unset clip; 
set clip one; set clip two
set xyplane 0 
  plot '/tmp/mainproblem-msh' u 2:3 t 'undeformed mesh' w lp lw 1 lt 5 pt 6, '/tmp/mainproblem-mshf.001' u 1:2 t 'load case 1 of 2' w l lw 1 lt 3
# splot '/tmp/mainproblem-msh' u 2:3:4 t 'load case 1 of 2' w lp  lw 1 lt 5 pt 6, '/tmp/mainproblem-mshf.001' u 1:2:3 t 'load case 1 of 2' w l lw 1 lt 3
pause -1
set title "Input Data file for Verification-I - 2D structural frame analysis (N m Kg) \nanalysis file: mainproblem.3dd   deflection exaggeration: 5.0   load case 2 of 2 "
unset clip; 
set clip one; set clip two
set xyplane 0 
  plot '/tmp/mainproblem-msh' u 2:3 t 'undeformed mesh' w lp lw 1 lt 5 pt 6, '/tmp/mainproblem-mshf.002' u 1:2 t 'load case 2 of 2' w l lw 1 lt 3
# splot '/tmp/mainproblem-msh' u 2:3:4 t 'load case 2 of 2' w lp  lw 1 lt 5 pt 6, '/tmp/mainproblem-mshf.002' u 1:2:3 t 'load case 2 of 2' w l lw 1 lt 3
