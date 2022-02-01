#=========================================================
# example_3D_1_vector.py
#
# A simple example for drawing 3D vectors using graphiclib
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

# Create some 3D points
point__a = np.array([0.0, 0, 0])
point__b = np.array([3.0, 0, 1])
point__c = np.array([0.0, 2, 0])

# Create some 3D vectors
vector_a = np.array([0.0, 0, 0])
vector_b = np.array([3.0, 0, 1])
vector_c = np.array([0.0, 2, 0])
vector_d = vector_b + vector_c
vector_e = np.cross(vector_b, vector_c)

# Display the arrows
fig = plt.figure()
ax = plt.axes(projection='3d')
# Create and display some arrows/vectors based on the available points/vectors
gl.draw3D(ax, 'point', point__a, color='k')
gl.draw3D(ax, 'point', point__b, color='r')
gl.draw3D(ax, 'point', point__c, color='g')
gl.draw3D(ax, 'arrow', vector_b, position=point__a, color='r')
gl.draw3D(ax, 'arrow', vector_c, position=point__a, color='g')
gl.draw3D(ax, 'arrow', vector_d, position=point__a, color='b')
gl.draw3D(ax, 'arrow', vector_e, position=point__a, color='k')
gl.draw3D(ax, 'arrow', vector_e, position=point__b, color='c')
gl.draw3D(ax, 'arrow', vector_e, position=point__c, color='c')
gl.setAxesEqual3D(ax)
plt.show()
