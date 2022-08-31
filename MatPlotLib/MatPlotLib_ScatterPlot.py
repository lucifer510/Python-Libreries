import matplotlib.pyplot as plt
import numpy as np

# Making Random Number Arrays For Plot Generation.
x = np.random.randint(10,100,10,int)
y = np.random.randint(20,200,10,int)
z = np.random.randint(30,300,10,int)

# Making The Plot
plt.scatter(x, y, marker="*", c="black", s=100)
plt.scatter(x, z, marker=".", c="red", s=100)
plt.legend(['x vs y','x vs z'])
plt.xlabel("X Values")
plt.ylabel("Y And Z Values")
plt.title("X Vs Y & X Vs Z - ScatterPlot")

# Show Figure
plt.show()
