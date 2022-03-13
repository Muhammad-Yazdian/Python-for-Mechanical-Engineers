#===============================================================================
# e03_2DOF_RR_DH_array.py
#
# A simple example for drawing a RR robot using its DH array
#
# Author(s):
#   Seied Muhammad Yazdian
#
# Last update:
#   Feb 3, 2022
#===============================================================================

import numpy as np
import roboticlib_path
import roboticlib as rl
import matplotlib.pyplot as plt
import graphiclib_path
import graphiclib as gl

theta_1 = 20.0
theta_2 = 30.0

LINK1 = 3.0
LINK2 = 2.0

DH_a = [LINK1, LINK2]
DH_d = [0.0, 0.0]
DH_alpha = [0.0, 0.0]
DH_theta = [theta_1, theta_2]
DH_table = np.transpose([DH_a, DH_d, DH_alpha, DH_theta])

endeffector_transformation_matrix = rl.forward_kinematics(DH_table)
endeffector_position = endeffector_transformation_matrix[0:3, 3]

transformation_matrix_all = rl.forward_kinematics_all_joints(DH_table)

p0 = transformation_matrix_all[0, 0:3, 3]
p1 = transformation_matrix_all[1, 0:3, 3]
p2 = transformation_matrix_all[2, 0:3, 3]

# Display contents
fig = plt.figure()
ax = plt.axes(projection='3d')
gl.draw_generic_3d(ax, 'point', endeffector_position, color = 'c')
gl.draw_generic_3d(ax, 'trans', transformation_matrix_all[0])
gl.draw_generic_3d(ax, 'trans', transformation_matrix_all[1])
gl.draw_generic_3d(ax, 'trans', transformation_matrix_all[2])
# plt.plot((p0[0], p1[0]), (p0[1], p1[1]), (p0[2], p1[2]), 'k')
# plt.plot((p1[0], p2[0]), (p1[1], p2[1]), (p1[2], p2[2]), 'k')
gl.draw_generic_3d(ax, 'arrow', p1-p0, position=p0, color='k')
gl.draw_generic_3d(ax, 'arrow', p2-p1, position=p1, color='k')
gl.set_axes_equal_3d(ax)
plt.show()
