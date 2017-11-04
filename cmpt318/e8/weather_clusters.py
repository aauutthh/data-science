#!/usr/bin/python3

# weather_clusters.py
# CMPT 318 Exercise 8 - Exploring the Weather
# Alex Macdonald
# ID#301272281
# November 3, 2017

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MinMaxScaler


def get_pca(X):
    """
    Transform data to 2D points for plotting. Should return an array with shape (n, 2).
    """
    flatten_model = make_pipeline(
        MinMaxScaler(),
        PCA(2)
    )
    X2 = flatten_model.fit_transform(X)
    assert X2.shape == (X.shape[0], 2)
    return X2


def get_clusters(X):
    """
    Find clusters of the weather data.
    """
    model = make_pipeline(
        MinMaxScaler(),
        KMeans(n_clusters=10)
    )
    model.fit(X)
    return model.predict(X)


def main():
    data = pd.read_csv(sys.argv[1])

    X = data
    y = data['city'].values
    X.drop(['city'], axis=1, inplace=True)
    X.drop(['year'], axis=1, inplace=True)

    X2 = get_pca(X)
    clusters = get_clusters(X)

    # Note: None of the qualitative colourmaps were working on my machine
    # So I used gnuplot just so the program wouldn't crash.
    plt.scatter(X2[:, 0], X2[:, 1], c=clusters, cmap='gnuplot', edgecolor='k', s=20)
    plt.savefig('clusters.png')

    df = pd.DataFrame({
        'cluster': clusters,
        'city': y,
    })
    counts = pd.crosstab(df['city'], df['cluster'])
    print(counts)


if __name__ == '__main__':
    main()