#=========================================================
# e02_frame.py
# 
# A simple example for drawing 3D frames using graphiclib
#
# Seied Muhammad Yazdian | Jan 30, 2022
#=========================================================
  
import numpy as np
import matplotlib.pyplot as plt
import graphiclib_path
import graphiclib as gl
import roboticlib_path
import roboticlib as rl

point_0 = np.array([0, 0, 0])
point_1 = np.array([0.75, 0.25, 0])
arrow_1 = np.array([1, 1, 1])
frame_1 = rl.Frame(rl.rotatoinMatixZ(0))

# Display contents
fig = plt.figure()
ax = plt.axes(projection='3d')
gl.draw(ax, point_1, color='r')
gl.draw(ax, arrow_1, position=point_0, color='k')
gl.draw(ax, frame_1, position=point_0)
gl.set_axes_equal(ax)
plt.show()