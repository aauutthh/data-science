#!/usr/bin/python3

# average_ratings.py
# CMPT 318 Exercise 4 - Movie Title Entity Resolution
# Alex Macdonald
# ID#301272281
# October 6, 2017

import sys
import numpy as np
import pandas as pd

movie_list = sys.argv[1]
movie_ratings = sys.argv[2]
outupt_file = sys.argv[3]

lines = open(movie_list).read().splitlines()
df_list = pd.DataFrame(lines, columns=["title"])

ratings = open(movie_ratings).read().splitlines()
df_ratings = pd.DataFrame(ratings, columns=["all"])
df_ratings["all"]drop(df_ratings["all"].index[[0]])
# df_ratings['title'].set_index('title', inplace=True);
df_ratings['title'] = df_ratings['all'].str.extract('(.*?),\d\d?$', expand=True)
# df_ratings['rating'].set_index('rating', inplace=True);
df_ratings['rating'] = df_ratings['all'].str.extract('.*?,(\d\d?)$', expand=True)
df_ratings.drop('all', axis=1, inplace=True)
print(df_ratings)

# Objective: 
# . Determin the average rating for each movie, compensating for bad spelling
# . It should produce a CSV file with 'title' as the first column
# . . and (average) 'rating' rounded to two decimal places as the second
# . The output should be sorted by title.


# ratings.to_csv(output_file)