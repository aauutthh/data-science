#!/usr/bin/python3

# create_data.py
# CMPT 318 Exercise 6 - Benchmarking Sorting
# Alex Macdonald
# ID#301272281
# October 20, 2017

import time
from implementations import all_implementations

# We are concerned about
# (1) Arrays with Random Integers
# (2) Arrays that are as large as possible
# (3) Being able to meaningfully analyse the results

# for sort in all_implementations:
#   st = time.time()
#   res = sort(random_array)
#   en = time.time()

# Create a DataFrame in a format that makes sense, and save it as data.csv
# data.to_csv('data.csv', index=False)