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
print(type(waiters_tips))

# examine new waiters_tips dataframe - view top 10 rows)
print(waiters_tips.head(10))




