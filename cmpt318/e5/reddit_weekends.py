#!/usr/bin/python3

# reddit_weekends.py
# CMPT 318 Exercise 5 - Reddit Weekends
# Alex Macdonald
# ID#301272281
# October 13, 2017

# Are there a different number of Reddit comments posted on weekdays than on weekends?

import sys
import gzip
import numpy as np
import pandas as pd
from scipy import stats

# Read the gzipped file with the built in Pandas funciton
reddit_filename = sys.argv[1]
reddit_fh = gzip.open(reddit_filename, 'rt', encoding='utf-8')
reddit = pd.read_json(reddit_fh, lines=True)


# We will only look at values:
# 1. in 2012 and 2013
# Code for identifying specific dates in a df row borrowed from:
# https://stackoverflow.com/questions/28629154/pandas-python-deleting-rows-based-on-date-column
reddit = reddit[(reddit['date'].dt.year == 2012) | (reddit['date'].dt.year == 2013)]
# 2. In the /r/canada subreddit
reddit = reddit[reddit['subreddit'] == "canada"]
reddit.drop('subreddit', axis=1, inplace=True)

# Separate the weekdays from the weekends
# Credit to ggbaker for the hint about checking datetime.date.weekday 5 || 6
weekends = reddit[(reddit['date'].dt.weekday == 5) | (reddit['date'].dt.weekday == 6)].reset_index()
weekdays = reddit[(reddit['date'].dt.weekday != 5) & (reddit['date'].dt.weekday != 6)].reset_index()

# Studen't T-test
# stats.t
# Fix 1: transforming data might save us.
# Fix 2: the Central Limit Theorem might save us.
# Fix 3: a non-parametric test might save us.
print (weekends)



# OUTPUT_TEMPLATE = (
#     "Initial (invalid) T-test p-value: {initial_ttest_p:.3g}\n"
#     "Original data normality p-values: {initial_weekday_normality_p:.3g} {initial_weekend_normality_p:.3g}\n"
#     "Original data equal-variance p-value: {initial_levene_p:.3g}\n"
#     "Transformed data normality p-values: {transformed_weekday_normality_p:.3g} {transformed_weekend_normality_p:.3g}\n"
#     "Transformed data equal-variance p-value: {transformed_levene_p:.3g}\n"
#     "Weekly data normality p-values: {weekly_weekday_normality_p:.3g} {weekly_weekend_normality_p:.3g}\n"
#     "Weekly data equal-variance p-value: {weekly_levene_p:.3g}\n"
#     "Weekly T-test p-value: {weekly_ttest_p:.3g}\n"
#     "Mann–Whitney U-test p-value: {utest_p:.3g}"
# )


# def main():
#     reddit_counts = sys.argv[1]

#     # ...

#     print(OUTPUT_TEMPLATE.format(
#         initial_ttest_p=0,
#         initial_weekday_normality_p=0,
#         initial_weekend_normality_p=0,
#         initial_levene_p=0,
#         transformed_weekday_normality_p=0,
#         transformed_weekend_normality_p=0,
#         transformed_levene_p=0,
#         weekly_weekday_normality_p=0,
#         weekly_weekend_normality_p=0,
#         weekly_levene_p=0,
#         weekly_ttest_p=0,
#         utest_p=0,
#     ))


# if __name__ == '__main__':
#     main()