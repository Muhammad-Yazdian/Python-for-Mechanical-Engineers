# ===============================================================================
# e08_puma_560_class.py
#
# This script simulates Puma 560 FK and IK for position and rotation using the
# RobotPuma560 class.
#   - Test the position error or IK model on a line
#   - Input: None
#   - Joint angles can be modified using set_angle() method
#   - #TODO: Workspace restriction:
#   - #TODO: Joint angle limits
#
# Author(s):
#   Seied Muhammad Yazdian (@Muhammad-Yazdian)
#
# Last update:
#   Feb 12, 2022
# ===============================================================================

import numpy as np
import roboticlib_path
import roboticlib as rl
import matplotlib.pyplot as plt
import graphiclib_path
import graphiclib as gl

show_plots = True


def main():
    puma = rl.RobotPuma560()
    puma.set_angles([10, 20, 30, 0, 0, 0])

    # Display contents
    # fig = plt.figure()
    # ax = plt.axes(projection='3d')
    # puma.draw_puma(ax)
    # gl.set_axes_equal_3d(ax)
    # plt.show()

    result = puma.inverse_kinematics(puma.transformation_matrix_all[-1, :, :])
    print(result)

    temp = puma.transformation_matrix_all[-1, :, :]
    trans_matrix_desired = np.identity(4)
    trans_matrix_desired[:3, :3] = rl.rotation_matrix_x(180)
    trans_matrix_desired[:3, 3] = temp[:3, 3]
    x_start = 3.0
    x_delta = 1.0
    position_desired_0 = np.array(temp[:3, 3])
    position_desired_0[0] = x_start
    # position_desired_0[1] = x_start

    fig = plt.figure()
    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()
    ax = plt.axes(projection='3d')
    for i in range(100):
        trans_matrix_desired[0, 3] = x_start + i/100.0 * x_delta
        # trans_matrix_desired[1,3] = x_start + i/100.0 * x_delta
        joint_angles = puma.inverse_kinematics(trans_matrix_desired)
        puma.set_angles([joint_angles[0], joint_angles[1], joint_angles[2],
                        joint_angles[3], joint_angles[4], joint_angles[5]])
        if show_plots:
            plt.cla()
            ax.plot([0, 0], [-3, 3], 'gray')
            ax.plot([-3, 3], [0, 0], 'gray')
            # puma.draw(ax)
            puma.draw_puma(ax)
            gl.draw_arrow_3d(ax, [x_delta, 0, 0],
                             position_desired_0, color='gray')
            ax.set(xlim=(3, 5), ylim=(1, 2), zlim=(2, 3))
            gl.set_axes_equal_3d(ax)
            # ax.view_init(elev=90, azim=-90)
            ax.view_init(elev=32, azim=-55)
            plt.pause(0.03)
        print('Error x =', (puma.transformation_matrix_all[-1, 0, 3]
                            - trans_matrix_desired[0, 3])*100, '(mm)')
    if show_plots:
        plt.show()


if __name__ == '__main__':
    main()
