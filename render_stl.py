import numpy as np
from stl import mesh
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import os

# Specify path for the new folder
desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
folder = "images"
path = os.path.join(desktop, folder)

# Create new folder if it doesn't already exist
if not os.path.exists(path):
    os.makedirs(path)

# Load the STL files
your_mesh = mesh.Mesh.from_file('your_stl_file.stl')

# Create a new plot
figure = plt.figure()
axes = Axes3D(figure)

# Render the STL mesh
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

# Auto scale the rendering
scale = your_mesh.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)

# Save the plot to the new folder
plt.savefig(os.path.join(path, 'your_image.png'))
