#!/usr/bin/python3

# ab_analysis.py
# CMPT 318 Exercise 8 - Case of the Unlabelled Weather
# Alex Macdonald
# ID#301272281
# November 3, 2017

# Reads the labelled data and trains a machine learning model
# It should predict the cities where the unlabelled 2016 weather came from

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# python3 weather_city.py monthly-data-labelled.csv monthly-data-unlabelled.csv labels.csv
labelled = pd.read_csv(sys.argv[1])
unlabelled = pd.read_csv(sys.argv[2])

X = labelled
y = labelled['city'].values
X.drop(['city'], axis=1, inplace=True)
X.drop(['year'], axis=1, inplace=True)

X_train, X_test, y_train, y_test = train_test_split(X, y)

# Credit to ggbaker for giving the hint to use StandardScaler
# Documentation found at: http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html
model = make_pipeline(
  StandardScaler(),
  SVC(kernel='linear')
)
model.fit(X_train, y_train)

unlabelled.drop(['city'], axis=1, inplace=True)
unlabelled.drop(['year'], axis=1, inplace=True)
predictions = model.predict(unlabelled)

# The output format should be one city name per line:
pd.Series(predictions).to_csv(sys.argv[3], index=False)

# Program should print one line: the "score" of the model you're using on a testing subset of the labelled data
print(model.score(X_test, y_test))