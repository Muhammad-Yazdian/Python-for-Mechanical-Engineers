#=========================================================
# e02_rr_robot.py
# 
# A simple example for drawing a RR robot
#
# Seied Muhammad Yazdian | Jan 30, 2022
#=========================================================

import numpy as np
import roboticlib_path
import roboticlib as rl
import matplotlib.pyplot as plt 
import graphiclib_path
import graphiclib as gl

LINK1 = 3.0
LINK2 = 2.0

theta_1 = 10.0
theta_2 = 20.0

frame_00 = rl.rotatoinMatixZ(0.0)
frame_01 = rl.rotatoinMatixZ(theta_1)
frame_12 = rl.rotatoinMatixZ(theta_1+theta_2)
frame_02 = np.matmul(frame_01, frame_12)

p0 = np.array([0,0,0])
p1 = np.matmul(frame_01, np.array([LINK1,0,0]))
p2 = np.matmul(frame_01, np.array([LINK1,0,0] + np.matmul(frame_12, np.array([LINK2,0,0]))))

# Display contents
fig = plt.figure()
ax = plt.axes(projection='3d')
gl.draw(ax, 'frame', frame_00, position=p0)
gl.draw(ax, 'frame', frame_01, position=p1)
gl.draw(ax, 'frame', frame_02, position=p2)
plt.plot((p0[0], p1[0]), (p0[1], p1[1]),(p0[2], p1[2]),'k')
plt.plot((p1[0], p2[0]), (p1[1], p2[1]),(p1[2], p2[2]),'k')
gl.set_axes_equal(ax)
plt.show()