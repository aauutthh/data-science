#!/usr/bin/python3

# reddit_averages.py
# CMPT 318 Exercise 12 - Word Count
# Alex Macdonald
# ID#301272281
# December 1, 2017

import sys
from pyspark.sql import SparkSession, functions, types, Row
import string, re

spark = SparkSession.builder.appName('correlate logs').getOrCreate()

assert sys.version_info >= (3, 4) # make sure we have Python 3.4+
assert spark.version >= '2.1' # make sure we have Spark 2.1+

wordbreak = r'[%s\s]+' % (re.escape(string.punctuation),)  # regex that matches spaces and/or punctuation

def main():
  in_directory = sys.argv[1]
  out_directory = sys.argv[2]

  # 1. Read lines from the files with spark.read.text
  lines = spark.read.text(in_directory).cache()

  # 2. Split the lines into words with the regular expression
  # .. use the spilt and explode functions. Normalize all of the strings to lower-case 
  
  # Usage of Explode and Split based on a StackOverFlow discussion which
  # can be found at: https://stackoverflow.com/questions/38210507/explode-in-pyspark
  words = lines.select(functions.explode(functions.split(lines.value, wordbreak)).alias("words")).cache()
  words = words.select(words.words, functions.lower(words.words).alias("word"))
  words = words.drop('words')

  # 3. Count the number of times each word occurs
  words = words.groupby('word').count()

  # 4. Sort by decreasing count (i.e. frequent words first) and alphabetically if there's a tie
  words = words.sort(functions.desc('count'))

  # 5. Notice that there are likely empty strings being counted: remove them from the output
  # .. they come from spaces at the start/end of lines in the original input 
  # Note: I wanted to use Regex for this, so I had to find out how to filter w/regex in pyspark.
  # Found a StackOverflow page that told me about rlike(), it can be fount at:
  # https://stackoverflow.com/questions/45580057/pyspark-filter-dataframe-by-regex-with-string-formatting
  words = words.filter(words.word.rlike("[A-z]+"))

  # 6. Write results as CSV files with the word in the first column,
  # .. and count in the second (uncompressed, they aren't big enough to worry about)
  words.write.csv(out_directory, mode='overwrite')


if __name__=='__main__':
    main()