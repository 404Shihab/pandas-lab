import pandas as pd

# aggregate functions = Reduces a set of values into a single summary value
#                       Used to summarize and analyze data
#                       Often used with the groupby() function


df = pd.read_csv("Aggregation/data.csv")

print(df.to_string())