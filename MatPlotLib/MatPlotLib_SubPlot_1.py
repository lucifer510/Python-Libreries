import numpy as np
import matplotlib.pyplot as plt

# Compute the x and y coordinates for points on sine and cosine curves
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)

# Set up a subplot grid that has height 2 and width 1,
# and set the first such subplot as active.
plt.subplot(3,1,1)

# Make the first plot
plt.plot(x, y_sin,color='magenta', linestyle='dashdot')
plt.title('Sine')

# Set the second subplot as active, and make the second plot.
plt.subplot(3, 1, 2)
plt.plot(x, y_cos)
plt.grid(True)
plt.title('Cosine')

# Set the Third subplot as active, and make the second plot.
plt.subplot(3, 1, 3)
plt.plot(x, y_tan, color='Black', linestyle=':')
plt.title('Tangent')
# Show the figure.
plt.show()