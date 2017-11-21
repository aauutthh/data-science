#!/usr/bin/python3

# reddit_averages.py
# CMPT 318 Exercise 10 - Reddit Average Scores
# Alex Macdonald
# ID#301272281
# November 17, 2017

# Question: what is the average score in each subreddit?

import sys
from pyspark.sql import SparkSession, functions, types

spark = SparkSession.builder.appName('reddit averages').getOrCreate()

assert sys.version_info >= (3, 4) # make sure we have Python 3.4+
assert spark.version >= '2.1' # make sure we have Spark 2.1+


schema = types.StructType([ # commented-out fields won't be read
    #types.StructField('archived', types.BooleanType(), False),
    #types.StructField('author', types.StringType(), False),
    #types.StructField('author_flair_css_class', types.StringType(), False),
    #types.StructField('author_flair_text', types.StringType(), False),
    #types.StructField('body', types.StringType(), False),
    #types.StructField('controversiality', types.LongType(), False),
    #types.StructField('created_utc', types.StringType(), False),
    #types.StructField('distinguished', types.StringType(), False),
    #types.StructField('downs', types.LongType(), False),
    #types.StructField('edited', types.StringType(), False),
    #types.StructField('gilded', types.LongType(), False),
    #types.StructField('id', types.StringType(), False),
    #types.StructField('link_id', types.StringType(), False),
    #types.StructField('name', types.StringType(), False),
    #types.StructField('parent_id', types.StringType(), True),
    #types.StructField('retrieved_on', types.LongType(), False),
    types.StructField('score', types.LongType(), False),
    #types.StructField('score_hidden', types.BooleanType(), False),
    types.StructField('subreddit', types.StringType(), False),
    #types.StructField('subreddit_id', types.StringType(), False),
    #types.StructField('ups', types.LongType(), False),
])


def main(in_directory, out_directory):
    comments = spark.read.json(in_directory, schema=schema)

    # Code modified from a StackOverflow post found at:
    # https://stackoverflow.com/questions/33882894/sparksql-apply-aggregate-functions-to-a-list-of-column/33907419
    averages = comments.groupby('subreddit').avg()
    averages = averages.cache()

    # We want to produce the average scores sorted two ways:
    # 1. by subreddit name
    averages_by_subreddit = averages.sort('subreddit')
    # 2. by score (highest scores first) = descending
    averages_by_score = averages.sort(functions.desc('avg(score)'))

    averages_by_subreddit.write.csv(out_directory + '-subreddit', mode='overwrite')
    averages_by_score.write.csv(out_directory + '-score', mode='overwrite')


if __name__=='__main__':
    in_directory = sys.argv[1]
    out_directory = sys.argv[2]
    main(in_directory, out_directory)
