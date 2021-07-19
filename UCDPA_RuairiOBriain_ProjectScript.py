# importing libraries (installed via Python Interpretter
# pandas - library for dataframe
import pandas as pd
# numpy - library for arrays
import numpy as np
# os to import dataframe
import os
# matplolib - library for data visualisation
import matplotlib.pyplot as plt


# check current working directory (CWD)
print(os.getcwd())
# change working directory to working file
os.chdir(r"C:\Users\obria\OneDrive\Documents\Edu\UCD - Data Anlaytics\Data Project\UCDPA_Project")
#include break in code display
print("\n")

# import .csv dataset
waiters_tips = pd.read_csv('waiter_tips.csv', encoding = 'ISO-8859-1')
# check type of imported dataset
waiters_tips_type = str(type(waiters_tips))
print("Waiters_tips is a: " + waiters_tips_type)

# examine the waiters_tips dataframe - Print a list of the column headers
# deep copy and converting to list
# converting to string to concatenate
column_headers = list(waiters_tips.columns)
print("The column headers constitute a " + str(type(column_headers)))
print("\n")

print("The column headers are: ")
# using a for loop to list out the column headers for reference
for i in column_headers:
    print(i)
# Alternatively could use for i in waiters_tips.columns
print("\n")

print("The format/shape of the database looks like the following: ")
# examine the broader content & format of waiters_tips dataframe - view top 10 & bottom 5 rows
print("Head")
print(waiters_tips.head(10))
print("\n")
print("Tail")
print(waiters_tips.tail())

# examine length and shape of waiters_tips dataframe
dataframe_length = str(len(waiters_tips))
dataframe_shape = str(waiters_tips.shape)
print("The waiters_tips dataframe is " + dataframe_length + " rows long.")
print("Its shape (rows,columns) is: " + dataframe_shape)
print("\n")
# examine data types of each column
print("The data types in each column are: ")
print(waiters_tips.dtypes)
print("\n")

# examine level of the dataset that is the primary key
print("The number of unique values in each column is: ")
print("Total Bill: " + str(len(waiters_tips.total_bill.unique())))
print("Tip: " + str(len(waiters_tips.tip.unique())))
print("Sex: " + str(len(waiters_tips.sex.unique())))
print("Smoker: " + str(len(waiters_tips.smoker.unique())))
print("Day: " + str(len(waiters_tips.day.unique())))
print("Time: " + str(len(waiters_tips.time.unique())))
print("\n")
# display unique values in sex, smoker, day, and time columns
print("The unique values in the sex, smoker, day, and time columns are: ")
print("Sex: ", waiters_tips.sex.unique())
print("Smoker: ", waiters_tips.smoker.unique())
print("Day: ", waiters_tips.day.unique())
print("Time: ", waiters_tips.time.unique())

print("\n")
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
print("\n")
# Examine dataframe for duplicate values
removed_duplicates = waiters_tips.dropna()
print(waiters_tips.shape, removed_duplicates.shape)

if waiters_tips.shape == removed_duplicates.shape:
    print("No duplicates were identified in this dataframe and therefore none had to be removed.")
else:
    print("Duplicates have been identified and removed from this dataframe.")

# Visualisaton - Matplotlib library with .pyplot functionality already imported as plt.
# Add command to keep graphs from opening in a new window and instead appear in line with code
%matplotlib inline














