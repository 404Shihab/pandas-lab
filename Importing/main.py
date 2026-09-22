import pandas as pd

#  CSV = Comma-separated values
#  JSON = JavaScript Object Notation

df = pd.read_csv("Importing/data.csv")

print(df)

print(df.to_string())  # print all rows

