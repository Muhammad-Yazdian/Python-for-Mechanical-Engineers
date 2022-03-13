# ===============================================================================
# e01_rotate_frame.py
#
# A simple example for drawing rotation matrix
#
# Author(s):
#   Seied Muhammad Yazdian
#
# Last update:
#   Feb 1, 2022
# ===============================================================================

import numpy as np
import matplotlib.pyplot as plt
import graphiclib_path
import graphiclib as gl
import roboticlib_path
import roboticlib as rl

show_plots = True


def main():
    theta = float(0)
    rot_mat_1 = rl.rotation_matrix_z(theta)
    print('Rx = \n', rot_mat_1)

    theta = float(10)
    rot_mat_2 = rl.rotation_matrix_z(theta)
    print('Rx = \n', rot_mat_2)

    # Display contents
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    gl.draw_generic_3d(ax, 'frame', rot_mat_1, position=np.array([0, 0, 0]))
    gl.draw_generic_3d(ax, 'frame', rot_mat_2, position=np.array([0, 0, 0]))
    gl.set_axes_equal_3d(ax)
    if show_plots:
        plt.show()


if __name__ == '__main__':
    main()
