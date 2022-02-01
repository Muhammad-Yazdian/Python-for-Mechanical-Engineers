#=========================================================
# e02_frame.py
# 
# A simple example for drawing 2D frames using graphiclib
# 
# Author(s):
#   Seied Muhammad Yazdian
# 
# Last update:
#    Jan 30, 2022
#=========================================================
  
import numpy as np
import matplotlib.pyplot as plt
import graphiclib_path
import graphiclib as gl
import mathlib_path
import mathlib as ml

point_0 = np.array([0.0, 0, 0])
point_1 = np.array([6.0, 8, 0])
frame_1 = ml.rotatoinMatixZ(10)

# Display contents
fig = plt.figure()
ax = plt.axes()
gl.drawFrame(ax, frame_1, point_0, color=['k','k'])
gl.drawFrame(ax, -frame_1, point_1)
ax.set_aspect('equal')
plt.show()