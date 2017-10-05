#!/usr/bin/python3

# average_ratings.py
# CMPT 318 Exercise 4 - Cities: Temperatures and Density
# Alex Macdonald
# ID#301272281
# October 6, 2017

import sys
import gzip
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

stations_filename = sys.argv[1] # gziped json
city_data = sys.argv[2] # csv
output_file = sys.argv[3] # svg

station_fh = gzip.open(stations_filename, 'rt', encoding='utf-8')
stations = pd.read_json(station_fh, lines=True)



# Produce a scatterplot of average maximum temperature against population Density
plt.figure(figsize=(1, 1))
plt.xlabel('Avg Max Temperature (\u00b0C)')
plt.ylabel('Population Density (people/km\u00b2)')
plt.title('Temperature vs. Population Density (people/km\u00b2)')
# plt.show()
plt.savefig(output_file)