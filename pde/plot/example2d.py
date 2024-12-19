import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function f(x, y)
def f(x, y):
    return np.sin(2 * np.pi * x) * np.sin(2 * np.pi * y)

# Define the grid size and domain
grid_size = 1000
x = np.linspace(-1, 1, grid_size)
y = np.linspace(-1, 1, grid_size)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# 1. Contour Plot
plt.figure(figsize=(8, 6))
contour = plt.contour(X, Y, Z, levels = 30)
plt.colorbar(contour)
plt.title(r"Contour Plot of $f(x, y) = \sin(2\pi x) \sin(2\pi y)$")  # Use raw string (r"")
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('contour_plot.pdf')  # Save as .pdf
plt.close()

# 2. Heatmap Plot
plt.figure(figsize=(8, 6))
heatmap = plt.imshow(Z, extent=[-1, 1, -1, 1], origin='lower', cmap='viridis', aspect='auto')
plt.colorbar(heatmap)
plt.title(r"Heatmap of $f(x, y) = \sin(2\pi x) \sin(2\pi y)$")  # Use raw string (r"")
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('heatmap_plot.pdf')  # Save as .pdf
plt.close()

# 3. Surface Plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
ax.set_title(r"Surface Plot of $f(x, y) = \sin(2\pi x) \sin(2\pi y)$")  # Use raw string (r"")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
plt.savefig('surface_plot.pdf')  # Save as .pdf
plt.close()


print("All plots saved as .pdf files!")
