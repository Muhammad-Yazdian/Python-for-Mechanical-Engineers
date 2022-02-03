"""Graphical tools for drawing 2D and 3D vector, frames, and more.
    
    For more advanced plots one can use PyQtGraph
        - https://www.pyqtgraph.org/
  """
# By Seied Muhammad Yazdian | Feb 1s, 2022
# TODO: Add PyQTGraph https://www.pyqtgraph.org/
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d, Axes3D

def drawArrow(ax, vector, position, *args, **kwargs):
    """Draw a 2D arrow on xy plane
    
      Args:
        - ax (matplotlib.axes): an axes to draw the item on
        - position (numpy.ndarray): Start position (2x1, 3x1, or nx1)
        - vector (numpy.ndarray): Vector (2x1, 3x1, or nx1)"""
    color = kwargs.get('color')
    if color is None:
        color = 'k'
    # FIXME: To solve the auto zoom issue with quiver, I put two frames on top
    # of each other. The first part can be removed if you can find a better
    # solution for auto zooming of quiver
    ax.plot([position[0], position[0] + vector[0]], 
            [position[1], position[1] + vector[1]], 
            color=color)
    ax.quiver(position[0], position[1], 
              vector[0], vector[1],
              scale=1, scale_units='xy', angles='xy', color=color)

def drawFrame(ax, frame, position, *args, **kwargs):
    """Draw a 2D frame on xy plane
    
      Args:
        - ax (matplotlib.axes): an axes to draw the item on
        - frame (numpy.ndarray): 2x2, 3x3, or nxn rotation matrix (only xy elemets are used)
        - position (numpy.ndarray): 2x1, 3x1, or nx1 position vector (only xy element are used)"""
    color = kwargs.get('color')
    if color is None:
        color = ['r', 'g']
    # FIXME: To solve the auto zoom issue with quiver, I put two frames on top
    # of each other. The first part can be removed if you can find a better
    # solution for auto zooming of quiver
    ax.plot([position[0], position[0]+frame[0,0]], 
            [position[1], position[1]+frame[1,0]], 
            color=color[0])
    ax.plot([position[0], position[0]+frame[0,1]], 
            [position[1], position[1]+frame[1,1]],
            color=color[1])
    origin = np.array([[position[0], position[0]],[position[1], position[1]]])
    ax.quiver(*origin, frame[0, 0:2], frame[1, 0:2],
              scale=1, scale_units='xy', angles='xy', color=color)


class Arrow3D(FancyArrowPatch):
    """Constructs a 3D arrow based on matplotlib's FancyArrowPatch

      Author(s):

      - tacaswell, 2021 @ https://github.com/matplotlib/matplotlib/issues/21688"""
        
    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        """3D draw method"""
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)
    
    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        return np.min(zs)


def setAxesEqual3D(ax):
    """Make axes of 3D plot have equal scale so that spheres appear as spheres,
      cubes as cubes, etc..  This is one possible solution to Matplotlib's
      ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

      Author(s):

        - Karlo (2015) and Trenton McKinney (2021) @ https://stackoverflow.com/questions/13685386/matplotlib-equal-unit-length-with-equal-aspect-ratio-z-axis-is-not-equal-to

      Args:
        - ax: a matplotlib axis (e.g., plt.gca())
      """
    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5*max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])


def draw3D(ax, item_cat, item, *args, **kwargs):
    """Displays a generic object

      Args:
        - ax (matplotlib.axes._subplots.Axes3DSubplot): an axes to draw the item on
        - item_cat (str): Select a category: "point", "arrow", of "frame" 
        - item (numpy.ndarray): The item to be drawn on ax

      Returns:
        None

      Note: 
        -It is required to setup a figure before calling draw() function."""
    position = kwargs.get('position')
    color = kwargs.get('color')
    show_axis = kwargs.get('show_axis')

    if item_cat == "point": 
        drawPoint3D(ax, item, color)
    elif item_cat == "arrow":
        drawArrow3D(ax, item, position, color)
    elif item_cat == "frame":
        drawFrame3D(ax, item, position, show_axis=show_axis)
    elif item_cat == "trans":
        drawTransformationMatrix3D(ax, item)


def drawPoint3D(ax, vector, color):
    """Displays a 3D point indicated by a vector relative to origin of ax"""
    ax.plot(vector[0], vector[1], vector[2], 'o', color=color)


def drawArrow3D(ax, vector, position, color):
    """Displays a 3D vector at a given position"""
    a = position
    b = position + vector
    # A standard line plot behind the Arrow3D.
    # It is required to pass as ax when using set_axes_equal(ax)
    # Add the arrow with a triangle at the tip
    ax.plot((a[0], b[0]), (a[1], b[1]), (a[2], b[2]), color=color)
    arrow = Arrow3D((a[0], b[0]), (a[1], b[1]), (a[2], b[2]), mutation_scale=15,
                lw=1, arrowstyle="-|>", color=color)
    ax.add_artist(arrow)


def drawFrame3D(ax, frame, position, *args, **kwargs):
    """Displays a 3D frame (i.e., rotation matrix) at a given position
      The frame is right-handed and color-coded:
    
      - Red axis: :math:`\hat{x}`
      - Green axis: :math:`\hat{y}`
      - Blue axis: :math:`\hat{z}`"""
    show_axis = kwargs.get('show_axis')
    if show_axis is None:
        show_axis = np.array([1,1,1])
    if show_axis[0]:
        drawArrow3D(ax, frame[:,0], position, 'r')
    if show_axis[1]:
        drawArrow3D(ax, frame[:,1], position, 'g')
    if show_axis[2]:
        drawArrow3D(ax, frame[:,2], position, 'b')


def drawTransformationMatrix3D(ax, transformation_matrix):
    """Draw a 4x4 transformation matrix using its orientation (R) and position (p)"""
    drawFrame3D(
        ax, transformation_matrix[0:3, 0:3], transformation_matrix[0:3, 3])
