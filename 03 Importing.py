import pandas as pd

#Read a CSV Data
df = pd.read_csv("Pokemon.csv")
print(df)

# To show all data
print(df.to_string())

#Print data based on filtering
print(df[df.Legendary == True].to_string())


