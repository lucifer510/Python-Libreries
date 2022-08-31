# We Will Create Histogram for the csv file.
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(r"C:\Users\MIHIR\Desktop\marveldata.csv")
plt.hist(data[['Year']], bins=10, color="black")
plt.xlabel('Year') # Xlabel for the Histogram Plotting.
plt.ylabel("Number of Marvel Character In Each Year") # Y Label for the Histogram Plotting.
plt.title("Histogram for the csv file") # Title for the histogram plot.
plt.savefig(r"C:\Users\MIHIR\Desktop\marvelHistogram")
plt.show()  # Show the histogram plot.