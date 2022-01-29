import sys
import roboticlib_path
import roboticlib as rl

theta = float(0)
a = rl.rotatoinMatixX(theta)
print('Rx = \n', a)

theta = float(30)
a = rl.rotatoinMatixX(theta)
print('Rx = \n', a)
