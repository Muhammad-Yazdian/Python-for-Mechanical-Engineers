#=========================================================
# example_3D_3_shapes.py
#
# A simple example for drawing 3D shapes using graphiclib
#
# Author(s):
#   Seied Muhammad Yazdian
#
# Last update:
#   Mar 7, 2022
#=========================================================

import numpy as np
import matplotlib.pyplot as plt
import graphiclib_path
import graphiclib as gl

circle_radius = 3
circle_position = np.array([1, 1, 0])
circle_normal = np.array([1, 1, 2])

fig = plt.figure()
ax = plt.axes(projection='3d')
gl.draw_circle_3d(ax, circle_position, circle_normal, circle_radius, 'r')
gl.draw_arrow_3d(ax, circle_normal, circle_position, 'k')
gl.set_axes_equal_3d(ax)
plt.show()
