import numpy as np
from stl import mesh
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Load the STL file
your_mesh = mesh.Mesh.from_file('your_stl_file.stl')

# Create a new plot
figure = plt.figure()
axes = mplot3d.Axes3D(figure)

# Render the STL mesh
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

# Auto scale the rendering
scale = your_mesh.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)

# Show the plot and save the image
plt.savefig('your_image.png')
