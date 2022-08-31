import matplotlib.pyplot as plt

# Creating Dictionary..
student = {'Mihir': 99, 'Raj': 95, 'Yashvi': 98}
names = student.keys() # Store Keys As Names
marks = student.values() # Store Values As Marks

# Make The Bar Plot
plt.bar(names, marks)
plt.title("Distribution Of Students Marks")
plt.grid(True)
plt.xlabel("Names")
plt.ylabel("Marks")
# Show The Figure
plt.show()
