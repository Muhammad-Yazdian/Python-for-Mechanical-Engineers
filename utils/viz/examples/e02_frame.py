#=========================================================
# e02_frame.py
# 
# A simple example for drawing 3D frames using graphiclib
#
# Seied Muhammad Yazdian | Jan 29, 2022
#=========================================================
  
import numpy as np
import matplotlib.pyplot as plt
import graphiclib_path
import graphiclib as gl
import roboticlib_path
import roboticlib as rl

point_a = gl.Point3d(0, 0, 0)
point_b = gl.Point3d(0, 0, 2)

# Display contents
fig = plt.figure()
ax = plt.axes(projection='3d')
gl.GraphicalFrame(ax, point_a)
rotz = rl.rotatoinMatixZ(30)
gl.GraphicalFrame(ax, point_a, rotz)
gl.set_axes_equal(ax)
plt.show()

