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

# Read the gzipped file with the built in Pandas funciton
station_fh = gzip.open(stations_filename, 'rt', encoding='utf-8')
stations = pd.read_json(station_fh, lines=True)

# The avg_tmax column is C * 10, so must divide by 10
stations['avg_tmax'] = stations['avg_tmax']/10

# The city data is in a nice convenient CSV file. There are many cities that
# are missing either their area or population: we can't calculate density for those,
# so they can be removed.
# The idea to use np.isfinite was from a StackOverflow discussion I read from user eumiro at:
# https://stackoverflow.com/questions/13413590/how-to-drop-rows-of-pandas-dataframe-whose-value-in-certain-columns-is-nan
cities = pd.read_csv(city_data)
cities = cities[np.isfinite(cities['area'])]
cities = cities[np.isfinite(cities['population'])]

# There are a few cities with areas not reasonable: exclude cities with area greater than 10000 km^2
# Note that the city area is given in m^2, must convert first
cities['area'] = cities['area']/1000000
cities = cities[cities['area'] < 10000]

# Calculate the population density
cities['population_density'] = cities['population']/cities['area']

# Find the weather station that is closest to each city
# We need it's avg_tmax value
# This takes an O(mn) kind of calculation: the distance between every
# city and station pair must be calculated

# Calculates the distance between ONE city and EVERY station
# Can probably modify the function from GPS question in E3
# NOTE: when working on the collection of stations, make sure you're using
# numpy ufuncs which are faster than df.apply(). Your program should take a few
# seconds on a reasonably fast computer, not a few minutes

# Code For the Haversine Function borrowed from:
# https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula/21623206
# Also thanks to ggbaker for posting this link inside the exercise 3 description
def haversine(lat1, long1, lat2, long2):
  EARTH_RADIUS = 6371
  dLat = np.deg2rad(lat2-lat1)
  dLong = np.deg2rad(long2-long1)
  a = np.sin(dLat/2) * np.sin(dLat/2) + np.cos(np.deg2rad(lat1)) * np.cos(np.deg2rad(lat2)) * np.sin(dLong/2) * np.sin(dLong/2)
  c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
  d = EARTH_RADIUS * c
  return d

def distance(city, stations):
  distances = haversine(city['latitude'], city['longitude'], stations['latitude'], stations['longitude'])
  # print(distances)
  return distances

# Returns the best value you can find for avg_tmax for that one city,
# from the list of all weather stations. HINT: use distance and 
# numpy.argmin for this (or series.argmin, or df.idxmin)
# NOTE: there are a few cities that have more than one station at the same
# minimum distance. In that case, we'll use the station that is the first
# in the input data. That choice happens to match the behaviour of .argmin
# and .idxmin, so if you ignore the ambiguity, you'll likely get the right result
def best_tmax(city, stations):
  d = distance(city, stations) # calculate all the distances for each station
  closest_city_index = d.idxmin() # get the index in stations of the nearest station
  return stations.loc[closest_city_index].avg_tmax # use the index to get the avg_tmax

# Apply that function across all cities. You can give extra arguments when applying
# in Pandas like this: cities.apply(best_tmax, stations=station)
# cities.apply(distance, stations=stations, axis=1)
cities['avg_tmax'] = cities.apply(best_tmax, stations=stations, axis=1)

# Produce a scatterplot of average maximum temperature against population Density
plt.figure()
plt.xlabel('Avg Max Temperature (\u00b0C)')
plt.ylabel('Population Density (people/km\u00b2)')
plt.title('Temperature vs. Population Density')
plt.scatter(cities['avg_tmax'], cities['population_density'])
# plt.show()
plt.savefig(output_file)