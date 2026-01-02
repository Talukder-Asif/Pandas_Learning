import pandas as pd

print(pd.__version__)

# Series = A Pandas 1-Dimensional labeled array that can hold any data type.
# It like one column spreadsheet
data = [100, 102, 104, 200, 202]
series = pd.Series(data)
print(series)

#Change Index of the series
series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
print("\nUsing custom index ->")
print(series)

#select a value using index  && loc means location
print("\nValue of index c =", series.loc["c"])

#change the value of a index
series.loc["c"]=201

print("\nAfter update")
print(series)

#select a value using index  && iloc means integer location
print("\nValue of 2nd integer =", series.iloc[1])

#Return a value that is more than 200
print(series[series > 200])

#We did not need to add index in python Dictionary
calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}
series = pd.Series (calories)
print(series)