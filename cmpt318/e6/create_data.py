#!/usr/bin/python3

# CMPT 318 Exercise 6 - Benchmarking Sorting
# Alex Macdonald
# ID#301272281
# October 20, 2017

import numpy as np
import pandas as pd
import datetime
import time
from implementations import all_implementations

# Generate random arrays, and use time.time to measure the wall-clock time
# each function takes to sort them. Can write loops.

# We are concerned about
# (1) Arrays with Random Integers -> use np.random.randint()
# (2) Arrays that are as large as possible -> no max size for np .. let's go with 100,000 size ten
# (3) Being able to meaningfully analyse the results

# This program must run in at most 60 seconds on gateway.sfucloud.ca
# So let's be safe, and run this program for 57 seconds
time_end = time.time() + 57
global_results = []
print('Creating data for analysis .. this will take ~57 seconds.')
# On the gateway.sfuclould.ca, will create ~48 results in 57 seconds, with a total runtime of ~58.5 seconds.
print('          [Start                               Approx. End]')
# Idea of flushing console for a progress bar borrowed from: 
# https://stackoverflow.com/questions/493386/how-to-print-without-newline-or-space
print('Progress: [', end='', flush=True)
while time.time() < time_end:
  random_array = np.random.randint(low=0, high=10000, size=22500, dtype=np.int)
  local_results = []
  for sort in all_implementations:
    st = time.time()
    res = sort(random_array)
    en = time.time()
    elapsed = en-st
    local_results.append(elapsed)
  global_results.append(local_results)
  print('=', end='', flush=True)
print(']')
data = pd.DataFrame(global_results, columns=['qs1', 'qs2', 'qs3', 'qs4', 'qs5', 'merge1', 'partition_sort'])

# Create a DataFrame in a format that makes sense, and save it as data.csv
data.to_csv('data.csv', index=False)