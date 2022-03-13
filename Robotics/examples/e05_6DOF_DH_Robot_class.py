# ===============================================================================
# e05_6DOF_DH_Robot_class.py
#
# A simple example for drawing a generic robot using DH file and Robot class
# - Joint angles can be modified using angle() method
#
# Author(s):
#   Seied Muhammad Yazdian
#
# Last update:
#   Feb 3, 2022
# ===============================================================================

import numpy as np
import roboticlib_path
import roboticlib as rl
import matplotlib.pyplot as plt
import graphiclib_path
import graphiclib as gl
import os

show_plots = True


def main():

    path = os.path.dirname(__file__) + '/e04_6DOF_DH_file.csv'
    robot = rl.Robot(path)

    # Display contents
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    robot.draw(ax, show_axis=[1, 0, 1])
    gl.set_axes_equal_3d(ax)
    if show_plots:
        plt.show()

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    robot.set_angles([0, 0, 0, 0, 0, 0])
    robot.draw(ax, show_axis=[0, 0, 1])
    gl.set_axes_equal_3d(ax)
    if show_plots:
        plt.show()
