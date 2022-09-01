import matplotlib.pyplot as plt
import numpy as np

# Making the random array.
x = np.random.randint(1, 50, 20, int)

plt.hist(x, bins=20,color="black")  # Make the histogram plot.
plt.title("Histogram Plot") # Declare the title for the plot..
plt.xlabel("Value Of X") # The Value Of X into the plot.
plt.ylabel("Frequency Of X") # The Frequency Of X into the plot.
plt.grid(True) # Make the grid for the plotting.
plt.show()  # Show the histogram plot
