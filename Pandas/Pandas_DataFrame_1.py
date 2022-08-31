# it is 2D Labeled data Structure
import pandas as pd

df1 = pd.DataFrame({'Name': ['Mihir', 'Raj', 'Yashvi'], 'Marks': [99, 95, 98]})
print(df1)  # Prints "Name  Marks
#                0   Mihir     99
#                1     Raj     95
#                2  Yashvi     98"
print(type(df1))  # Prints "<class 'pandas.core.frame.DataFrame'>"

# Read Data From Excel .csv File
data = pd.read_csv(r"C:\Users\MIHIR\Desktop\marveldata.csv")
# To Print First N Records Of DataSet.
print(data.head(3))  # Prints "page_id                                 name  ... FIRST APPEARANCE    Year
#                            0     1678            Spider-Man (Peter Parker)  ...           Aug-62  1962.0
#                            1     7139      Captain America (Steven Rogers)  ...           Mar-41  1941.0
#                            2    64786  Wolverine (James \"Logan\" Howlett)  ...           Oct-74  1974.0 "

# To Print Last N Records Of DataSet.
print(data.tail(3))  # Prints "
#        page_id                            name  ... FIRST APPEARANCE Year
# 16373   695217   Tinkerer (Skrull) (Earth-616)  ...              NaN  NaN
# 16374   708811  TK421 (Spiderling) (Earth-616)  ...              NaN  NaN
# 16375   673702           Yologarch (Earth-616)  ...              NaN  NaN "

# To Get Number Of Rows And Columns
print(data.shape)  # Prints "(16376, 13)"

# To Get Basic Math Information Of Data
print(data.describe())  # Prints " page_id   APPEARANCES          Year
#                     count   16376.000000  15280.000000  15561.000000
#                     mean   300232.082377     17.033377   1984.951803
#                     std    253460.403399     96.372959     19.663571
#                     min      1025.000000      1.000000   1939.000000
#                     25%     28309.500000      1.000000   1974.000000
#                     50%    282578.000000      3.000000   1990.000000
#                     75%    509077.000000      8.000000   2000.000000
#                     max    755278.000000   4043.000000   2013.000000 "

# To Get Specific Rows And Columns
print(data.iloc[0:5, 6:10])  # Prints "  HAIR              SEX  GSM              ALIVE
#                              0  Brown Hair  Male Characters  NaN  Living Characters
#                              1  White Hair  Male Characters  NaN  Living Characters
#                              2  Black Hair  Male Characters  NaN  Living Characters
#                              3  Black Hair  Male Characters  NaN  Living Characters
#                              4  Blond Hair  Male Characters  NaN  Living Characters "

# To Print Including Both Index.
print(data.loc[1:5, ("name", "SEX", "ALIVE")])  # Prints " name              SEX              ALIVE
#                    1      Captain America (Steven Rogers)  Male Characters  Living Characters
#                    2  Wolverine (James \"Logan\" Howlett)  Male Characters  Living Characters
#                    3    Iron Man (Anthony \"Tony\" Stark)  Male Characters  Living Characters
#                    4                  Thor (Thor Odinson)  Male Characters  Living Characters
#                    5           Benjamin Grimm (Earth-616)  Male Characters  Living Characters"

# To Delete Columns From Data Set.
i2 = data.drop('urlslug', axis=1)
print(i2.head(5))  # Prints "  page_id                                 name  ... FIRST APPEARANCE    Year
#                           0     1678            Spider-Man (Peter Parker)  ...           Aug-62  1962.0
#                           1     7139      Captain America (Steven Rogers)  ...           Mar-41  1941.0
#                           2    64786  Wolverine (James \"Logan\" Howlett)  ...           Oct-74  1974.0
#                           3     1868    Iron Man (Anthony \"Tony\" Stark)  ...           Mar-63  1963.0
#                           4     2460                  Thor (Thor Odinson)  ...           Nov-50  1950.0
#
# [5 rows x 12 columns]

# To Delete Rows From Data Set.
i1 = data.drop([5, 6, 7], axis=0)
print(i1.head(10))  # Prints " page_id                                 name  ... FIRST APPEARANCE    Year


#                          0      1678            Spider-Man (Peter Parker)  ...           Aug-62  1962.0
#                          1      7139      Captain America (Steven Rogers)  ...           Mar-41  1941.0
#                          2     64786  Wolverine (James \"Logan\" Howlett)  ...           Oct-74  1974.0
#                          3      1868    Iron Man (Anthony \"Tony\" Stark)  ...           Mar-63  1963.0
#                          4      2460                  Thor (Thor Odinson)  ...           Nov-50  1950.0
#                          8     29481            Scott Summers (Earth-616)  ...           Sep-63  1963.0
#                          9      1837           Jonathan Storm (Earth-616)  ...           Nov-61  1961.0
#                          10    15725              Henry McCoy (Earth-616)  ...           Sep-63  1963.0
#                          11     1863              Susan Storm (Earth-616)  ...           Nov-61  1961.0
#                          12     7823           Namor McKenzie (Earth-616)  ...              NaN     NaN
#
# [10 rows x 13 columns]

def half(s):
    return s / 2


i3 = data[['APPEARANCES', 'Year']].apply(half)
print(i3)  # Prints "        APPEARANCES   Year
#                     0           2021.5  981.0
#                     1           1680.0  970.5
#                     2           1530.5  987.0
#                     3           1480.5  981.5
#                     4           1129.0  975.0
#                     ...            ...    ...
#                     16371          NaN    NaN
#                     16372          NaN    NaN
#                     16373          NaN    NaN
#                     16374          NaN    NaN
#                     16375          NaN    NaN

# To Get Number Of Occurrence Of category.
print(data['SEX'].value_counts())  # Prints " Male Characters           11638
#                                             Female Characters          3837
#                                             Agender Characters           45
#                                             Genderfluid Characters        2
#                                             Name: SEX, dtype: int64

# To Sort Values In Data.
print(data.sort_values(by='Year'))  # Prints "page_id                               name  ... FIRST APPEARANCE    Year
#                                      15281   645438  Mr. Harris' Secretary (Earth-616)  ...           Oct-39  1939.0
#                                      60        1836  Human Torch (Android) (Earth-616)  ...           Oct-39  1939.0
#                                      15282   331151                 N'Jaga (Earth-616)  ...           Oct-39  1939.0
#                                      10506   642960            Tim Roberts (Earth-616)  ...           Oct-39  1939.0
#                                      10505   727086    Tex (Masked Raider) (Earth-616)  ...           Dec-39  1939.0
#                                      ...        ...                                ...  ...              ...     ...
#                                      16371   657508                 Ru'ach (Earth-616)  ...              NaN     NaN
#                                      16372   665474    Thane (Thanos' son) (Earth-616)  ...              NaN     NaN
#                                      16373   695217      Tinkerer (Skrull) (Earth-616)  ...              NaN     NaN
#                                      16374   708811     TK421 (Spiderling) (Earth-616)  ...              NaN     NaN
#                                      16375   673702              Yologarch (Earth-616)  ...              NaN     NaN
