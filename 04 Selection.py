import pandas as pd

df = pd.read_csv("Pokemon.csv")

#Selection by column
print(df["Name"])

print(df[["Name", "Type 1", "Attack", "Defense", "Speed"]])

# selection by rows
print(df.loc[10])

#We can give index as any column in data read
DF = pd.read_csv("Pokemon.csv", index_col="Name")
print(DF)

print(DF.loc["Pikachu"])

# We can also show limited info
print(DF.loc["Charizard", ["Type 1", "HP", "Attack", "Defense"]])

# We can select multiple rows ->
print(DF.loc["Pikachu" : "Doduo" ])

#We can select rows and columns at once
print(DF.iloc[0 : 11, 1:])