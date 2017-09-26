#!/usr/bin/python3

# smooth_temperature.py
# CMPT 318 Exercise 3 - CPU Temperature Noise Reduction
# Alex Macdonald
# ID#301272281
# September 29, 2017

import sys
from pykalman import KalmanFilter
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Function to convert datetime entries to a timestamp
def to_timestamp(datetime):
  timestamp = datetime.timestamp()
  return timestamp

file = sys.argv[1]
data = pd.read_table(file, sep=',', header=0)

# There's a problem with the timestamp data in the csv
# To rectify this, convert the column to datetime format ..
data['timestamp'] = pd.to_datetime(data['timestamp'])
# And then back into a timestamp format.
data['timestamp'] = data['timestamp'].apply(to_timestamp)
# TODO Convert into a nice format like hour:min for readibility

# LOESS Smoothing
frac = 0.15 # looks like a pretty good value to choose
lowess_smoothed = sm.nonparametric.lowess(data['temperature'].values, data['timestamp'].values, frac)

# Kalman Smoothing
kalman_data = data[['temperature', 'cpu_percent', 'sys_load_1']]
initial_state = kalman_data.iloc[0]
observation_covariance = np.diag([0, 0, 0]) ** 2 # TODO: shouldn't be zero
transition_covariance = np.diag([0, 0, 0]) ** 2 # TODO: shouldn't be zero
transition = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # TODO: shouldn't (all) be zero
kf = KalmanFilter()
kalman_smoothed, _ = kf.smooth(kalman_data)

# Prepare the chart, and write to file
plt.figure(figsize=(12, 4))
plt.plot(data['timestamp'], data['temperature'], 'b.', alpha=0.5)
plt.plot(data['timestamp'], lowess_smoothed[:, 1], 'r-')
# plt.plot(data['timestamp'], kalman_smoothed[:, 0], 'g-')
plt.title('Daily Correlation')
plt.xlabel('Timestamp')
plt.ylabel('Temperature')
plt.show()
# plt.savefig('cpu.svg')