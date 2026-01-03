import pandas as pd

# aggregate function = Reduces a set of values into single summary value
# use to summarize and analyze data
# Often used with groupby() function

df = pd.read_csv("Pokemon.csv")

# Hole dataframe
# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())


#Single Column
#print(df["Total"].mean()
#print(df["Total"].sum()
# print(df["Total"].min()
# print(df["Total"].max()
# print(df["Total"].count())

group = df.groupby("Type 1")

print(group["HP"].mean())
print(group["HP"].sum())
print(group["HP"].min())
print(group["HP"].max())
print(group["HP"].count())