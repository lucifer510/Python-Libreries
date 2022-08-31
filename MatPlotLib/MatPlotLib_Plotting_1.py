import matplotlib.pyplot as plt
import numpy as np

# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
z = np.cos(x)
# Plot the points using matplotlib
plt.plot(x, y)
plt.plot(x, z)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])
plt.show()  # You must call plt.show() to make graphics appear.
