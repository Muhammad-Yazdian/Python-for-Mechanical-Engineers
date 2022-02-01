# Add libs to system path
import sys
import os
libs_path = os.path.dirname(os.path.dirname(
    os.path.dirname(__file__))) + '/math'
sys.path.append(libs_path)
