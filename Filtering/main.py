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

barcelona_midfielders = df[(df["Club"]== "Barcelona") &
                          (df["Position"] == "Midfielder") ]

print(barcelona_midfielders)

england_or_forward = df[(df["Country"]== "England") |
                          (df["Position"] == "Forward") ]


print(england_or_forward)
