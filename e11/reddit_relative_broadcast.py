#!/usr/bin/python3

# reddit_averages.py
# CMPT 318 Exercise 11 - Reddit Relative Scores w/broadcasting
# Alex Macdonald
# ID#301272281
# November 24, 2017

import sys
from pyspark.sql import SparkSession, functions, types

spark = SparkSession.builder.appName('reddit relative scores w/broadcasting').getOrCreate()

assert sys.version_info >= (3, 4) # make sure we have Python 3.4+
assert spark.version >= '2.1' # make sure we have Spark 2.1+

schema = types.StructType([ # commented-out fields won't be read
    #types.StructField('archived', types.BooleanType(), False),
    types.StructField('author', types.StringType(), False),
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


def main():
    in_directory = sys.argv[1]
    out_directory = sys.argv[2]

    comments = spark.read.json(in_directory, schema=schema).cache()

    # Calculate the average for each subreddit, as before
    averages = comments.groupby('subreddit').agg(functions.avg('score').alias('average_score')).cache()

    # Exclude any subreddits with average score <= 0
    averages = averages.filter("average_score > 0")
    averages = functions.broadcast(averages)
    

    # Join the average score to the collection of all comments. Divide to get the relative score
    comments = comments.join(averages, 'subreddit')
    comments = comments.withColumn('rel_score', comments.score/comments.average_score)

    # Determine the max relative score for each subreddit
    max_relative_score = comments.groupby('subreddit').agg(functions.max('rel_score').alias('max_rel_score'))
    max_relative_score = functions.broadcast(max_relative_score)

    # Join again to get the best comment on each subreddit: we need this step to get the author
    comments = comments.join(max_relative_score, 'subreddit')
    
    # Filter so we only end up with the authors we want
    comments = comments.filter("rel_score == max_rel_score")
    
    # Remove the now unimportant columns
    comments = comments.drop('score', 'average_score', 'max_rel_score')
    best_author = comments.sort('subreddit')
    
    # Output the results
    best_author.write.json(out_directory, mode='overwrite')


if __name__=='__main__':
    main()
