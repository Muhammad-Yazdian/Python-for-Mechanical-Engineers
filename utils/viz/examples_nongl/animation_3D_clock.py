#===============================================================================
# animation_2D_clock.py
#
# Animates the minute handle of an analog clock using matplotlib
#
# Author(s):
#   Seied Muhammad Yazdian
#
# Last update:
#   Feb 2, 2022
#===============================================================================
import numpy as np
import matplotlib.pyplot as plt

TOTAL_TIME = 60  # (seconds)

fig = plt.figure()
ax = plt.axes(projection='3d')

for time in range(TOTAL_TIME+1):
    theta = np.radians(6*time)
    x = np.sin(theta)
    y = np.cos(theta)
    z = np.cos(theta)/5
    plt.cla()
    ax.plot([0, x], [0, y], [0, z], 'r')
    ax.plot([0, x], [0, y], [0, 0], 'gray')
    ax.plot([x, x], [y, y], [0, z], 'gray')
    ax.plot([-1, 1], [0.0, 0.0], 'gray')
    ax.plot([0.0, 0.0], [-1, 1], 'gray')
    ax.set(xlim=(-1.5, 1.5), ylim=(-1.5, 1.5), zlim=(-1.5, 1.5))
    # ax.grid(True)
    plt.pause(1/60)

plt.show()
