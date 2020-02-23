"""
@Author: Alberto Geniola
@Date: 09/02/2020
@Description:
  MNIST image classifier example using Linear Regression.
  Please note that in order to run this script, you might need some RAM memory (>4Gb).
  Python x64 bit version runs it better as it can leverage large memory space.

  Before running this script, make sure you have installed all the required dependencies.
  pip3 install scikit-learn matplotlib numpy
"""
# Importing libraries
from sklearn.datasets import fetch_openml               # Dataset utility to fetch data from public datasets
from sklearn.model_selection import train_test_split    # Library used to split dataset into portions
from sklearn.linear_model import LogisticRegression       # Implementation of LinearRegression
import matplotlib                                       # Library used to plot images/charts
import matplotlib.pyplot as plt
import numpy as np                                      # Numerical manipulation library


# --------------------------------------------------------------------------------------------------
# DATA COLLECTION PHASE
# --------------------------------------------------------------------------------------------------
# Loading public MNIST dataset: 28x28 pixel, grayscale (0 to 255)
# The mnist dataset contains 70.000 images of hand-written digits (from 0 to 9).
# Each image is a 28x28 matrix = 784 pixels. Each pixel is in gray scale.
# An integer represents the quantity of "black ink": 0 means totally WHITE, 255 means totally BLACK.
print("Loading public MNIST dataset...")
mnist = fetch_openml('mnist_784', data_home="./data")
print("Data loaded.")

# --------------------------------------------------------------------------------------------------
# TEST SET PREPARATION
# --------------------------------------------------------------------------------------------------
# Split arrays or matrices into random train and test subsets
x_train, x_test, y_train, y_test = train_test_split(mnist.data, mnist.target, test_size=0.15, random_state=0)

# --------------------------------------------------------------------------------------------------
# TRAINING
# --------------------------------------------------------------------------------------------------
ml_alg = LogisticRegression(max_iter=200)
trained_model = ml_alg.fit(x_train, y_train)

# --------------------------------------------------------------------------------------------------
# TEST
# --------------------------------------------------------------------------------------------------
predictions = trained_model.predict(x_test)
score = trained_model.score(x_test, y_test)
print("----------------------------------------------")
print("Model Accuracy: {}".format(score))
print("----------------------------------------------")

# --------------------------------------------------------------------------------------------------
# Display misclassified images
# --------------------------------------------------------------------------------------------------
index = 0
misclassifiedIndexes = []
for label, predict in zip(y_test, predictions):
    if label != predict:
        misclassifiedIndexes.append(index)
        index += 1

plt.figure(figsize=(20, 4))
for plotIndex, badIndex in enumerate(misclassifiedIndexes[0:5]):
    plt.subplot(1, 5, plotIndex + 1)
    plt.imshow(np.reshape(x_test[badIndex], (28, 28)), cmap=plt.cm.gray)
    plt.title("Predicted: {}, Actual: {}".format(predictions[badIndex], y_test[badIndex]), fontsize=15)

plt.show()
input("Press ENTER to exit")