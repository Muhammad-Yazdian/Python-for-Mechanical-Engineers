#===============================================================================
# e07_puma_560.py
#
# This script simulates Puma 560
#   - Input: DH parametes file (e07_puma_560_dh)
#   - Joint angles can be modified using angle() method
#   - #TODO: Add an animation
#   - #TODO: Add a image with CS
#
# Author(s):
#   Seied Muhammad Yazdian (@Muhammad-Yazdian)
#
# Last update:
#   Feb 10, 2022
#===============================================================================

import numpy as np
import roboticlib_path
import roboticlib as rl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import graphiclib_path
import graphiclib as gl
import os
import time

path = os.path.dirname(__file__) + '/e07_puma_560_dh.csv'
robot = rl.Robot(path)
fig = plt.figure()
ax = plt.axes(projection='3d')
num_steps = 100
for step in range(num_steps):
    theta_final = np.array([-0, -40, -30, 0, 30, 0])
    theta = theta_final * step/num_steps
    ax.set(xlim=(-0, 20), ylim=(0, 20), zlim=(0, 20))
    # ax.grid(True)
    robot.angles(theta)
    plt.cla()
    ax.plot([0, 0], [-3, 3], 'gray')
    ax.plot([-3, 3], [0, 0], 'gray')
    robot.draw(ax)
    gl.setAxesEqual3D(ax)
    plt.pause(0.03)
plt.show()
