#!/usr/bin/python3

# average_ratings.py
# CMPT 318 Exercise 4 - Movie Title Entity Resolution
# Alex Macdonald
# ID#301272281
# October 6, 2017

# Objective: 
# . Determine the average rating for each movie, compensating for bad spelling
# . It should produce a CSV file with 'title' as the first column
# . . and (average) 'rating' rounded to two decimal places as the second
# . The output should be sorted by title.

import sys
import difflib
import numpy as np
import pandas as pd

movie_titles = sys.argv[1]
movie_ratings = sys.argv[2]
output_file = sys.argv[3]

# Read data from movie_list.txt, store in a df
movie_list = open(movie_titles).read().splitlines()

# Reading data from movie_ratings.csv
ratings = open(movie_ratings).read().splitlines()

# Dump it all into a dataframe
df_ratings = pd.DataFrame(ratings, columns=["all"])

# Remove the header line, I'll re-add it soon
df_ratings.drop(df_ratings["all"].index[[0]], inplace=True)

# Regex out the movie titles into a column
df_ratings['title'] = df_ratings['all'].str.extract('(.*?),\d\.?\d?$', expand=True)

# Regex out the movie ratings into a column
df_ratings['rating'] = df_ratings['all'].str.extract('.*?,(\d\.?\d?)$', expand=True)
df_ratings['rating'] = df_ratings['rating'].astype('float')

# Remove the column that contained a monolithic dump of the data
df_ratings.drop('all', axis=1, inplace=True)

# Find the closest match for every movie title from movie_list
def get_closest_movie_name(t):
  result = difflib.get_close_matches(t, movie_list)
  return ''.join(result)

df_ratings['title'] = df_ratings['title'].apply(get_closest_movie_name)

# Remove the entries that had no closest match
df_ratings = df_ratings[df_ratings['title'].str.len() != 0]

# Sort (and group) by title & aggregate & round to 2 decimal places
df_ratings = df_ratings.groupby('title').aggregate('mean').round(2)

# Write dataframe to a csv file
df_ratings.to_csv(output_file)
