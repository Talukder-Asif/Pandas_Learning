import pandas as pd

# Data cleaning is the process of fixing/removing incomplete, incorrect or irrelevant data.

df = pd.read_csv("Pokemon.csv")
df = df.drop(columns=["#", "Total", "Generation"])

# Handle missing data
# 1. using dropna() = drop not available to remove null value rows
#df = df.dropna(subset=["Type 2"])
# 2. using fillna() = fill not available to fill null value
#df = df.fillna({"Type 2": "None"})

# Fix inconsistent values
#df["Type 1"] = df["Type 1"].replace({"Grass" : "GRASS"})

# Standardize text
#df["Name"] = df["Name"].str.lower()

# Remove Duplicate data
df = df.drop_duplicates()

print(df)