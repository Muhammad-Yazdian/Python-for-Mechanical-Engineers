"""**Basic mathematics for matrix operation**

  Features:
    - Based on NumPy

  Usage: 
    Use *ml* namespace when importing mathlib.
    
    Example:
    ::
    
        import mathlib as ml
        alpha = 30 # (deg)
        rot_x = ml.rotation_matrix_x(alpha)
  """
# By Seied Muhammad Yazdian | Feb 1s, 2022

import numpy as np


def rotation_matrix_x(theta) -> np.ndarray:
  r"""Returns the 3x3 rotation matrix of a frame rotated by :math:`\theta` degrees about x axis

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


def rotation_matrix_y(theta):
  r"""Returns the 3x3 rotation matrix of a frame rotated by :math:`\theta` degrees about y axis

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


def rotation_matrix_z(theta):
  r"""Returns the 3x3 rotation matrix of a frame rotated by :math:`\theta` degrees about z axis

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