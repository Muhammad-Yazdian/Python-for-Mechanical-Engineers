import roboticlib_path
import roboticlib as rl
import matplotlib.pyplot as plt
import graphiclib_path
import graphiclib as gl

puma = rl.RobotPuma560()
puma.angles([0, -40, 40, 0, 0, 0])

# Display contents
fig = plt.figure()
ax = plt.axes(projection='3d')
puma.draw(ax)
# gl.draw3D(ax, 'point', endeffector_position, color='c')  # Optional
gl.setAxesEqual3D(ax)
plt.show()
