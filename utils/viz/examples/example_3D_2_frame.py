#=========================================================
# e02_frame.py
# 
# A simple example for drawing 3D frames using graphiclib
#
# Author(s):
#   Seied Muhammad Yazdian
# 
# Last update:
#   Jan 30, 2022
#=========================================================
  
import numpy as np
import matplotlib.pyplot as plt
import graphiclib_path
import graphiclib as gl
import mathlib_path
import mathlib as ml

point_0 = np.array([0, 0, 0])
point_1 = np.array([0.75, 0.25, 0])
arrow_1 = np.array([1, 1, 1])
frame_1 = ml.rotatoinMatixZ(10)

# Display contents
fig = plt.figure()
ax = plt.axes(projection='3d')
gl.draw3D(ax, 'point', point_1, color='r')
gl.draw3D(ax, 'arrow', point_1, position=point_0, color='c')
gl.draw3D(ax, 'arrow', arrow_1, position=point_0, color='k')
gl.draw3D(ax, 'frame', frame_1, position=point_0)
gl.draw3D(ax, 'frame', frame_1, position=point_1, show_axis=(1, 0, 1))
gl.setAxesEqual3D(ax)
plt.show()