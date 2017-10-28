#!/usr/bin/python3

# colour_bayes.py
# CMPT 318 Exercise 7 - Colour Words
# Alex Macdonald
# ID#301272281
# October 27, 2017

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from skimage.color import lab2rgb
import skimage.color
import sys
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer

# representative RGB colours for each label, for nice display
COLOUR_RGB = {
    'red': (255, 0, 0),
    'orange': (255, 114, 0),
    'yellow': (255, 255, 0),
    'green': (0, 230, 0),
    'blue': (0, 0, 255),
    'purple': (187, 0, 187),
    'brown': (117, 60, 0),
    'pink': (255, 187, 187),
    'black': (0, 0, 0),
    'grey': (150, 150, 150),
    'white': (255, 255, 255),
}
name_to_rgb = np.vectorize(COLOUR_RGB.get, otypes=[np.uint8, np.uint8, np.uint8])


def plot_predictions(model, lum=71, resolution=256):
    """
    Create a slice of LAB colour space with given luminance; predict with the model; plot the results.
    """
    wid = resolution
    hei = resolution
    n_ticks = 5

    # create a hei*wid grid of LAB colour values, with L=lum
    ag = np.linspace(-100, 100, wid)
    bg = np.linspace(-100, 100, hei)
    aa, bb = np.meshgrid(ag, bg)
    ll = lum * np.ones((hei, wid))
    lab_grid = np.stack([ll, aa, bb], axis=2)

    # convert to RGB for consistency with original input
    X_grid = lab2rgb(lab_grid)

    # predict and convert predictions to colours so we can see what's happening
    y_grid = model.predict(X_grid.reshape((wid*hei, 3)))
    pixels = np.stack(name_to_rgb(y_grid), axis=1) / 255
    pixels = pixels.reshape((hei, wid, 3))

    # plot input and predictions
    plt.figure(figsize=(10, 5))
    plt.suptitle('Predictions at L=%g' % (lum,))
    plt.subplot(1, 2, 1)
    plt.title('Inputs')
    plt.xticks(np.linspace(0, wid, n_ticks), np.linspace(-100, 100, n_ticks))
    plt.yticks(np.linspace(0, hei, n_ticks), np.linspace(-100, 100, n_ticks))
    plt.xlabel('A')
    plt.ylabel('B')
    plt.imshow(X_grid.reshape((hei, wid, 3)))

    plt.subplot(1, 2, 2)
    plt.title('Predicted Labels')
    plt.xticks(np.linspace(0, wid, n_ticks), np.linspace(-100, 100, n_ticks))
    plt.yticks(np.linspace(0, hei, n_ticks), np.linspace(-100, 100, n_ticks))
    plt.xlabel('A')
    plt.imshow(pixels)

def rgb_to_lab(rgb):
    lab = skimage.color.rgb2lab(rgb)
    return lab.reshape(-1, 3)

def main():
    data = pd.read_csv(sys.argv[1])

    # Import data into a NumPy array using as_matrix:
    # https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.as_matrix.html
    # From the reference: "Return is NOT a Numpy-matrix, rather, a Numpy-array."
    # X = data[['R', 'G', 'B']]/255
    X = data.as_matrix(columns=['R', 'G', 'B'])/255 # array with shape (n, 3). Divide by 255 so components are all 0-1.
    y = data['Label'].values # array with shape (n,) of colour words.

    # Partition your data into training and testing sets using train_test_split
    # Code for using train_test_split amended from documentation found at:
    # http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    # TODO: build model_rgb to predict y from X.
    # Now we're ready to create a naive Bayes classifier and train it
    # Code for using the model & prediction borrowed from the ML:Classification Lecture Slides
    model = GaussianNB()
    model_rgb = model.fit(X_train, y_train)
    y_predicted = model.predict(X_test)
    # TODO: print model_rgb's accuracy_score
    print("model_rgb: ", accuracy_score(y_test, y_predicted))

    # TODO: build model_lab to predict y from X by converting to LAB colour first.
    # There's no built-in transformer that does colour space conversion,
    # instead use function rgb2lab in a FunctionTransformer
    # Can create a pipeline where the first step is a transformer, and the second is a Gaussian
    # pipeline = make_pipeline(FunctionTransformer(rgb_to_lab), GaussianNB(priors=None))
    
    # Will need to do a little NumPy reshaping
    # Reshape the array of colours to an image 1 x n (.reshape(1, -1, 3))
    
    # Couldn't get the pipeline method to work as described in the exercise description
    # Instead, convert the X training data back to RGB and feed it to the rgb2lab function
    # Reshape back, and feed it into the gaussian model, continue as before.
    X_train = X_train * 255 # Convert back into RGB values
    X_re_train = X_train.reshape((1, -1, 3))
    X_lab = rgb_to_lab(X_re_train) # Convert to LAB values
    model = GaussianNB(priors=None)
    model_lab = model.fit(X_lab, y_train)
    y_predicted = model.predict(X_test)

    # TODO: print model_lab's accuracy_score
    print("model_lab: ", accuracy_score(y_test, y_predicted))

    # Do NOT have a plt.show()
    # colour_bayes.py should print two lines:
    # The (1) first and (2) secondary accuracy score
    plot_predictions(model_rgb)
    plt.savefig('predictions_rgb.png')
    plot_predictions(model_lab)
    plt.savefig('predictions_lab.png')


if __name__ == '__main__':
    main()

