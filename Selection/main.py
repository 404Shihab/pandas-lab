import pandas as pd

df = pd.read_csv("Importing/data.csv", index_col="Name")

# Selection by column

# print(df["Name"])
# print(df["Name"].to_string())  # to print entire row

# print(df[["Name","Weight","Height"]].to_string()) # multiple column 

# Selection by Row(s)

# print(df.loc[0])

print(df.loc["Pikachu"])

print(df.loc["Charizard",["Height","Weight"]])

print(df.iloc[0:11]) # second one is exclusive

print(df.iloc[3:12:2]) # every second row

print(df.iloc[4:14:2, 0:2])

# ------- EXERCISE --------


pokemon = input("Enter a pokemon name ")

try:
    print(df.loc[pokemon])

except KeyError:
    print(f"{pokemon} not found")