import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define control points and knot vectors
control_points = [
    [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (2.0, 0.0, 0.0)],
    [(0.0, 1.0, 0.0), (1.0, 1.0, 1.0), (2.0, 1.0, 0.0)],
    [(0.0, 2.0, 0.0), (1.0, 2.0, 0.0), (2.0, 2.0, 0.0)]
]

# Create parameter values for u and v directions
u = np.linspace(0, 1, len(control_points))
v = np.linspace(0, 1, len(control_points[0]))

# Generate surface points using bilinear interpolation
surface_points = np.zeros((len(u), len(v), 3))
for i, ui in enumerate(u):
    for j, vj in enumerate(v):
        x = np.sum([control_points[m][n][0] * (1 - ui) * (1 - vj) for m in range(len(control_points)) for n in range(len(control_points[0]))])
        y = np.sum([control_points[m][n][1] * (1 - ui) * (1 - vj) for m in range(len(control_points)) for n in range(len(control_points[0]))])
        z = np.sum([control_points[m][n][2] * (1 - ui) * (1 - vj) for m in range(len(control_points)) for n in range(len(control_points[0]))])
        surface_points[i, j] = [x, y, z]

# Extract x, y, and z coordinates
x = surface_points[:, :, 0]
y = surface_points[:, :, 1]
z = surface_points[:, :, 2]

# Define colormap
cmap = 'tab20c_r'  # You can change the colormap here

# Visualize the surface with colormap
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap=cmap)
plt.show()
