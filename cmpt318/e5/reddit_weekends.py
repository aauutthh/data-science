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
# import matplotlib.pyplot as plt

OUTPUT_TEMPLATE = (
    "Initial (invalid) T-test p-value: {initial_ttest_p:.3g}\n"
    "Original data normality p-values: {initial_weekday_normality_p:.3g} {initial_weekend_normality_p:.3g}\n"
    "Original data equal-variance p-value: {initial_levene_p:.3g}\n"
    "Transformed data normality p-values: {transformed_weekday_normality_p:.3g} {transformed_weekend_normality_p:.3g}\n"
    "Transformed data equal-variance p-value: {transformed_levene_p:.3g}\n"
    "Weekly data normality p-values: {weekly_weekday_normality_p:.3g} {weekly_weekend_normality_p:.3g}\n"
    "Weekly data equal-variance p-value: {weekly_levene_p:.3g}\n"
    "Weekly T-test p-value: {weekly_ttest_p:.3g}\n"
    "Mann–Whitney U-test p-value: {utest_p:.3g}"
)

# Perform the normal tests, levene test, and ttest
def perform_tests(weekends, weekdays):
    weekends_normaltest = stats.normaltest(weekends['comment_count'])
    weekdays_normaltest = stats.normaltest(weekdays['comment_count'])
    levene = stats.levene(weekends['comment_count'], weekdays['comment_count'])
    ttest = stats.ttest_ind(weekends['comment_count'], weekdays['comment_count'])
    return weekends_normaltest, weekdays_normaltest, levene, ttest

def main():
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

    # Separate the weekdays from the weekends
    # Credit to ggbaker for the hint about checking datetime.date.weekday
    weekends = reddit[(reddit['date'].dt.weekday >= 5)].reset_index() # 5 || 6 is a weekend
    weekdays = reddit[(reddit['date'].dt.weekday < 5)].reset_index() # < 5 is a weekday

    # Student's T-test
    initial_weekends_normaltest, initial_weekdays_normaltest, initial_levene, initial_ttest = perform_tests(weekends, weekdays)

    # Fix 1: transforming data might save us.
    # Create a copy of the dataframes, and apply a log transformation to it
    weekends_transformed = weekends.copy(deep=True)
    weekdays_transformed = weekdays.copy(deep=True)
    weekends_transformed['comment_count'] = np.log(weekends_transformed['comment_count'])
    weekdays_transformed['comment_count'] = np.log(weekdays_transformed['comment_count'])
    transformed_weekends_normaltest, transformed_weekdays_normaltest, transformed_levene, transformed_ttest = perform_tests(weekends_transformed, weekdays_transformed)
    # Used to show how well the np.log() normalized the data
    # plt.figure()
    # plt.hist(weekends_transformed['comment_count'])
    # plt.show()

    # Fix 2: the Central Limit Theorem might save us.
    # Combine all weekdays and weekend days from each year/week pair and take the mean of their non-transformed count
    # Add a week number and year column to the dataframes 
    weekends['week'] = weekends['date'].dt.week
    weekends['year'] = weekends['date'].dt.year
    weekdays['week'] = weekends['date'].dt.week
    weekdays['year'] = weekends['date'].dt.year

    # Group by the values, and take the mean
    mean_weekends = weekends.groupby(['week', 'year']).mean().reset_index()
    mean_weekdays = weekdays.groupby(['week', 'year']).mean().reset_index()
    mean_weekends.drop('index', axis=1, inplace=True)
    mean_weekends.groupby(mean_weekends.week).sum()
    mean_weekdays.drop('index', axis=1, inplace=True)
    # print(mean_weekends['comment_count'].sum())
    # print(mean_weekdays['comment_count'].sum())
    weekly_weekends_normaltest, weekly_weekdays_normaltest, weekly_levene, weekly_ttest = perform_tests(mean_weekends, mean_weekdays)

    # Fix 3: a non-parametric test might save us.
    # Use the Mann-Whitney test from scipy
    mann_whitney = stats.mannwhitneyu(weekends['comment_count'], weekdays['comment_count'])

    print(OUTPUT_TEMPLATE.format(
        initial_ttest_p=initial_ttest.pvalue,
        initial_weekday_normality_p=initial_weekdays_normaltest.pvalue,
        initial_weekend_normality_p=initial_weekends_normaltest.pvalue,
        initial_levene_p=initial_levene.pvalue,
        transformed_weekday_normality_p=transformed_weekdays_normaltest.pvalue,
        transformed_weekend_normality_p=transformed_weekends_normaltest.pvalue,
        transformed_levene_p=transformed_levene.pvalue,
        weekly_weekday_normality_p=weekly_weekdays_normaltest.pvalue,
        weekly_weekend_normality_p=weekly_weekends_normaltest.pvalue,
        weekly_levene_p=weekly_levene.pvalue,
        weekly_ttest_p=weekly_ttest.pvalue,
        utest_p=mann_whitney.pvalue,
    ))


if __name__ == '__main__':
    main()