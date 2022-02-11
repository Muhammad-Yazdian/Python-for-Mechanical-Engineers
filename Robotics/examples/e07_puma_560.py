#===============================================================================
# e07_puma_560.py
#
# This script simulates Puma 560 FK and IK
#   - Input: DH parametes file: e07_puma_560_dh.csv
#   - Joint angles can be modified using angle() method
#   - #TODO: Add an animation
#   - #TODO: Add a image with CS
#   - #TODO: Workspace restriction: hyp0 > d2, and ...
#   - #TODO: Joint angle limits
#
# Author(s):
#   Seied Muhammad Yazdian (@Muhammad-Yazdian)
#
# Last update:
#   Feb 10, 2022
#===============================================================================

import numpy as np
from numpy.linalg import inv
import roboticlib_path
import roboticlib as rl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import graphiclib_path
import graphiclib as gl
import os
import time

theta_final = np.array([15, 15, 10, 0, 0, 0])

def puma_560_fk():
    pass


def puma_560_ik(robot, T_tip, hand='left', elbow='up', flip='no'):
    dh = robot.dh_array
    D1 = dh[0, 1] # It is always a positive constant (for Puma)
    D2 = dh[1, 1] # It is always a positive constant (for Puma)
    D4 = dh[3, 1] # It is always a positive constant (for Puma)
    A2 = dh[1, 0] # It is always a positive constant (for Puma)
    A3 = dh[2, 0] # It is always a positive constant (for Puma)
    D6 = dh[5, 1] # It is always a positive constant (for Puma)
    
    T56 = np.identity(4)
    T56[2, 3] = D6
    T = np.matmul(T_tip, inv(T56))
    x, y, z = T[:3, 3]

    # Compute theta1
    hyp0 = np.hypot(x, y)
    alpha1 = np.arcsin(D2/hyp0)
    phi1 = np.arctan2(y, x)
    theta1 = phi1 - alpha1
    if hand == 'right':
        theta1 = phi1 + alpha1 + np.pi
    
    # Compute theta2
    h1 = -(z - D1)
    phi2 = np.arctan2(h1, hyp0*np.cos(alpha1))
    hyp1 = np.hypot(h1, hyp0*np.cos(alpha1))
    hyp2 = np.hypot(A3, D4)
    alpha2 = np.arccos((A2**2 + hyp1**2 - hyp2**2)/(2*A2*hyp1))
    theta2 = phi2 - alpha2
    if elbow == 'down':
        theta2 = phi2 + alpha2
    
    # Compute theta2
    beta3 = np.arccos((A2**2 + hyp2**2 - hyp1**2)/(2*A2*hyp2))
    ALPHA3 = np.arccos(A3/hyp2)
    theta3 = np.pi - beta3 - ALPHA3

    return (theta1, theta2, theta3)


path = os.path.dirname(__file__) + '/e07_puma_560_dh.csv' # PUMA_560_LeftArm_ElbowUp
robot = rl.Robot(path)
puma_560_fk() 
fig = plt.figure()
ax = plt.axes(projection='3d')
num_steps = 30
for step in range(num_steps):
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

robot.angles(theta_final)
endeffector_frame = robot.transformation_matrix_all[6]

# result = puma_560_ik(robot, 
#                      endeffector_frame[0, 3], 
#                      endeffector_frame[1, 3], 
#                      endeffector_frame[2, 3],
#                      hand='left', elbow='up')

result = puma_560_ik(robot, endeffector_frame, hand='left', elbow='up')
print(theta_final)
print(np.degrees(result))
