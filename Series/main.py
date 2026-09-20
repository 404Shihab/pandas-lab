import pandas as pd


# Series = A Pandas 1 Dimensional labeled array that can hold any data type

#           Think of it like a single column in a spreadsheet (1-Dimensional)


data = [100,200,300]

series = pd.Series(data) # here Series() is constructor

print(series) # 0    100
              # 1    200
              # 2    300
             # dtype: int64

data2 = ["A","B","C"]
series2 = pd.Series(data2)
print(series2) # 0    A
               # 1    B
               # 2    C
               # dtype: str

data3 = [True, False, True]
series3 = pd.Series(data3, index=["a","b","c"])  # custom indexing 
print(series3) # a     True
              #  b    False
              #  c     True
              #  dtype: bool

print(series3.loc["a"]) # True

print(series3.loc['b']) # False

data4 = [101,102,102]
series4 = pd.Series(data4, index=["A","B","C"])

series4.loc["B"] = 555

print(series4) # A    101
               # B    555
               # C    102
               # dtype: int64

print(series4.iloc[2]) # 102    - iloc = integer location


data5 = [122,455,677,100,201]
series5 = pd.Series(data5, index=["a","b","c","d","e"])
print(series5[series5 >= 200]) # b    455
                               # c    677
                               # e    201

# ------------------------------

calories = {"Day 1": 1750, "Day 2":2100, "Day 3":1750}
series6 = pd.Series(calories)
print(series6) # Day 1    1750
               # Day 2    2100
               # Day 3    1750
               # dtype: int64

series6.loc["Day 2"] += 400

print(series6.loc["Day 2"]) # 2500

print(series6) # Day 1    1750
               # Day 2    2500
               # Day 3    1750
               # dtype: int64

print(series6[series6 >= 2000]) # Day 2    2500
                                # dtype: int64