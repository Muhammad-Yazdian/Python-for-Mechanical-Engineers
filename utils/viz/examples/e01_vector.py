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
point_a = gl.Point3d(0, 0, 0)
point_b = gl.Point3d(3, 0, 0)
point_c = gl.Point3d(0, 2, 0)
point_d = gl.Point3d(3, 3, 1)

# Create some 3D vectors
vector_a = gl.Vector3d(0, 0, 0)
vector_b = gl.Vector3d(3, 0, 0)
vector_c = gl.Vector3d(0, 2, 0)
vector_d = gl.Vector3d(3, 3, 1)
vector_e = vector_b + vector_c

# Display the arrows
fig = plt.figure()
ax = plt.axes(projection='3d')
plt.xlim(-1, 4)
plt.ylim(-1, 4)
# plt.zlim(-3, 3) # Not supported.
ax.set_aspect('auto', 'box') # 'equal is not supported'

# Create and display some arrows/vectors based on the available points
arrow_1 = gl.Arrow3D2(point_a, point_b, ax, 'k')
arrow_2 = gl.Arrow3D2(point_b, point_c, ax, 'g')
arrow_3 = gl.Arrow3D2(point_a, point_c, ax, 'b')
arrow_4 = gl.Arrow3D2(point_b, point_d, ax, 'r')
arrow_5 = gl.Arrow3D2(point_a, vector_e, ax, 'r')

plt.show()