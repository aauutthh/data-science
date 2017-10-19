#!/usr/bin/python3

# analyse_data.py
# CMPT 318 Exercise 6 - Benchmarking Sorting
# Alex Macdonald
# ID#301272281
# October 20, 2017

import numpy as np
import pandas as pd
from scipy import stats

# Reads the data.csv produced and does the relevant analysis
# It should print the information used to answer question 3, but no specific format

# Will need a statistical test that can be used to determine if the means of
# multiple samples are different - TUKEY (& ANOVA)

# QUESTION - Can we assume that this is called data.csv, or do we take it as a cli?

data = pd.read_csv('data.csv')

# Ideas and methodologies for the ANOVA and Tukey tests were borrowed from:
# http://cleverowl.uk/2015/07/01/using-one-way-anova-and-tukeys-test-to-compare-data-sets/

f, p = stats.f_oneway(
  data['qs1'],
  data['qs2'],
  data['qs3'],
  data['qs4'],
  data['qs5'],
  data['merge1'],
  data['partition_sort']
)
print(f)
print(p)