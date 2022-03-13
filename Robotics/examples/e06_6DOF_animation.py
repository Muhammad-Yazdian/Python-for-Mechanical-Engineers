#===============================================================================
# e06_6DOF_Animation
#
# A simple example for animating a generic robot using DH file and Robot class
# - Joint angles can be modified using angle() method
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
from matplotlib.animation import FuncAnimation
import graphiclib_path
import graphiclib as gl
import os
import time

path = os.path.dirname( __file__ ) + '/e04_6DOF_DH_file.csv'
robot = rl.Robot(path)
fig = plt.figure()
ax = plt.axes(projection='3d')
num_steps = 10
for step in range(num_steps):
    theta_final = np.array([10, 10, 10, 10, 10, 10]) * 2
    theta = theta_final * step/num_steps
    ax.set(xlim=(-0, 20), ylim=(0, 20), zlim=(0, 20))
    # ax.grid(True)
    robot.set_angles(theta)
    plt.cla()
    robot.draw(ax)
    gl.set_axes_equal_3d(ax)
    plt.pause(0.03)
plt.show()