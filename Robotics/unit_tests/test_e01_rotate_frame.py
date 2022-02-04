#===============================================================================
# Tests roboticlib rotatoin matrices
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


def test_rotatoinMatices():
    # assert rl.rotatoinMatixX(0) == np.identity(3)
    answer = rl.rotatoinMatixX(0)
    key = np.identity(3)
    np.testing.assert_allclose(answer, key, rtol=1e-10, atol=1e-10)

    answer = rl.rotatoinMatixX(90)
    key = np.array([[1, 0, 0],
                    [0, 0, -1],
                    [0, 1, 0]])
    np.testing.assert_allclose(answer, key, rtol=1e-10, atol=1e-10)

    answer = rl.rotatoinMatixY(0)
    key = np.identity(3)
    np.testing.assert_allclose(answer, key, rtol=1e-10, atol=1e-10)

    answer = rl.rotatoinMatixY(90)
    key = np.array([[0, 0, 1],
                    [0, 1, 0],
                    [-1, 0, 0]])
    np.testing.assert_allclose(answer, key, rtol=1e-10, atol=1e-10)

    answer = rl.rotatoinMatixZ(0)
    key = np.identity(3)
    np.testing.assert_allclose(answer, key, rtol=1e-10, atol=1e-10)

    answer = rl.rotatoinMatixZ(90)
    key = np.array([[0, -1, 0],
                    [1, 0, 0],
                    [0, 0, 1]])
    np.testing.assert_allclose(answer, key, rtol=1e-10, atol=1e-10)
