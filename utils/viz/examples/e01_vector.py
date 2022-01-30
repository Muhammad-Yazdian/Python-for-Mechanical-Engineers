#=========================================================
# e01_vector.py
# 
# A simple example for drawing 3D vectors using graphiclib
#
# Seied Muhammad Yazdian | Jan 28, 2022
#=========================================================

import numpy as np
import matplotlib.pyplot as plt
import graphiclib_path
import graphiclib as gl

# Create some 3D points
point_a = np.array([0.0, 0, 0]) 
point_b = np.array([3.0, 0, 0])
point_c = np.array([0.0, 2, 0])
point_d = np.array([3.0, 3, 1])

# Create some 3D vectors
vector_a = np.array([0.0, 0, 0])
vector_b = np.array([3.0, 0, 0])
vector_c = np.array([0.0, 2, 0])
vector_d = np.array([3.0, 3, 1])
vector_e = vector_b + vector_c
vector_f = np.cross(vector_b, vector_c)
print(type(vector_e))
print(type(vector_f))

# Display the arrows
fig = plt.figure()
ax = plt.axes(projection='3d')
# Create and display some arrows/vectors based on the available points/vectors
gl.draw(ax, 'arrow', point_b, position=point_a, color='k')
gl.draw(ax, 'arrow', point_c, position=point_b, color='g')
gl.draw(ax, 'arrow', point_c, position=point_a, color='b')
gl.draw(ax, 'arrow', point_d, position=point_b, color='r')
gl.draw(ax, 'arrow', vector_e, position=point_a, color='r')
gl.draw(ax, 'arrow', vector_f, position=point_a, color='b')
gl.set_axes_equal(ax)
plt.show()