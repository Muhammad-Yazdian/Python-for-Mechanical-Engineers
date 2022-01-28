import numpy as np
import matplotlib.pyplot as plt
import graphiclib_path as gl
import graphiclib as gl

a = gl.Point(0, 0, 0)
b = gl.Point(3, 0, 0)
c = gl.Point(3, 3, 0)
d = gl.Point(3, 3, 1)

arrow_1 = gl.Arrow(a, b, 'k')
arrow_2 = gl.Arrow(b, c, 'g')
arrow_3 = gl.Arrow(a, c, 'b')
arrow_tool = gl.Arrow(b, d, 'r')

fig = plt.figure()
ax = plt.axes(projection='3d')
plt.xlim(-1, 4)
plt.ylim(-1, 4)
# plt.zlim(-3, 3) # Not supported.
ax.set_aspect('auto', 'box') # 'equal is not supported'

arrow_1.draw(ax)
arrow_2.draw(ax)
arrow_3.draw(ax)
arrow_tool.draw(ax)

plt.show()
