import numpy as np
import roboticlib_path
import roboticlib as rl
import matplotlib.pyplot as plt
import graphiclib_path
import graphiclib as gl

puma = rl.RobotPuma560()
puma.angles([10, 20, 30, 0, 0, 0])

# Display contents
# fig = plt.figure()
# ax = plt.axes(projection='3d')
# puma.draw_puma(ax)
# gl.setAxesEqual3D(ax)
# plt.show()

result = puma.inverse_kinematics(puma.transformation_matrix_all[-1,:,:])
print(result)

temp = puma.transformation_matrix_all[-1,:,:]
trans_matrix_desired = np.identity(4)
trans_matrix_desired[:3,:3] = rl.rotation_matrix_x(180)
trans_matrix_desired[:3,3] = temp[:3,3]
x_start = 4
x_delta = 1
position_desired_0 = np.array(temp[:3,3])
position_desired_0[0] = x_start

fig = plt.figure()
ax = plt.axes(projection='3d')
for i in range(100):    
    trans_matrix_desired[0,3] = x_start + i/100.0 * x_delta
    joint_angles = puma.inverse_kinematics(trans_matrix_desired)
    puma.angles([joint_angles[0], joint_angles[1], joint_angles[2], 0, 0, 0])
    plt.cla()
    ax.plot([0, 0], [-3, 3], 'gray')
    ax.plot([-3, 3], [0, 0], 'gray')
    # puma.draw(ax)
    puma.draw_puma(ax)
    gl.drawArrow3D(ax, [x_delta, 0, 0], position_desired_0, color='gray')
    ax.set(xlim=(4, 6), ylim=(1, 2), zlim=(2, 3))
    gl.setAxesEqual3D(ax)
    # ax.view_init(elev=90, azim=-90)
    ax.view_init(elev=32, azim=-55)
    plt.pause(0.03)
    # FIXME: The is a position error outside the home positioin! x: d 4.99 act 5.053329186599401
    print('x: d', trans_matrix_desired[0,3], 'act', puma.transformation_matrix_all[-1,0,3])
    
    
plt.show()

