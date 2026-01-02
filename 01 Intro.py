import pandas as pd

print(pd.__version__)

# Series = A Pandas 1-Dimensional labeled array that can hold any data type.
# It like one column spreadsheet
data = [100,102,104]
series = pd.Series(data)
print(series)