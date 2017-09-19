#!/usr/bin/python3

# create_plots.py
# CMPT 318 Exercise 2 - Plotting Wikipedia Page Views
# Alex Macdonald
# ID#301272281
# September 19, 2017

import sys
import pandas as pd
import matplotlib.pyplot as plt

filename1 = sys.argv[1]
filename2 = sys.argv[2]

data1 = pd.read_table(filename1, sep=' ', header=None, index_col=1, names=['lang', 'page', 'views', 'bytes'])
data2 = pd.read_table(filename2, sep=' ', header=None, index_col=1, names=['lang', 'page', 'views', 'bytes'])

plt.figure(figsize=(10, 5)) # change the size to something sensible
plt.subplot(1, 2, 1) # subplots in 1 row, 2 columns, select the first
plt.plot(data1)
plt.subplot(1, 2, 2) # ... and then select the second
plt.plot(data2)
plt.show()