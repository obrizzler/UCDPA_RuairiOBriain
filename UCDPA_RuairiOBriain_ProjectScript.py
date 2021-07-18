# importing libraries (installed via Python Interpretter
# pandas - library for dataframe
import pandas as pd
# numpy - library for arrays
import numpy as np
# os to import dataframe
import os

# check current working directory (CWD)
print(os.getcwd())
# not necessary to change CWD (os.chdir(r"file_path")

# import .csv dataset
waiters_tips = pd.read_csv('waiter_tips.csv', encoding = 'ISO-8859-1')
# check type of imported dataset
waiters_tips_type = str(type(waiters_tips))
print("Waiters_tips is a: " + waiters_tips_type)

# examine the waiters_tips dataframe - Print a list of the column headers
column_headers = list(waiters_tips.columns)
print("Column Headers is a " + str(type(column_headers)))
for i in column_headers:
    print(i)
# (alternatively for i in waiters_tips.columns)

# examine the broader content & format of waiters_tips dataframe - view top 10 & bottom 5 rows
print(waiters_tips.head(10))
print(waiters_tips.tail())

# examine length and shape of waiters_tips dataframe
dataframe_length = str(len(waiters_tips))
dataframe_shape = str(waiters_tips.shape)
print("The waiters_tips dataframe is " + dataframe_length + " rows long.")
print("Its shape (rows,columns) is: " + dataframe_shape)

# examine data types of each column
print(waiters_tips.dtypes)

# examine level of the dataset that is the primary key
print("Total Bill: " + str(len(waiters_tips.total_bill.unique())))
print("Tip: " + str(len(waiters_tips.tip.unique())))
print("Sex: " + str(len(waiters_tips.sex.unique())))
print("Smoker: " + str(len(waiters_tips.smoker.unique())))
print("Day: " + str(len(waiters_tips.day.unique())))
print("Time: " + str(len(waiters_tips.time.unique())))

# display unique values in columns with < 10 unique values
print("Sex: ", waiters_tips.sex.unique())
print("Smoker: ", waiters_tips.smoker.unique())
print("Day: ", waiters_tips.day.unique())
print("Time: ", waiters_tips.time.unique())

# examine data - search for null values
null_values = waiters_tips.isnull()
print(null_values)
# count null values
null_value_count = waiters_tips.isnull().sum()
print(null_value_count)
# there are no missing values that need to be treated
"""
had there been any missing values, would use .fillna function
"""

# Search for duplicate values
removed_duplicates = waiters_tips.dropna()
print(waiters_tips.shape, removed_duplicates.shape)
# there are no duplicate values indicating each row is a valid unique service by the waiter













