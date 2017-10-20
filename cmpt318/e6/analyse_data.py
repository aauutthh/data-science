#!/usr/bin/python3

# analyse_data.py
# CMPT 318 Exercise 6 - Benchmarking Sorting
# Alex Macdonald
# ID#301272281
# October 20, 2017

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Reads the data.csv produced and does the relevant analysis
# It should print the information used to answer question 3, but no specific format

# Will need a statistical test that can be used to determine if the means of
# multiple samples are different - TUKEY

data = pd.read_csv('data.csv')

# Code for post-hoc Tukey test borrowed from:
# http://www.cs.sfu.ca/~ggbaker/data-science/content/stats-tests.html
melt = pd.melt(data)
posthoc = pairwise_tukeyhsd(
  melt['value'], melt['variable'],
  alpha=0.05)

# It should print the information you used to answer queston 3
print(posthoc)

# I used the figure that is commentet out below to answer #3
fig = posthoc.plot_simultaneous()
plt.show()

# Based on the above figure, I did some quick analysis to show the mean values
# for the significantly different sorts, as determined by Tukey

# TODO: Create a simple function that calculates the mean of each row and outputs them
# only for those which are different from each other
# QS1, Partition Sort, QS4/5, QS2/3, Mergesort