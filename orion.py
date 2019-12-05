# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 16:02:13 2019

@author: lilit
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file = "orion_stepcount.csv"
orion = pd.read_csv(file)


# %% Initial examination:

print("Orion step count data - head: \n", orion.head(), "\n")
print("Orion step count data - info: \n", orion.info(), "\n") #Why does this say None?
print("Orion step count data - columns: \n", orion.columns, "\n")
print("Orion step count data - shape: \n", orion.shape, "\n")

# %% Check nulls:

print("Check for null values: ")
print(orion.isnull().any())

# %% Rename columns:

# Replace white space in columns headers with underscore:
orion.columns = orion.columns.str.replace(" ", "_")
# The .replacec(old, new) function is a python string method.
# I think this is why we need to use .str.replace() in order for this to work!

# (For more tips on removing whitespace, e.g. trailing whitespace, see
# rename_columns_remove_whitespace.py file in Useful Libraries.

# Lower case columns using map(function, input):
orion.columns = map(str.lower, orion.columns) 

orion.rename(columns = {"difference_between_my_steps_per_day_and_orion's_count":"steps_diff"}, inplace=True)

print("\nNew column names: \n", orion.columns, "\n")
# %% Some useful functions:

def start_date():
    """Returns the date that records began, 
    i.e. the date this knee was obtained."""
    return(orion.date_recorded.iloc[-1])
    
def total_steps():
    """Returns the total number of steps recorded 
    since the knee was obtained."""
    return(orion.total_step_count.iloc[-1])

# ^NB: When you want to retrieve a specific entry (e.g. the last entry),
    # DON'T use [-1:] because this will return a Series!
    # instead, use .iloc[-1] and this will return a numpy integer or string, etc.

print("You have walked {0} steps so far since {1}.".format(total_steps(), start_date()))

# %% TO DO:

"""
- save to git and github
- think of more helpful functions?
- start seeing what graphs I want to make
- eventually, make it so that all interactions can happen through functions
(then i can upload to pythonanywhere!)
"""
