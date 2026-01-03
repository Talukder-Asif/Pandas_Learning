import pandas as pd

# Data Frames is a tabular data structure with rows and columns. (2D)

data = {"Name": ["Asif", "Atik", "Anik", "Siam"], "Age": [24, 21, 16, 14]}
df = pd.DataFrame(data)
print(df)

# we can give index also
print("\nwe can give index also ->")
df = pd.DataFrame(data, index= ["E1", "E2", "E3", "E4"])
print("\nwe can give index also ->")
print(df)

# To select a single one, we can use loc property
print('\n')
print(df.loc["E2"])

# To select a single one, we also can use iloc property
print('\n')
print(df.iloc[3])

# Add a new column
df["Job"] = ["Web Dev", "Phone Master", "Student", "Student"]

# Add a new row
new_row = pd.DataFrame([{'Name': "Rafin", "Age": 9, "Job": "Pora churi"},{'Name': "Raiyan", "Age": 1, "Job": "Army Officer"}], index=["E4", "E5"])
df = pd.concat([df, new_row])

print('\n')
print(df)

