# import sys
import roboticlib_path
import roboticlib as rl

theta = float(0)
rot_mat_1 = rl.rotatoinMatixZ(theta)
print('Rx = \n', rot_mat_1)

theta = float(10)
rot_mat_2 = rl.rotatoinMatixZ(theta)
print('Rx = \n', rot_mat_2)

# Display contents
import numpy as np
import matplotlib.pyplot as plt 
import graphiclib_path
import graphiclib as gl

fig = plt.figure()
ax = plt.axes(projection='3d')
gl.draw(ax, 'frame', rot_mat_1, position=np.array([0,0,0]))
gl.draw(ax, 'frame', rot_mat_2, position=np.array([0,0,0]))
gl.set_axes_equal(ax)
plt.show()
