"""Graphical library provides tools for displaying 3D vector, frames, and more.
  
  Seied Muhammad Yazdian | Jan 29, 2022

  muhammad.yazdian@gmail.com"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d, Axes3D


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


class Point3d:
    """A 3D position point relative to origin (based on NumPy)"""

    def __init__(self, x, y, z):
        self.values = np.array([float(x), float(y), float(z)])

    def __getitem__(self, i):
        """Makes the object substricptable; aka Position3d[0], ..."""
        return self.values[i]

    # Addition is not meaningful for Points    
    # def __add__(self, other):
    #     """Overloading + operator"""
    #     sum_value = self.values + other.values
    #     return Point(sum_value[0], sum_value[1], sum_value[2])

class Vector3d:
    """A 3D free vector without any origin (based on NumPy)"""

    def __init__(self, dx, dy, dz):
        self.values = np.array([float(dx), float(dy), float(dz)])

    def __getitem__(self, i):
        """Makes the object substricptable; aka Position3d[0], ..."""
        return self.values[i]

    def __add__(self, other):
        """Overloading + operator"""
        result = self.values + other.values
        # TODO: Use function overloading
        return Vector3d(result[0], result[1], result[2])

    def __sub__(self, other):
        """Overloading - operator"""
        result = self.values - other.values
        return Vector3d(result[0], result[1], result[2])

    def dot(self, other):
        """Inner dot product"""
        return np.inner(self.values, other.values)

    def cross(self, other):
        """Outer cross product"""
        result = np.cross(self.values, other.values)
        return Vector3d(result[0], result[1], result[2])


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


class Arrow3D2:
    """Constructs a graphical 3D arrow"""

    def __init__(self, start, end, ax, color='k'):
        """Note: Setup a figure before calling draw() function."""
        self.start = start
        self.end = end
        self.color = color
        self.ax = ax
        # def draw(self, ax):
        s = self.start
        e = self.end
        # A standard line plot behind the Arrow3D.
        # It is required to pass as ax when using set_axes_equal(ax)
        # Add the arrow with a triangle at the tip
        ax.plot((s[0], e[0]), (s[1], e[1]), (s[2], e[2]), color=self.color)
        a = Arrow3D((s[0], e[0]), (s[1], e[1]), (s[2], e[2]), mutation_scale=15,
                    lw=1, arrowstyle="-|>", color=self.color)
        ax.add_artist(a)
        

class GraphicalFrame:
    """Constructs a graphical 3D frame (right-handed coordinate system)
    
      - Red axis: :math:`\hat{x}`
      - Green axis: :math:`\hat{y}`
      - Blue axis: :math:`\hat{z}`"""

    def __init__(self, ax, position, orientation=None):
        self.position = position
        self.orientation = np.identity(3)
        if orientation is None:
            self.orientation = np.identity(3)
        else:
            self.orientation = orientation
        
        # def draw(self, ax):
        p = self.position
        o = self.orientation
        Arrow3D2(p, (p[0]+o[0][0], p[1]+o[0][1], p[2]+o[0][2]), ax, 'r')
        Arrow3D2(p, (p[0]+o[1][0], p[1]+o[1][1], p[2]+o[1][2]), ax, 'g')
        Arrow3D2(p, (p[0]+o[2][0], p[1]+o[2][1], p[2]+o[2][2]), ax, 'b')