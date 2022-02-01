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

point_0 = np.array([0, 0, 0])
point_1 = np.array([2, 0, 0])
vector_1 = np.array([1, 1, 0])

# Display contents
fig = plt.figure()
ax = plt.axes()
gl.drawArrow(ax, [0, 0], [1, 0.5])
gl.drawArrow(ax, point_0, point_1, color='r')
gl.drawArrow(ax, point_0, point_0 + vector_1, color='g')
ax.set_aspect('equal')
plt.show()
