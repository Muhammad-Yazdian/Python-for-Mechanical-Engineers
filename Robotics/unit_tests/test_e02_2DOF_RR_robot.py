#===============================================================================
# A unit test for example for e02_2DOF_RR_robot.py example
# 
# NOTE: The entire example is copied into this file!
#
# Author(s):
#   Seied Muhammad Yazdian
#
# Last update:
#   Feb 4, 2022
#===============================================================================

import numpy as np
# import roboticlib_path
# Add libs to system path
import sys
import os
libs_path = os.path.dirname(os.path.dirname(__file__)) + '/libs'
sys.path.append(libs_path)
import roboticlib as rl
import matplotlib.pyplot as plt
# import graphiclib_path
import graphiclib as gl

LINK1 = 3.0
LINK2 = 2.0

theta_1 = 10.0
theta_2 = 20.0

frame_00 = rl.rotatoinMatixZ(0.0)
frame_01 = rl.rotatoinMatixZ(theta_1)
frame_12 = rl.rotatoinMatixZ(theta_2)
frame_02 = np.matmul(frame_01, frame_12)

p0 = np.array([0, 0, 0])
p1 = np.matmul(frame_01, np.array([LINK1, 0, 0]))
p2 = np.matmul(frame_01, np.array(
    [LINK1, 0, 0] + np.matmul(frame_12, np.array([LINK2, 0, 0]))))

trans_01 = rl.transformationMatrix(0, 1, 0, -10)

# Display contents
fig = plt.figure()
ax = plt.axes(projection='3d')
gl.draw3D(ax, 'frame', frame_00, position=p0)
gl.draw3D(ax, 'frame', frame_01, position=p1)
gl.draw3D(ax, 'frame', frame_02, position=p2)
plt.plot((p0[0], p1[0]), (p0[1], p1[1]), (p0[2], p1[2]), 'k')
plt.plot((p1[0], p2[0]), (p1[1], p2[1]), (p1[2], p2[2]), 'k')
gl.draw3D(ax, 'trans', trans_01)
gl.setAxesEqual3D(ax)
plt.show()
