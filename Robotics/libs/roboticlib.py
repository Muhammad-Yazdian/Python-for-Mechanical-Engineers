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
from numpy.linalg import inv
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

    def __init__(self, dh_param_file=None):
        self.dh_array = 0
        if dh_param_file:
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

      
    def set_dh(self):
        self.dh_array = 1

    
    def draw(self, ax):
        i = 0
        p_a = self.transformation_matrix_all[i, 0:3, 3]
        for i in range(self.transformation_matrix_all.shape[0]):
            gl.draw3D(ax, 'trans', self.transformation_matrix_all[i])
            if i > 0:
                p_b = self.transformation_matrix_all[i, 0:3, 3]
                gl.draw3D(ax, 'arrow', p_b-p_a, position=p_a, color='k')
                p_a = p_b


class RobotPuma560(Robot):

    def __init__(self):
        self.dh_array = np.array([[0.00,   6.60,   -90,   0.0],
                                  [4.32,   1.49,   0.0,   0.0],
                                  [0.20,   0.00,   -90,   0.0],
                                  [0.00,   4.32,   -90,   0.0],
                                  [0.00,   0.00,   90,    0.0],
                                  [0.00,   0.56,   0.0,   0.0]])

    def draw_puma(self, ax):
        """Draws the light version 3D plot of Puma 560

          Args:
            - ax (matplotlib axis): plot axis
          """
        i = 0
        p_a = self.transformation_matrix_all[i, 0:3, 3]
        for i in range(self.transformation_matrix_all.shape[0]):
            # gl.draw3D(ax, 'trans', self.transformation_matrix_all[i])
            if i > 0:
                p_b = self.transformation_matrix_all[i, 0:3, 3]
                if i != 2:
                    gl.draw3D(ax, 'arrow', p_b-p_a, position=p_a, color='k')
                else:
                    l1 = np.matmul(self.transformation_matrix_all[i-1, :3, :3], 
                                   [0, 0, self.dh_array[1, 1]])
                    l2 = np.matmul(self.transformation_matrix_all[i, :3, :3],
                                   [self.dh_array[1, 0], 0, 0])
                    gl.draw3D(ax, 'arrow', l1, position=p_a, color='r')
                    gl.draw3D(ax, 'arrow', l2, position=p_a + l1, color='r')
                p_a = p_b
        gl.draw3D(ax, 'trans', self.transformation_matrix_all[0])
        gl.draw3D(ax, 'trans', self.transformation_matrix_all[-1])


    def inverse_kinematics(self, trans_matrix_tip, hand='left', elbow='up', flip='no'):
        """Inverse kinematics of Puma robot

          Args:
            - trans_matrix_tip (ndarray): Transformation matrix of endeffector
            - hand (str, optional): Handedness. Defaults to 'left'.
            - elbow (str, optional): Elbow configuration. Defaults to 'up'.
            - flip (str, optional): Flip configuration. Defaults to 'no'.

          Returns:
            ndarray: Joint angles :math:`\theta_1, \theta_2, and theta_3`
          """
        dh = self.dh_array
        D1 = dh[0, 1] # It is always a positive constant (for Puma)
        D2 = dh[1, 1] # It is always a positive constant (for Puma)
        D4 = dh[3, 1] # It is always a positive constant (for Puma)
        A2 = dh[1, 0] # It is always a positive constant (for Puma)
        A3 = dh[2, 0] # It is always a positive constant (for Puma)
        D6 = dh[5, 1] # It is always a positive constant (for Puma)
        
        T56 = np.identity(4)
        # T56[:3,:3] = rotation_matrix_x(180)
        T56[2, 3] = D6
        T = np.matmul(trans_matrix_tip, inv(T56))
        x, y, z = T[:3, 3]

        # Compute theta1
        hyp0 = np.hypot(x, y)
        alpha1 = np.arcsin(D2/hyp0)
        phi1 = np.arctan2(y, x)
        theta1 = phi1 - alpha1
        if hand == 'right':
            theta1 = phi1 + alpha1 + np.pi
        
        # Compute theta2
        h1 = -(z - D1)
        phi2 = np.arctan2(h1, hyp0*np.cos(alpha1))
        hyp1 = np.hypot(h1, hyp0*np.cos(alpha1))
        hyp2 = np.hypot(A3, D4)
        alpha2 = np.arccos((A2**2 + hyp1**2 - hyp2**2)/(2*A2*hyp1))
        theta2 = phi2 - alpha2
        if elbow == 'down':
            theta2 = phi2 + alpha2
        
        # Compute theta2
        beta3 = np.arccos((A2**2 + hyp2**2 - hyp1**2)/(2*A2*hyp2))
        ALPHA3 = np.arccos(A3/hyp2)
        theta3 = np.pi - beta3 - ALPHA3

        return np.degrees([theta1, theta2, theta3])
