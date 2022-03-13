import numpy as np
import matplotlib.pyplot as plt
import sys
import os

libs_path = os.path.dirname(os.path.dirname(__file__)) + '/libs'
sys.path.append(libs_path)
libs_path = os.path.dirname(os.path.dirname(
    os.path.dirname(__file__))) + '/math'
sys.path.append(libs_path)

import mathlib as ml
import graphiclib as gl