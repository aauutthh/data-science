#!/usr/bin/python3

# create_plots.py
# CMPT 318 Exercise 2 - Plotting Wikipedia Page Views
# Alex Macdonald
# ID#301272281
# September 22, 2017

import sys
import pandas as pd
import matplotlib.pyplot as plt

filename1 = sys.argv[1]
filename2 = sys.argv[2]

data1 = pd.read_table(filename1, sep=' ', header=None, names=['lang', 'page', 'views', 'bytes'])
data2 = pd.read_table(filename2, sep=' ', header=None, names=['lang', 'page', 'views', 'bytes'])

# Plot 1: Distribution of Views
# > We will use only the first data set
# > Using only the first input file, sort the data by the number of views (decreasing)
#   HINT: sort_values
data1Sorted = data1.sort_values('views', 0, ascending=False)

# > If you give plt.plot a single data set, it will be plotted against a 0 to n-1 range,
#   which is what we want.
# > BUT, if we give matplotlib a Pandas series (e.g., data['views']) it will try to
#   use its index as the x-coordinate. To convince it otherwise, we have two options:
# > > 1. Pass the underlying NumPy array (data['views'].values) OR
# > > 2. Create a range to explicitly use as the x-coordinates (with np.arrange)
plt.figure(figsize=(10, 5)) # change the size to something sensible
plt.subplot(1, 2, 1) # subplots in 1 row, 2 columns, select the first
plt.xlabel('Rank')
plt.ylabel('Views')
plt.title('Popularity Distribution')
plt.plot(data1Sorted['views'].values)

# Plot 2: Daily Views
# > The files contain space-separated values for the language, page name, number of
#   views, and bytes transferred. You can get the data out of the file format like this:
# > The second plot we want to create is a scatterplot of views from the first data file
#   (x-coordinate), and the corresponding values from the second data file (y-coordinate)
# > It's fairly reasonable to expect a linear relationship between those values.
# > To do this, will need to get the two series into the same DataFrame.
# > If used the hint above to read the file, the page name will be the index, so the
#   right data points will be joined together if you create a new DF with those series
# > Because of the distribution of values, the linear axes don't make much sense, change
#   this plot to log-scale on both axes using plt.xscale and plt.yscale

merged = pd.merge(data1, data2, on=['page'])

plt.subplot(1, 2, 2) # ... and then select the second
plt.title('Daily Correlation')
plt.xlabel('Day 1 views')
plt.ylabel('Day 2 views')
plt.xscale('log')
plt.yscale('log')
plt.scatter(merged['views_x'], merged['views_y'])

# Final Output
# > Can use plt.show() to see the figure as the program runs
# > That is probably the easiest for testing, but as a final result, don't show()
# > Instead, create a PNG file called wikipedia.png
# > Use the functions plt.title, plt.xlabel, and plt.ylabel to give some useful
#   labels to the plots. A sample wikipedia.png is included in the ZIP file.

# plt.show()
plt.savefig('wikipedia.png')
