#===============================================================================
# Tests roboticlib rotation matrices
#
# Author(s):
#   Seied Muhammad Yazdian
#
# Last update:
#   Feb 4, 2022
#===============================================================================

import numpy as np
import os
import sys
libs_path = os.path.dirname(os.path.dirname(__file__)) + '/libs'
sys.path.append(libs_path)
import roboticlib as rl
# import unittest


def test_rotationMatices():
    # assert rl.rotation_matrix_x(0) == np.identity(3)
    answer = rl.rotation_matrix_x(0)
    key = np.identity(3)
    np.testing.assert_allclose(answer, key, rtol=1e-10, atol=1e-10)

    answer = rl.rotation_matrix_x(90)
    key = np.array([[1, 0, 0],
                    [0, 0, -1],
                    [0, 1, 0]])
    np.testing.assert_allclose(answer, key, rtol=1e-10, atol=1e-10)

    answer = rl.rotation_matrix_y(0)
    key = np.identity(3)
    np.testing.assert_allclose(answer, key, rtol=1e-10, atol=1e-10)

    answer = rl.rotation_matrix_y(90)
    key = np.array([[0, 0, 1],
                    [0, 1, 0],
                    [-1, 0, 0]])
    np.testing.assert_allclose(answer, key, rtol=1e-10, atol=1e-10)

    answer = rl.rotation_matrix_z(0)
    key = np.identity(3)
    np.testing.assert_allclose(answer, key, rtol=1e-10, atol=1e-10)

    answer = rl.rotation_matrix_z(90)
    key = np.array([[0, -1, 0],
                    [1, 0, 0],
                    [0, 0, 1]])
    np.testing.assert_allclose(answer, key, rtol=1e-10, atol=1e-10)
