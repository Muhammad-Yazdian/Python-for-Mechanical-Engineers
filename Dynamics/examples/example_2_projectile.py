#===============================================================================
# example_2_projectile.py
#
# Simulating the 2D motion of a projectile using
#   - Euler algorithm and 
#   - quiver for drawing its velocity vector on its path.
#   - Note: The plot only shows a subset of the full simulation data points.
#
# Author(s):
#   Seied Muhammad Yazdian
#
# Last update:
#   Feb 6, 2022
#===============================================================================

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import graphiclib_path
import graphiclib as gl

# Simulaiton parameters
velocity_0 = 100  # (m/s)
theta_0 = 60  # (deg)
g = -9.81  # (m/s^2)
dt = 0.1  # (s)

# Drawing parameters
font_size = 14
every_nth_point = 10

# Init simulation
t = np.array([0])
position = np.array([[0, 0]])
theta_0_rad = np.radians(theta_0)
velocity = np.array([[np.cos(theta_0_rad), np.sin(theta_0_rad)]]) * velocity_0

while position[-1, 1] >= 0:
    t = np.append(t, t[-1]+dt)
    position = np.append(position, [position[-1] + velocity[-1]*dt], axis=0)
    velocity = np.append(velocity, [velocity[-1] + [0, g*dt]], axis=0)

# Display contents
matplotlib.rcParams['text.usetex'] = True
fig, ax = plt.subplots(figsize=(6, 4), tight_layout=True)
ax.plot(position[::every_nth_point, 0],
        position[::every_nth_point, 1], 'o')
Q = ax.quiver(position[::every_nth_point, 0],
              position[::every_nth_point, 1],
              velocity[::every_nth_point, 0],
              velocity[::every_nth_point, 1],
              pivot='tail',
              width=0.002)
qk = ax.quiverkey(Q, 0.85, 0.8, 100, r'$100 {m/s}$', labelpos='E',
                  coordinates='figure')
ax.set(aspect=1, xlim=(-100,1000), ylim=(-100,500))
ax.set_xlabel(r'$x(m)$', fontsize=font_size)
ax.set_ylabel(r'$y(m)$', fontsize=font_size)
plt.grid()
plt.show()
