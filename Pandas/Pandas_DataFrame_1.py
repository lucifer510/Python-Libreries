# it is 2D Labeled data Structure
import pandas as pd

df1 = pd.DataFrame({'Name': ['Mihir', 'Raj', 'Yashvi'], 'Marks': [99, 95, 98]})
print(df1)  # Prints "Name  Marks
#                0   Mihir     99
#                1     Raj     95
#                2  Yashvi     98"
print(type(df1))  # Prints "<class 'pandas.core.frame.DataFrame'>"
