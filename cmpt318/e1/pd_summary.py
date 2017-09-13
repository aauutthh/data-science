#!/usr/bin/env python

# pd_summary.py
# CMPT 318 Exercise 1 - Getting Started with Pandas
# Alex Macdonald
# ID#301272281
# September 11, 2018

# Objective
# Write a Python program pd_summary.py that produces the values specified here.
# Its output should exactly match the provided pd_summary.txt.

import pandas as pd

totals = pd.read_csv('totals.csv').set_index(keys=['name'])
counts = pd.read_csv('counts.csv').set_index(keys=['name'])

# Which city had the lowest total precipitation over the year? 
# Hints: sum across the rows (axis 1); use argmin to determine which row has the lowest value. 
# Print the row number.
cityTotals = totals.sum(axis=1)
lowestPrecip = cityTotals.idxmin()
print ("Row with lowest total preciptiation:")
# print lowestPrecip # More human readible output
print (totals.index.get_loc(lowestPrecip)) # Similar to the NumPy output


# Determine the average precipitation in these locations for each month. 
# That will be the total precipitation for each month (axis 0), divided by the total observations for that months. 
# Print the resulting array.
monthlyTotals = totals.sum(axis=0)
monthlyCounts = counts.sum(axis=0)
avgMonthlyPrecip = monthlyTotals.div(monthlyCounts)
print ("Average precipitation in each month:")
# print avgMonthlyPrecip # More human readible output
print (avgMonthlyPrecip.values) # Similar to the NumPy output

# Do the same for the cities: 
# give the average daily precipitation for each city by printing the array.
cityCounts = counts.sum(axis=1)
avgCityPrecip = cityTotals.div(cityCounts)
print ("Average precipitation in each city:")
# print avgCityPrecip # More human readible output
print (avgCityPrecip.values) # Similar to the NumPy output