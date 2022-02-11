"""**Basic Mathematics for Robotics**

    Features:
        - Based on NumPy

  Usage:
    Use *rl* namespace when importing roboticlib. 
    
    Example:
    ::

        import roboticlib as rl
        alpha = 30 # (deg)
        rot_x = rl.rotation_matrix_x(alpha)"""

# By Seied Muhammad Yazdian | Feb 1s, 2022

import numpy as np
from numpy import genfromtxt
import mathlib_path
import mathlib as ml
import graphiclib_path
import graphiclib as gl

def rotation_matrix_x(theta):
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
    return ml.rotation_matrix_x(theta)


def rotation_matrix_y(theta):
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
        \end{bmatrix}"""
    return ml.rotation_matrix_y(theta)


def rotation_matrix_z(theta):
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
            \end{bmatrix}"""
    return ml.rotation_matrix_z(theta)


def rotation_matrix_joint(alpha, theta):
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
          \end{bmatrix}"""
    ct = np.cos(np.radians(theta))
    st = np.sin(np.radians(theta))
    ca = np.cos(np.radians(alpha))
    sa = np.sin(np.radians(alpha))
    return np.array([[ct, -st*ca, st*sa],
                    [st, ct*ca, -ct*sa],
                    [0, sa, ca]])


def transformation_matrix(a, d, alpha, theta):
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
              \end{bmatrix}"""
    ct = np.cos(np.radians(theta))
    st = np.sin(np.radians(theta))
    ca = np.cos(np.radians(alpha))
    sa = np.sin(np.radians(alpha))
    return np.array([[ct, -st*ca,  st*sa,  a*ct],
                    [st,  ct*ca, -ct*sa,  a*st],
                    [0,   sa,     ca,     d],
                    [0,   0,      0,      1]])


def forward_kinematics(DH_parameters):
    """Returns endeffector transformation matrix based on DH parameters

      Args:
        - DH_parameters (numpy.ndarray): Whole DH table

      Returns:
        numpy.ndarray: Endeffector transformation matrix
      """
    trans_0_previous = np.identity(4)
    for i in range(DH_parameters.shape[0]):
        row = DH_parameters[i]
        trans_previous_current = transformation_matrix(
            row[0], row[1], row[2], row[3])
        trans_0_current = np.matmul(trans_0_previous, trans_previous_current)
        trans_0_previous = trans_0_current
    return trans_0_current


def forward_kinematics_all_joints(DH_parameters):
    """Returns transformation matrix of all joints based on DH parameters

      Args:
        - DH_parameters (numpy.ndarray): Whole DH table

      Returns:
        numpy.ndarray: T matrix of all joints
      """
    trans_0_previous = np.identity(4)
    trans_0_joint_all = trans_0_previous
    for i in range(DH_parameters.shape[0]):
        row = DH_parameters[i]
        trans_previous_current = transformation_matrix(
            row[0], row[1], row[2], row[3])
        trans_0_current = np.matmul(trans_0_previous, trans_previous_current)
        if i == 0:
            trans_0_joint_all = np.stack(
                (trans_0_joint_all, trans_0_current), axis=0)
        else:
            # TODO: Combine np.append with the np.stack to remove if statement
            trans_0_joint_all = np.append(
                trans_0_joint_all, trans_0_current[np.newaxis, :], axis=0)
        trans_0_previous = trans_0_current
    return trans_0_joint_all


class Robot:
    """Creates a robot object with fk and draw functionalities

      Args:
        - DH_parameters (numpy.ndarray): Whole DH table
      """

    def __init__(self, dh_param_file):
        self.dh_array = genfromtxt(dh_param_file, delimiter=',')[:,1:5]
        self.transformation_matrix_all = forward_kinematics_all_joints(
            self.dh_array)
    

    def angles(self, theta):
        """Update robot joint angles

          Args:
            - theta (list): Joint angles
         """
        self.dh_array[:,3] = theta
        self.transformation_matrix_all = forward_kinematics_all_joints(
            self.dh_array)

      
    def draw(self, ax):
        # transformation_matrix_all = fkAllJoints(self.dh_array)
        i = 0
        p_a = self.transformation_matrix_all[i, 0:3, 3]
        for i in range(self.transformation_matrix_all.shape[0]):
            gl.draw3D(ax, 'trans', self.transformation_matrix_all[i])
            if i > 0:
                p_b = self.transformation_matrix_all[i, 0:3, 3]
                gl.draw3D(ax, 'arrow', p_b-p_a, position=p_a, color='k')
                p_a = p_b


class RobotPuma560:
    pass
