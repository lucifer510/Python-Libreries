# Basic Math Operation on Series Object
import pandas as pd

s1 = pd.Series([1, 2, 3])
print(s1 + 10)  # Prints "0    11
#                         1    12
#                         2    13
#                         dtype: int64
print(s1 - 100)  # Prints "0   -99
#                          1   -98
#                          2   -97
#                          dtype: int64"
print(s1 * 5)  # Prints "0     5
#                        1    10
#                        2    15
#                        dtype: int64"
print(s1 / 10)  # Prints "0    0.1
#                         1    0.2
#                         2    0.3
#                         dtype: float64"

s2 = pd.Series([4, 5, 6])
print(s1 + s2)  # Prints "0    5
#                         1    7
#                         2    9
#                         dtype: int64"
print(s1 - s2)  # Prints "0   -3
#                         1   -3
#                         2   -3
#                         dtype: int64"
print(s1 * s2)  # Prints "0     4
#                         1    10
#                         2    18
#                         dtype: int64"
print(s1 / s2)  # Prints "0    0.25
#                         1    0.40
#                         2    0.50
#                         dtype: float64"

