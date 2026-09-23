import pandas as pd

# aggregate functions = Reduces a set of values into a single summary value
#                       Used to summarize and analyze data
#                       Often used with the groupby() function


df = pd.read_csv("Aggregation/data.csv")

# print(df.to_string())

# --- whole data frame ----

print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))
print(df.count())


# --- Single column ---

print(df["Age"].mean())
print(df["StrikeRate"].min())
print(df["Runs"].max())
print(df["Matches"].count())

# ---groupby() ---

group = df.groupby("Country")
print(group["Runs"].mean())
print(group["Runs"].sum())
print(group["Wickets"].min())
print(group["Wickets"].max())
print(group["Matches"].count())