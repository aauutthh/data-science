#!/usr/bin/python3

# smooth_temperature.py
# CMPT 318 Exercise 3 - GPS Tracks: How Far Did I Walk?
# Alex Macdonald
# ID#301272281
# September 29, 2017

import sys
from pykalman import KalmanFilter
import numpy as np
import pandas as pd
from xml.dom.minidom import parse, parseString

# Read the XML
def read_gpx(file):
  
  # Lists that will hold the data as the XML is parsed
  latitude = []
  longitude = []

  # Parse the file, and iterate over the file to extract lat & lon info
  dom = parse(file)
  for node in dom.getElementsByTagName('trkpt'):
    latitude.append(node.getAttribute('lat'))
    longitude.append(node.getAttribute('lon'))

  # Shove it all into a dataframe
  points = pd.DataFrame({
    'lat': latitude,
    'lon': longitude
  })

  # Make sure that the information is in float data type
  points['lat'] = points['lat'].astype('float')
  points['lon'] = points['lon'].astype('float')
  return points

def distance(df):
  points = df.copy(deep=True)
  points['lat_adjacent'] = points.lat.shift(-1)
  points['lon_adjacent'] = points.lon.shift(-1)
  points['distance'] = haversine(points['lat'], points['lon'], points['lat_adjacent'], points['lon_adjacent'])
  return points['distance'].sum()
  
# Code For the Haversine Function borrowed from:
# https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula/21623206
# Also thanks to ggbaker for posting this link inside the assignments  
def haversine(lat1, long1, lat2, long2):
  EARTH_RADIUS = 6371
  dLat = np.deg2rad(lat2-lat1)
  dLong = np.deg2rad(long2-long1)
  a = np.sin(dLat/2) * np.sin(dLat/2) + np.cos(np.deg2rad(lat1)) * np.cos(np.deg2rad(lat2)) * np.sin(dLong/2) * np.sin(dLong/2)
  c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
  d = EARTH_RADIUS * c
  return d * 1000

def smooth(df):
  points = df.copy(deep=True)

  # the first data point is a good guess of where the walk started
  initial_state = points.iloc[0]

  # One degree of latitude is about 10^5 meters - close enough for calculating error
  # observation_covariance: phone is accurate to 15 to 20 meters
  observation_covariance = np.diag([20/10000, 20/10000]) ** 2
  
  # transition_matrices: current position will be the same as previous position
  transition_matrix = np.diag([1, 1])

  # transition_covariance: ggbaker walks at 1m/s, and the data contains an observation ~every 10 s
  transition_covariance = np.diag([10/10000, 10/10000]) ** 2
  
  kf = KalmanFilter(
    transition_matrices=transition_matrix,
    transition_covariance=transition_covariance,
    observation_covariance=observation_covariance,
    initial_state_mean=initial_state
  )
  kf_smoothed, _ = kf.smooth(points)
  kf_df = pd.DataFrame(kf_smoothed, columns=['lat', 'lon'])
  return kf_df

# Borrowed code from calc_distance_hint.py
def output_gpx(points, output_filename):
    """
    Output a GPX file with latitude and longitude from the points DataFrame.
    """
    from xml.dom.minidom import getDOMImplementation
    def append_trkpt(pt, trkseg, doc):
        trkpt = doc.createElement('trkpt')
        trkpt.setAttribute('lat', '%.8f' % (pt['lat']))
        trkpt.setAttribute('lon', '%.8f' % (pt['lon']))
        trkseg.appendChild(trkpt)
    
    doc = getDOMImplementation().createDocument(None, 'gpx', None)
    trk = doc.createElement('trk')
    doc.documentElement.appendChild(trk)
    trkseg = doc.createElement('trkseg')
    trk.appendChild(trkseg)
    
    points.apply(append_trkpt, axis=1, trkseg=trkseg, doc=doc)
    
    with open(output_filename, 'w') as fh:
        doc.writexml(fh, indent=' ')


def main():
    points = read_gpx(sys.argv[1])
    print('Unfiltered distance: %0.2f' % (distance(points)))
    
    smoothed_points = smooth(points)
    print('Filtered distance: %0.2f' % (distance(smoothed_points)))
    output_gpx(smoothed_points, 'out.gpx')


if __name__ == '__main__':
    main()
