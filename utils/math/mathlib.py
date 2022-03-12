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
from numpy.linalg import norm


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


def rotation_matrix_z_align_to(z_vector):
    """Constructs a relaxed frame (rotation matrix) based on the given z vector

      Args:
        - z_vector (ndarray): a vector representing the direction of z axis of
        the desired frame

      Returns:
        3x3 rotation matrix
    """
    z_axis = z_vector / norm(z_vector)
    dummy_vector = np.array([0, 1, 0])
    if np.dot(z_axis, dummy_vector) == 0:
        dummy_vector = np.array([1, 0, 0])
    x_axis_temp = np.cross(z_axis, dummy_vector)
    x_axis = x_axis_temp / norm(x_axis_temp)
    y_axis = np.cross(z_axis, x_axis)
    frame = np.zeros((3, 3))
    frame[:, 0] = x_axis
    frame[:, 1] = y_axis
    frame[:, 2] = z_axis
    return frame


def rotation_matrix_xy(theta_x, theta_y):
    """Sequence of rotaions along x and y axes

      Args:
        - theta_x (float): Rotation angle about x axis (deg)
        - theta_y (float): Rotation angle about y axis (deg)

      Returns:
        - (float): Rotation matrix :math:`R_xy`
      
        .. math::

        R_xy = R_y R_x """
    ca = np.cos(np.radians(theta_z))
    cb = np.cos(np.radians(theta_y))
    cg = np.cos(np.radians(theta_x))
    sa = np.sin(np.radians(theta_z))
    sb = np.sin(np.radians(theta_y))
    sg = np.sin(np.radians(theta_x))

    Rxy = np.array([[cb,  sb*sg, sb*cg],
                    [0,      cg,    sg],
                    [-sb, cb*sg, cb*cg]])

    return Rxy


def rotation_matrix_xyz(theta_x, theta_y, theta_z):
    """Sequence of rotaions along x, y, and z axes

      Args:
        - theta_x (float): Rotation angle about x axis (deg)
        - theta_y (float): Rotation angle about y axis (deg)
        - theta_z (float): Rotation angle about z axis (deg)

      Returns:
        - (float): Rotation matrix :math:`R_xyz`
      
        .. math::

        R_xyz = R_z R_y R_x """
    ca = np.cos(np.radians(theta_z))
    cb = np.cos(np.radians(theta_y))
    cg = np.cos(np.radians(theta_x))
    sa = np.sin(np.radians(theta_z))
    sb = np.sin(np.radians(theta_y))
    sg = np.sin(np.radians(theta_x))

    Rzyx = np.array([[ca*cb, ca*sb*sg-sa*cg, ca*sb*cg+sa*sg],
                     [sa*cb, sa*sb*sg+ca*cg, sa*sb*cg-ca*sg],
                     [-sb, cb*sg, cb*cg]])
        
    return R_xyz


def rotation_matrix_axis_angle(axis, theta):
    """Converts rotation theta around axis to a rotation matrix

      Args:
        - axis (ndarray): Rotation axis
        - theta (float): rotation angle(deg)

      Returns:
        ndarray: rotation matrix"""
    c = np.cos(np.radians(theta))
    s = np.sin(np.radians(theta))
    a = 1 - c
    x, y, z = axis
    return np.array([[x*x*a+c,   x*y*a-z*s, x*z*a+y*s],
                     [y*x*a+z*s, y*y*a+c,   y*z*a-x*s],
                     [z*x*a-y*s, z*y*a+x*s, z*z*a+c]])
