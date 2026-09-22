import pandas as pd
#  Filtering = Keeping the rows that match a condition

df = pd.read_csv("Filtering/data.csv")

tall_player = df[df["Height"] > 190]

print(tall_player)


heavy_player = df[df["Weight"] > 90]

print(heavy_player)

real_madrid_player = df[df["Club"] == "Real Madrid"]

print(real_madrid_player)

defenders = df[df["Position"] == "Defender"]

print(defenders)

