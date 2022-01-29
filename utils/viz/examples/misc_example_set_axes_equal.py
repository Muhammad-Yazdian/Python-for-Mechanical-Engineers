#==================================================================
# misc_set_axes_equal.py
# 
# A simple example for drawing 3D graphics with equal aspect ratio
#
# Seied Muhammad Yazdian | Jan 29, 2022
#==================================================================

import matplotlib.pyplot as plt
import numpy as np
import graphiclib_path
from graphiclib import set_axes_equal

# With equal axes
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
x = np.array([0, 1, 1, 1])
y = np.array([0, 0, 1, 1])
z = np.array([0, 0, 0, 5])
ax.plot(x, y, z)
set_axes_equal(ax)
plt.show()

# Without equal axes
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
x = np.array([0, 1, 1, 1])
y = np.array([0, 0, 1, 1])
z = np.array([0, 0, 0, 5])
ax.plot(x, y, z)
plt.show()