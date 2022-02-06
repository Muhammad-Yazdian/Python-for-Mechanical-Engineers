#===============================================================================
# example_3_mass_spring_damper.py
#
# Simulating the 2D motion of a mass-spring-damper system using Euler algorithm
#
# Author(s):
#   Seied Muhammad Yazdian (@muhammad-yazdian)
#
# Last update:
#   Feb 6, 2022
#===============================================================================

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def massSpringDamperModel(q, t, m, k, b):
    """Mathematical model of an ideal mass-spring-damper system

      Args:
        - q (float): System state(s)
        - t (float): Time
        - m (float): Mass (kg)
        - k (float): Stiffness (N/m)
        - b (float): Damping coefficient (Ns/m)

      Returns:
        float: :math:`dq/dt`
      """
    q_dt = [q[1], -1/m * (b*q[1] + k*q[0])]
    return q_dt


# System parameters
m = 1  # (kg)
k = 1  # (N/m)
b = 0.1  # (Ns/m)
q_0 = [1, 0]  # initial condition [(m), (m/s)]

# Simulation using ODE solver
t = np.linspace(0, 15, 300)
q_a = odeint(massSpringDamperModel, q_0, t, args=(m, k, b))
q_b = odeint(massSpringDamperModel, q_0, t, args=(m, k, 0))

# Display contents
matplotlib.rcParams['text.usetex'] = True
fig, ax = plt.subplots()
ax.plot(t, q_a[:, 0], 'C1', label=r'$x_a$')
ax.plot(t, q_b[:, 0], 'C2', label=r'$x_b$')
ax.set_xlabel(r'$Time (s)$')
ax.set_ylabel(r'$Position (m)$')
plt.legend()
plt.show()
