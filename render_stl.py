import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot as plt
import os

# Specify path for the new folder
desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
folder = "images"
path = os.path.join(desktop, folder)

# Create new folder if it doesn't already exist
if not os.path.exists(path):
    os.makedirs(path)

# Load the STL files
your_mesh = mesh.Mesh.from_file('1.stl')

# Create a new plot
figure = plt.figure()
axes = mplot3d.Axes3D(figure)

# Render the STL mesh
poly = mplot3d.art3d.Poly3DCollection(your_mesh.vectors, linewidths=0.05, alpha=1, edgecolors='r')

# Make the object green
poly.set_facecolor((0,1,0))

axes.add_collection3d(poly)

# Auto scale to the mesh size
scale = your_mesh.points.flatten(None)
axes.auto_scale_xyz(scale, scale, scale)

# Set the background color to white
axes.set_facecolor((1,1,1))

# Hide the axes
axes.set_axis_off()

# Save the plot to the new folder
plt.savefig(os.path.join(path, 'your_image.png'), bbox_inches='tight', pad_inches=0, transparent=True)
