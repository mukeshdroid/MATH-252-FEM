# FRAME3DD ANALYSIS RESULTS  http://frame3dd.sf.net/ VERSION 20140514+ 
# Example A: linear static analysis of a 2D truss with support settlement (kips in)  
# Thu Mar 31 20:59:34 2022
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
set label ' 2' at   1.2000e+02,   0.0000e+00,   0.0000e+00
set label ' 3' at   2.4000e+02,   0.0000e+00,   0.0000e+00
set label ' 4' at   3.6000e+02,   0.0000e+00,   0.0000e+00
set label ' 5' at   4.8000e+02,   0.0000e+00,   0.0000e+00
set label ' 6' at   6.0000e+02,   0.0000e+00,   0.0000e+00
set label ' 7' at   7.2000e+02,   0.0000e+00,   0.0000e+00
set label ' 8' at   1.2000e+02,   1.2000e+02,   0.0000e+00
set label ' 9' at   2.4000e+02,   1.2000e+02,   0.0000e+00
set label ' 10' at   3.6000e+02,   1.2000e+02,   0.0000e+00
set label ' 11' at   4.8000e+02,   1.2000e+02,   0.0000e+00
set label ' 12' at   6.0000e+02,   1.2000e+02,   0.0000e+00
# ELEMENT NUMBER LABELS
set label ' 1' at   6.0000e+01,   0.0000e+00,   0.0000e+00
set label ' 2' at   1.8000e+02,   0.0000e+00,   0.0000e+00
set label ' 3' at   3.0000e+02,   0.0000e+00,   0.0000e+00
set label ' 4' at   4.2000e+02,   0.0000e+00,   0.0000e+00
set label ' 5' at   5.4000e+02,   0.0000e+00,   0.0000e+00
set label ' 6' at   6.6000e+02,   0.0000e+00,   0.0000e+00
set label ' 7' at   6.0000e+01,   6.0000e+01,   0.0000e+00
set label ' 8' at   1.2000e+02,   6.0000e+01,   0.0000e+00
set label ' 9' at   1.8000e+02,   6.0000e+01,   0.0000e+00
set label ' 10' at   2.4000e+02,   6.0000e+01,   0.0000e+00
set label ' 11' at   3.0000e+02,   6.0000e+01,   0.0000e+00
set label ' 12' at   3.6000e+02,   6.0000e+01,   0.0000e+00
set label ' 13' at   4.2000e+02,   6.0000e+01,   0.0000e+00
set label ' 14' at   4.8000e+02,   6.0000e+01,   0.0000e+00
set label ' 15' at   5.4000e+02,   6.0000e+01,   0.0000e+00
set label ' 16' at   6.0000e+02,   6.0000e+01,   0.0000e+00
set label ' 17' at   6.6000e+02,   6.0000e+01,   0.0000e+00
set label ' 18' at   1.8000e+02,   1.2000e+02,   0.0000e+00
set label ' 19' at   3.0000e+02,   1.2000e+02,   0.0000e+00
set label ' 20' at   4.2000e+02,   1.2000e+02,   0.0000e+00
set label ' 21' at   5.4000e+02,   1.2000e+02,   0.0000e+00
# set parametric
# set view 60, 70,  1.00 
# set view equal xyz # 1:1 3D axis scaling 
# unset key
# set xlabel 'x'
# set ylabel 'y'
# set zlabel 'z'
set title "Example A: linear static analysis of a 2D truss with support settlement (kips in)  \nanalysis file: ./tests/exA.3dd   deflection exaggeration: 50.0   load case 1 of 2 "
unset clip; 
set clip one; set clip two
set xyplane 0 
  plot '/tmp/ex-msh' u 2:3 t 'undeformed mesh' w lp lw 1 lt 5 pt 6, '/tmp/ex-mshf.001' u 1:2 t 'load case 1 of 2' w l lw 1 lt 3
# splot '/tmp/ex-msh' u 2:3:4 t 'load case 1 of 2' w lp  lw 1 lt 5 pt 6, '/tmp/ex-mshf.001' u 1:2:3 t 'load case 1 of 2' w l lw 1 lt 3
pause -1
set title "Example A: linear static analysis of a 2D truss with support settlement (kips in)  \nanalysis file: ./tests/exA.3dd   deflection exaggeration: 50.0   load case 2 of 2 "
unset clip; 
set clip one; set clip two
set xyplane 0 
  plot '/tmp/ex-msh' u 2:3 t 'undeformed mesh' w lp lw 1 lt 5 pt 6, '/tmp/ex-mshf.002' u 1:2 t 'load case 2 of 2' w l lw 1 lt 3
# splot '/tmp/ex-msh' u 2:3:4 t 'load case 2 of 2' w lp  lw 1 lt 5 pt 6, '/tmp/ex-mshf.002' u 1:2:3 t 'load case 2 of 2' w l lw 1 lt 3
