#!/usr/bin/python3

# weather_etl.py
# CMPT 318 Exercise 9 - Extract-Transform-Load GHCN Data
# Alex Macdonald
# ID#301272281
# November 10, 2017

import sys
from pyspark.sql import SparkSession, functions, types

spark = SparkSession.builder.appName('weather ETL').getOrCreate()

assert sys.version_info >= (3, 4) # make sure we have Python 3.4+
assert spark.version >= '2.1' # make sure we have Spark 2.1+, because 2.2 isn't in CSIL

observation_schema = types.StructType([
    types.StructField('station', types.StringType(), False),
    types.StructField('date', types.StringType(), False),
    types.StructField('observation', types.StringType(), False),
    types.StructField('value', types.IntegerType(), False),
    types.StructField('mflag', types.StringType(), False),
    types.StructField('qflag', types.StringType(), False),
    types.StructField('sflag', types.StringType(), False),
    types.StructField('obstime', types.StringType(), False),
])


def main(in_directory, out_directory):
    # 1. Read the input directory of .csv.gz files
    weather = spark.read.csv(in_directory, schema=observation_schema)
    # 2. Keep only the records we care about:
    # a. field qflag (quality flag) is null
    weather = weather.filter(weather.qflag.isNull())
    # b. the station starts with 'CA'
    weather = weather.filter(weather.station.startswith('CA'))
    # c. the observation is 'TMAX'
    weather = weather.filter("observation = 'TMAX'")
    # 3. Divide the temperature by 10 so it's actually in C (do in the next step for simplicity)
    # 4. Keep only the columns station, date, and tmax (which is the value after dividing by 10)
    cleaned_data = weather.select(weather['station'], weather['date'], (weather['value']/10).alias('tmax'))
    # 5. Write the result as a directory of JSON files GZIP compressed
    cleaned_data.write.json(out_directory, compression='gzip', mode='overwrite')


if __name__=='__main__':
    in_directory = sys.argv[1]
    out_directory = sys.argv[2]
    main(in_directory, out_directory)