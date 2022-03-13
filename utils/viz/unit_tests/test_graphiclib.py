#=========================================================
# test_01.py
#
# Unit test for math and graphic libraries
#
# Author(s):
#   Seied Muhammad Yazdian
#
# Last update:
#   Mar 12, 2022
#=========================================================

from library_list import np, plt, ml, gl

point_1 = np.array([1.5, 2.5])
point_2 = np.array([2.5, 5.4])
frame_1 = ml.rotation_matrix_z(10)


def test_draw_arrow_2d():
    fig = plt.figure()
    ax = plt.axes()
    gl.draw_arrow_2d(ax, point_1, point_2, color='r')
    # assert


def test_draw_frame_2d():
    fig = plt.figure()
    ax = plt.axes()
    gl.draw_frame_2d(ax, frame_1, point_1, color=['k', 'r'])
    # assert


def test_draw_generic_3d():
    point = np.array([0.1, 0.2, 0.3])
    vector = np.array([1.1, 1.2, 1.3])
    frame = ml.rotation_matrix_z(10)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    gl.draw_generic_3d(ax, 'point', point, color='k')
    gl.draw_generic_3d(ax, 'arrow', vector, position=point, color='r')
    gl.draw_generic_3d(ax, 'frame', frame, position=point)
    gl.draw_generic_3d(ax, 'frame', frame, position=point, show_axis=(1, 0, 1))
    gl.set_axes_equal_3d(ax)


def test_draw_arrow_3d():
    position = np.array([1, 1, 0])
    vector = np.array([1, 1, 2])
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    gl.draw_arrow_3d(ax, vector, position, 'k')
    gl.set_axes_equal_3d(ax)


def test_draw_circle_3d():
    circle_radius = 3
    circle_position = np.array([1, 1, 0])
    circle_normal = np.array([1, 1, 2])
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    gl.draw_circle_3d(ax, circle_position, circle_normal, circle_radius, 'r')
    gl.set_axes_equal_3d(ax)


def test_draw_arrow_between_3d():
    a = np.array([1, 1, 0])
    b = np.array([1, 1, 2])
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    gl.draw_arrow_between_3d(ax, a, b, 'r')

    
def test_draw_trans_matrix_3d():
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    gl.draw_trans_matrix_3d(ax, np.identity(4))


def test_find_axis_by_two_vectors_and_angles():
    vector_1 = np.array([1, 0, 0])
    vector_2 = np.array([0, 1, 0])
    angle_1 = np.pi/3
    angle_2 = np.pi/3
    intersection = ml.find_axis_by_two_vectors_and_angles(
        vector_1, angle_1, vector_2, angle_2)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    gl.draw_generic_3d(ax, 'arrow', vector_1, position=[0,0,0], color='r')
    gl.draw_generic_3d(ax, 'arrow', vector_2, position=[0,0,0], color='g')
    gl.draw_generic_3d(ax, 'arrow', intersection, position=[0,0,0], color='b')
    gl.set_axes_equal_3d(ax)
    # plt.show()
