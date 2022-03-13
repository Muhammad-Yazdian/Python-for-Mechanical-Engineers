#===============================================================================
# example_1_projectile.py
#
# Simulating the 2D motion of a projectile using Euler algorithm and drawing
# its velocity vector on its path 
#
# Author(s):
#   Seied Muhammad Yazdian
#
# Last update:
#   Feb 5, 2022
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
gl.draw_arrow_2d(ax, [v_x, v_y], [0, 0])

for i in range(num_steps):
    x += v_x * dt
    y += v_y * dt # Compute position before updating velocity
    v_y += g * dt
    gl.draw_arrow_2d(ax, [v_x, v_y], [x, y])
    t = t + dt

plt.grid()
plt.show()
