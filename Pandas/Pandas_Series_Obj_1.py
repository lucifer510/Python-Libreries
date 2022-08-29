import pandas as pd

# Creating Series Object
s1 = pd.Series([1, 2, 3, 4, 5])

print(s1)  # Prints "0    1
#                    1    2
#                    2    3
#                    3    4
#                    4    5
#                    dtype: int64"

# Customize The Index
s2 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s2)  # Prints "a    1
#                    b    2
#                    c    3
#                    d    4
#                    e    5
#                   dtype: int64"

# Series Object As Dictionary
s3 = pd.Series({'k1': 10, 'k2': 20, 'k3': 30})
print(s3)  # Prints "k1    10
#                    k2    20
#                    k3    30
#                    dtype: int64"

# Changing Index Position
s4 = pd.Series({'k1': 10, 'k2': 20, 'k3': 30}, index=['k3', 'k1', 'k4', 'k2'])
print(s4)  # Prints "k3    30.0
#                    k1    10.0
#                    k4     NaN
#                    k2    20.0
#                    dtype: float64"

# Extracting Individual Elements
s5 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(s5[4])  # Prints "5"
print(s5[:5])  # Prints "0    1
#                        1    2
#                        2    3
#                        3    4
#                        4    5
#                        dtype: int64"
print(s5[-5:])  # Prints "4    5
#                         5    6
#                         6    7
#                         7    8
#                         8    9
#                         dtype: int64"