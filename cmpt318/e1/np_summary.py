#!/usr/bin/env python

# np_summary.py
# CMPT 318 Exercise 1 - Getting Started with NumPy
# Alex Macdonald
# ID#301272281
# September 11, 2018

# Objective:
# Write a Python program np_summary.py that produces the values specified here. 
# Its output should exactly match the provided np_summary.txt. 
# We will test it on a different set of inputs: your code should not assume there is a specific number of weather stations. 
# You can assume that there is exactly one year (12 months) of data.

import numpy as np

data = np.load('monthdata.npz')
totals = data['totals']
counts = data['counts']

# Which city had the lowest total precipitation over the year? 
# Hints: sum across the rows (axis 1); use argmin to determine which row has the lowest value. 
# Print the row number.
cityTotals = totals.sum(axis=1)
lowestPrecip = np.argmin(cityTotals)
print "Row with lowest total preciptiation:"
print lowestPrecip

# Determine the average precipitation in these locations for each month. 
# That will be the total precipitation for each month (axis 0), divided by the total observations for that months. 
# Print the resulting array.
monthlyTotals = totals.sum(axis=0)
monthlyCounts = counts.sum(axis=0)
avgMonthPrecip = np.divide(monthlyTotals, monthlyCounts, dtype=float)
print "Average precipitation in each month:"
print avgMonthPrecip

# Do the same for the cities: 
# give the average daily precipitation for each city by printing the array.
cityCounts = counts.sum(axis=1)
avgCityPrecip = np.divide(cityTotals, cityCounts, dtype=float)
print "Average precipitation in each city:"
print avgCityPrecip

# Calculate the total precipitation for each quarter in each city 
# (i.e. the totals for each station across three-month groups). 
# You can assume the number of columns will be divisible by 3. 
# Hint: use the reshape function to reshape to a 4n by 3 array, 
# sum, and reshape back to n by 4.
n = np.shape(totals)[0]
reshaped = totals.reshape(4*n, 3)
reshaped_sum = reshaped.sum(axis=1)
quarterlyPrecipTotals = reshaped_sum.reshape(n, 4)
print "Quarterly precipitation totals:"
print quarterlyPrecipTotals
