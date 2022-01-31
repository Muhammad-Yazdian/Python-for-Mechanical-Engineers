"""Graphical library provides tools for displaying 3D vector, frames, and more.
  
    Seied Muhammad Yazdian | Jan 29, 2022

    muhammad.yazdian@gmail.com"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d, Axes3D


class Arrow3D(FancyArrowPatch):
    """Construct a 3D arrow based on matplotlib's FancyArrowPatch

      More information:
        https://stackoverflow.com/questions/11140163/plotting-a-3d-cube-a-sphere-and-a-vector-in-matplotlib"""
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)


def set_axes_equal(ax):
    '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
      cubes as cubes, etc..  This is one possible solution to Matplotlib's
      ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

      Input:
        ax: a matplotlib axis, e.g., as output from plt.gca().
    
      Author(s): 
        - Karlo (2015) and Trenton McKinney (2021)

      Source:
        https://stackoverflow.com/questions/13685386/matplotlib-equal-unit-length-with-equal-aspect-ratio-z-axis-is-not-equal-to'''
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


def draw(ax, item_cat, item, *args, **kwargs):
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
        drawPoint(ax, item, color)
    elif item_cat == "arrow":
        drawArrow(ax, item, position, color)
    elif item_cat == "frame":
        drawFrame(ax, item, position, show_axis=show_axis)
    elif item_cat == "trans":
        drawTransformationMatrix(ax, item)


def drawPoint(ax, vector, color):
    """Displays a 3D point indicated by a vector relative to origin of ax"""
    ax.plot(vector[0], vector[1], vector[2], 'o', color=color)


def drawArrow(ax, vector, position, color):
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


def drawFrame(ax, frame, position, *args, **kwargs):
    """Displays a 3D frame (i.e., rotation matrix) at a given position
      The frame is right-handed and color-coded:
    
      - Red axis: :math:`\hat{x}`
      - Green axis: :math:`\hat{y}`
      - Blue axis: :math:`\hat{z}`"""
    show_axis = kwargs.get('show_axis')
    if show_axis is None:
        show_axis = np.array([1,1,1])
    if show_axis[0]:
        drawArrow(ax, frame[:,0], position, 'r')
    if show_axis[1]:
        drawArrow(ax, frame[:,1], position, 'g')
    if show_axis[2]:
        drawArrow(ax, frame[:,2], position, 'b')

def drawTransformationMatrix(ax, transformation_matrix):
    drawFrame(ax, transformation_matrix[0:3,0:3], transformation_matrix[0:3,3])