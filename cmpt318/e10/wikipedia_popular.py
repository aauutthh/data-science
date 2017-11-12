#!/usr/bin/python3

# wikipedia_popular.py
# CMPT 318 Exercise 10 - Popular Wikipedia Pages
# Alex Macdonald
# ID#301272281
# November 17, 2017

import sys
from pyspark.sql import SparkSession, functions, types

spark = SparkSession.builder.appName('popular wikipedia pages').getOrCreate()

assert sys.version_info >= (3, 4) # make sure we have Python 3.4+
assert spark.version >= '2.1' # make sure we have Spark 2.1+

schema = types.StructType([
  types.StructField('language', types.StringType(), False),
  types.StructField('pagename', types.StringType(), False),
  types.StructField('viewcount', types.LongType(), False)
])

def get_filename_from_path(path):
  filename = path[path.rfind('/'):] # After this, the string will be /pagecounts-(what we want)0000
  filename = filename[12:23] # By means of voodoo hack-fu, here's a substring that returns the string we want
  return filename

def main(in_directory, out_directory):
    # Thanks to ggbaker for the hint to use sep & input_file_name & udf
    pages = spark.read.csv(in_directory, sep=' ', schema=schema).withColumn('filename', functions.input_file_name()).cache()

    # from the filename column, get the hour and then remove filename because we don't need it anymore
    path_to_hour = functions.udf(get_filename_from_path, returnType=types.StringType())
    pages = pages.withColumn('hour', path_to_hour(pages.filename))
    pages = pages.drop('filename')

    # We're interested in:
    # 1. English Wikipedia pages (i.e., language is 'en')
    pages = pages.filter("language = 'en'")
    pages = pages.drop('language')
    # 2. Exclude 'Main_Page'
    pages = pages.filter("pagename != 'Main_Page'")
    # 3. Exclude 'Special:'
    # Learned to use the tilde for negation from:
    # https://stackoverflow.com/questions/40743915/filtering-string-in-pyspark
    pages = pages.filter(~pages.pagename.contains('Special:'))

    # .. need to find the largest number of page views in each hour
    # Create a new dataframe to hold the aggregated hours & max views
    max_views = pages.groupby('hour').agg(functions.max('viewcount').alias('max'))

    # .. then join that back to the collection of all page pagecounts
    pages = pages.join(max_views, 'hour')

    # .. only keep those with count == max(count) for that hour
    pages = pages.filter(pages.viewcount == pages.max)

    # sort by date/hour and page name in the event of a tie
    pages = pages.sort('hour', 'pagename')

    # make sure the results are in the order as shown in the assignment sample output
    pages = pages.select('hour', 'pagename', 'viewcount')

    # Write results to directory
    pages.write.csv(out_directory, mode='overwrite')


if __name__=='__main__':
    in_directory = sys.argv[1]
    out_directory = sys.argv[2]
    main(in_directory, out_directory)