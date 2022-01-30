"""**Basic Mathematics for Robotics**

  - Author: S.M. Yazdian
  - Date: 2022

  Features:
   - Based on NumPy

  Usage: 
    Use *rl* namespace when importing roboticlib. 
    
    Example:
    ::
      import roboticlib as roblib
      alpha = 30 # (deg)
      rot_x = rl.rotatoinMatixX(alpha)"""

import numpy as np
import matplotlib.pyplot as plt


class Frame:
  def __init__(self, rotation_matrix):
    self.rotation_matrix = rotation_matrix

def rotatoinMatixX(theta):
  r"""Returns the rotation matrix of a frame rotated by :math:`\theta` degrees about x axis

    Args:
      - theta (float): Rotation angle about x axis (deg)

    Returns:
      - (float): Rotation matrix :math:`R_x`

      .. math::

        R_x=\begin{bmatrix}
        1 & 0 & 0\\
        0 & c_\theta & -s_\theta\\ 
        0 & s_\theta &  c_\theta
        \end{bmatrix}"""
  ct = np.cos(np.radians(theta))
  st = np.sin(np.radians(theta))
  return np.array([[1,  0,   0],
                    [0, ct, -st],
                    [0, st, ct]])


def rotatoinMatixY(theta):
  r"""Returns the rotation matrix of a frame rotated by :math:`\theta` degrees about y axis

    Args:
      - theta (float): Rotation angle about y axis (deg)

    Returns:
      - (float): Rotation matrix :math:`R_y`

      .. math::

        R_y=\begin{bmatrix}
        c_\theta & 0 & s_\theta\\ 
        0 & 1 & 0\\
        -s_\theta & 0 & c_\theta
        \end{bmatrix} """
  ct = np.cos(np.radians(theta))
  st = np.sin(np.radians(theta))
  return np.array([[ct, 0, st],
                    [0,  1,  0],
                    [-st, 0, ct]])


def rotatoinMatixZ(theta):
  r"""Returns the rotation matrix of a frame rotated by :math:`\theta` degrees about z axis

    Args:
      - theta (float): Rotation angle about z axis (deg)

    Returns:
      - (float): Rotation matrix :math:`R_z`

      .. math::

        R_z=\begin{bmatrix}
        c_\theta & -s_\theta &  0\\ 
        s_\theta &  c_\theta & 0\\ 
        0 & 0 & 1
        \end{bmatrix} """
  ct = np.cos(np.radians(theta))
  st = np.sin(np.radians(theta))
  return np.array([[ct, -st, 0],
                    [st, ct,  0],
                    [0,  0,   1]])


def rotatoinMatixJoint(alpha, theta):
  r"""Returns joint rotation matrix

    Args:
      - alpha (float): Angle between z axes (deg)
      - theta (float): Joint angle (deg)

    Returns:
      - (float): Joint rotation matrix R

      .. math::

        ^{i-1}\textrm{R}_i=\begin{bmatrix}
        c_\theta & -s_\theta c_\alpha & s_\theta s_\alpha\\ 
        s_\theta & c_\theta c_\alpha & -c_\theta s_\alpha\\ 
        0 & s_\alpha & c_\alpha
        \end{bmatrix} """
  ct = np.cos(np.radians(theta))
  st = np.sin(np.radians(theta))
  ca = np.cos(np.radians(alpha))
  sa = np.sin(np.radians(alpha))
  return np.array([[ct, -st*ca, st*sa],
                  [st, ct*ca, -ct*sa],
                  [0, sa, ca]])


def transformationMatrix(a, d, alpha, theta):
  r"""Returns robotic homogeneous transformation matrix (from frame i+1 to
    frame i)

    Args:
      - a (float): Link length
      - d (float): Prismatic displacement
      - alpha (float): Angle between z axes (deg)
      - theta (float): Joint angle (deg)

    Returns:
      - (float): Homogeneous transformation matrix T

      .. math::

        ^{i-1}\textrm{T}_i=\begin{bmatrix}
        c_\theta & -s_\theta c_\alpha & s_\theta s_\alpha & a c_\theta\\ 
        s_\theta & c_\theta c_\alpha & -c_\theta s_\alpha & a s_\theta\\ 
        0 & s_\alpha & c_\alpha & d\\ 
        0 & 0 & 0 & 1
        \end{bmatrix} """
  ct = np.cos(np.radians(theta))
  st = np.sin(np.radians(theta))
  ca = np.cos(np.radians(alpha))
  sa = np.sin(np.radians(alpha))
  return np.array([[ct, -st*ca,  st*sa,  a*ct],
                    [st,  ct*ca, -ct*sa,  a*st],
                    [0,   sa,     ca,     d],
                    [0,   0,      0,      1]])