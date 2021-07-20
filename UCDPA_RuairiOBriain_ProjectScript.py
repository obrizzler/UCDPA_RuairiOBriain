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
print("Review for any blanks: ")
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

print("\n")
"""
Create subset dataframes to facilitate segmentation and analysis
Create the following subsets
Billpayer by gender: female_bill payers / male_billpayers
Bill payer by gender & smoking status:
  female_smokers
  female_nonsmokers
  male_smokers
  male_nonsmokers
"""

# Create subset dataframe: Female Billpayers
print("Female Bill Payers Table")
female_billpayers = waiters_tips[(waiters_tips["sex"]=="Female")]
print(female_billpayers.head())
# compare shape
print(waiters_tips.shape, female_billpayers.shape)

print("\n")

# Create subset dataframe: Male Billpayers
print("Male Bill Payers Table")
male_billpayers = waiters_tips[(waiters_tips["sex"]=="Male")]
print(male_billpayers.head())
# compare shape
print(waiters_tips.shape, male_billpayers.shape)

print("\n")

# including an additional condition to further segment restaurant customers
# Create subset dataframe: Female Smokers
print("Female Smokers Table")
female_smokers = waiters_tips[(waiters_tips["sex"]=="Female") & (waiters_tips["smoker"]=="Yes")]
print(female_smokers.head())
# compare shape
print(waiters_tips.shape, female_smokers.shape)

print("\n")

# Create subset dataframe: Female Non-Smokers
print("Female Non Smokers Table")
female_nonsmokers = waiters_tips[(waiters_tips["sex"]=="Female") & (waiters_tips["smoker"]=="No")]
print(female_nonsmokers.head())
print(female_nonsmokers.shape)
print(waiters_tips.shape, female_nonsmokers.shape)

print("\n")

# Create subset dataframe: Male Smokers
print("Male Smokers Table")
male_smokers = waiters_tips[(waiters_tips["sex"]=="Male") & (waiters_tips["smoker"]=="Yes")]
print(male_smokers.head())
print(male_smokers.shape)
print(waiters_tips.shape, male_smokers.shape)

print("\n")

# Create subset dataframe: Male Non-Smokers
male_nonsmokers = waiters_tips[(waiters_tips["sex"]=="Male") & (waiters_tips["smoker"]=="No")]
print(male_nonsmokers.head())
print(male_nonsmokers.shape)
print(waiters_tips.shape, male_nonsmokers.shape)

print("\n")

# Concatenate dataframes to create subset dataframes: 'All Smokers' and 'Non-Smokers'
print("All Smokers Table")
all_smokers = pd.concat([female_smokers, male_smokers], axis = 0, ignore_index = True)
print(all_smokers.head())
print(all_smokers.shape)
print(waiters_tips.shape, all_smokers.shape)

print("\n")

print("All Non-Smokers Table")
all_nonsmokers = pd.concat([female_nonsmokers, male_nonsmokers], axis = 0, ignore_index = True)
print(all_nonsmokers.head())
print(all_nonsmokers.shape)
print(waiters_tips.shape, all_nonsmokers.shape)

print("\n")

# create lists from each dataframe column to aid visualisation
bill_list = waiters_tips.total_bill.values.tolist()
tip_list = waiters_tips.tip.values.tolist()
gender_list = waiters_tips.sex.values.tolist()
smoker_list = waiters_tips.smoker.values.tolist()
day_list = waiters_tips.day.values.tolist()
time_list = waiters_tips.time.values.tolist()


malesmoker_total = len(male_smokers)
male_nonsmoker_total = len(male_nonsmokers)
femalesmoker_total = len(female_smokers)
female_nonsmoker_total = len(female_nonsmokers)
smoker_values = [male_nonsmoker_total, malesmoker_total, femalesmoker_total, female_nonsmoker_total]


# Visualisaton - Matplotlib library with .pyplot functionality already imported as plt.

#Create plot area
fig,ax = plt.subplots()
plt.show()

# Create a pie chart displaying the proportion of bill_payers by gender and smoking status
# explode the largest segment for display / emphasis purposes

labels = 'Male Non-Smokers', 'Male Smokers', 'Female Smokers', 'Female Non-Smokers'
sizes = smoker_values
explode = (0.1, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()











