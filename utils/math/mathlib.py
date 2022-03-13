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
    cb = np.cos(np.radians(theta_y))
    cg = np.cos(np.radians(theta_x))
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

    Rxyz = np.array([[ca*cb, ca*sb*sg-sa*cg, ca*sb*cg+sa*sg],
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


def find_axis_by_two_vectors_and_angles(vector_1, angle_1, vector_2, angle_2):    
    """Finds a 3D unit vector that makes angles angle_1 and angle_2 with
      vector_1 and vector_2 respectively.
      
      Note:
        This is the same as finding the intersection of cones with same vertcies

      Args:
        - vector_1 (ndarray): A 3D vector
        - angle_1 (float): The angle between vector_1 and to-be-found axis
        - vector_2 (ndarray): A 3D vector
        - angle_2 (float): The angle between vector_2 and to-be-found axis

      Returns:
        ndarray: Unit vector
    """
    #TODO: There are two sets of solutions. Include the second one as well
    e, f, g = vector_1
    p, q, r = vector_2
    a, b = np.cos(angle_1), np.cos(angle_2)
    A=np.sqrt(-a**2*p**2-a**2*q**2-a**2*r**2+2*a*b*e*p+2*a*b*f*q+2*a*b*g*r-b**2*e**2-b**2*f**2-b**2*g**2+e**2*q**2+e**2*r**2-2*e*f*p*q-2*e*g*p*r+f**2*p**2+f**2*r**2-2*f*g*q*r+g**2*p**2+g**2*q**2)
    N=a*e*q**2+a*e*r**2-a*f*p*q-a*g*p*r-b*e*f*q-b*e*g*r+b*f**2*p+b*g**2*p+A*(g*q-f*r)
    D=e**2*q**2+e**2*r**2-2*e*f*p*q-2*e*g*p*r+f**2*p**2+f**2*r**2-2*f*g*q*r+g**2*p**2+g**2*q**2
    x=N/D
    N=-a*e*p*q+a*f*p**2+a*f*r**2-a*g*q*r+b*e**2*q-b*e*f*p-b*f*g*r+b*g**2*q+e*r*A-g*p*A
    D=e**2*q**2+e**2*r**2-2*e*f*p*q-2*e*g*p*r+f**2*p**2+f**2*r**2-2*f*g*q*r+g**2*p**2+g**2*q**2
    y=N/D
    N=(-e*q+f*p)*A
    D=e**2*q**2+e**2*r**2-2*e*f*p*q-2*e*g*p*r+f**2*p**2+f**2*r**2-2*f*g*q*r+g**2*p**2+g**2*q**2
    N2=-a*e*p*r-a*f*q*r+a*g*p**2+a*g*q**2+b*e**2*r-b*e*g*p+b*f**2*r-b*f*g*q
    D2=e**2*q**2+e**2*r**2-2*e*f*p*q-2*e*g*p*r+f**2*p**2+f**2*r**2-2*f*g*q*r+g**2*p**2+g**2*q**2
    z=N/D+N2/D2
    return np.array([x,y,z])
