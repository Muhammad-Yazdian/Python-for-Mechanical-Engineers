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

TOTAL_TIME = 15 # (seconds)

# fig = plt.figure(); ax = plt.axes()
fig, ax = plt.subplots()

for time in range(TOTAL_TIME+1):
    theta = np.radians(6*time)
    x = np.sin(theta)
    y = np.cos(theta)
    plt.cla()
    ax.plot([0, x], [0, y])
    ax.plot([-0.1, 0.1], [0.0, 0.0], 'gray')
    ax.plot([0.0, 0.0], [-0.1, 0.1], 'gray')
    ax.set(aspect='equal', xlim=(-1.5, 1.5), ylim=(-1.5, 1.5))
    ax.grid(True)
    plt.pause(1)

plt.show()
