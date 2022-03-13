# ===============================================================================
# e04_6DOF_DH_file.py
#
# A simple example for drawing a generic robot by reading DH parameters in a
# csv file
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
from numpy import genfromtxt
import os

show_plots = True


def drawRobot(ax, transformation_matrix_all):
    """Draws the whole robot"""
    i = 0
    p_a = transformation_matrix_all[i, 0:3, 3]
    for i in range(transformation_matrix_all.shape[0]):
        gl.draw_generic_3d(ax, 'trans', transformation_matrix_all[i])
        if i > 0:
            p_b = transformation_matrix_all[i, 0:3, 3]
            gl.draw_generic_3d(ax, 'arrow', p_b-p_a, position=p_a, color='k')
            p_a = p_b


def main():
    path = os.path.dirname(__file__) + '/e04_6DOF_DH_file.csv'
    DH_table = genfromtxt(path, delimiter=',')[:, 1:5]
    endeffector_transformation_matrix = rl.forward_kinematics(DH_table)
    endeffector_position = endeffector_transformation_matrix[0:3, 3]
    transformation_matrix_all = rl.forward_kinematics_all_joints(DH_table)

    # Display contents
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    drawRobot(ax, transformation_matrix_all)
    gl.draw_generic_3d(ax, 'point', endeffector_position,
                       color='c')  # Optional
    gl.set_axes_equal_3d(ax)
    if show_plots:
        plt.show()


if __name__ == '__main__':
    main()
