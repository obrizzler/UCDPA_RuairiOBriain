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

# Examine the waiters_tips dataframe - Print a list of the column headers
column_headers = waiters_tips.columns
print(column_headers)
# examine content of waiters_tips dataframe - view top 10 & bottom 5 rows
print(waiters_tips.head(10))
print(waiters_tips.tail())
# examine length and shape of waiters_tips dataframe
dataframe_length = str(len(waiters_tips))
dataframe_shape = str(waiters_tips.shape)
print("The waiters_tips dataframe is " + dataframe_length + " rows long.")
print("Its shape (rows,columns) is: " + dataframe_shape)
# examine data types of each column
print(waiters_tips.dtypes)












