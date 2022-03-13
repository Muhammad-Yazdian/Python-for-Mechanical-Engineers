#=========================================================
# example_2D_1_vector.py
#
# A simple example for drawing 2D vectors using graphiclib
#
# Author(s):
#   Seied Muhammad Yazdian
#
# Last update:
#   Feb 1, 2022
#=========================================================

import numpy as np
import matplotlib.pyplot as plt
import graphiclib_path
import graphiclib as gl
import mathlib_path
import mathlib as ml

point_0 = np.array([1, 0, 0])
point_1 = np.array([2, 0.1, 0])
vector_1 = np.array([1.5, 1, 0])

# Display contents
fig = plt.figure()
ax = plt.axes()
gl.draw_arrow_2d(ax, [1, 1], [0, 0])
gl.draw_arrow_2d(ax, [1, 1.1], [0, 0], color='r')
gl.draw_arrow_2d(ax, vector_1, point_0, color='g')
gl.draw_arrow_2d(ax, vector_1, point_1, color='b')
ax.set_aspect('equal')
plt.show()
