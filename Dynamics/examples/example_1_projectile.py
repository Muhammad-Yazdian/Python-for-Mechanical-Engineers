#===============================================================================
# example_1_projectile.py
#
# Drawing the velocity of a projectile on its path
#
# Author(s):
#   Seied Muhammad Yazdian
#
# Last update:
#   Feb 1, 2022
#===============================================================================

import numpy as np
import matplotlib.pyplot as plt
import graphiclib_path
import graphiclib as gl

velocity = 100  # (m/s)
theta = 45  # (deg)
g = -9.81  # (m/s^2)
dt = 1.25  # (s)
num_steps = 15

theta_rad = np.radians(theta)
v_x = velocity * np.cos(theta_rad)
v_y = velocity * np.sin(theta_rad)
x = y = t = 0

# Display contents
fig = plt.figure()
ax = plt.axes()
gl.drawArrow(ax, [v_x, v_y], [0, 0])

for i in range(num_steps):
    x = x + v_x * dt
    v_y = v_y + g * dt
    y = y + v_y * dt
    gl.drawArrow(ax, [v_x, v_y], [x, y])
    t = t + dt

plt.grid()
plt.show()
