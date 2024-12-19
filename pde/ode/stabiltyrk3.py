import numpy as np
import matplotlib.pyplot as plt

# Define the center and radius of the circle
center = -1 + 0j  # Center of the circle in the complex plane (z = -1)
epsilon = 1     # Radius of the region where |1 + z| < epsilon

# Generate a grid of points in the complex plane
x = np.linspace(-4, 4, 1000)  # Real axis range
y = np.linspace(-4, 4, 1000)  # Imaginary axis range
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y  # Create the complex grid

# Calculate the magnitude of (1 + z)
magnitude = np.abs(1 + Z + (Z**2)/2 + (Z**3)/6 )

# Plot the region where |1 + z| < epsilon
plt.figure(figsize=(6, 6))
plt.contourf(X, Y, magnitude, levels=[0, epsilon], colors='blue', alpha=0.5)

# Plot the center of the circle (z = -1)
plt.plot(-1, 0, 'ro', label="z = -1")

# Set plot limits and labels
#plt.xlim([-2, 0])
#plt.ylim([-0.5, 0.5])
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.gca().set_aspect('equal', adjustable='box')

plt.title(f"Region where $|1+z| < {epsilon}$")
plt.xlabel("Real Part")
plt.ylabel("Imaginary Part")
plt.legend()

# Show the plot
plt.grid(True)
plt.savefig("rk3.pdf")
plt.show()
