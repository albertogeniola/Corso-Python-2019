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
from sklearn.linear_model import LogisticRegression     # Implementation of LinearRegression
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
# Split arrays or matrices into random train and test subsets. We use 15% of the samples as test-set.
x_train, x_test, y_train, y_test = train_test_split(mnist.data, mnist.target, test_size=0.15, random_state=0)

# --------------------------------------------------------------------------------------------------
# TRAINING
# --------------------------------------------------------------------------------------------------
ml_alg = LogisticRegression(max_iter=500)
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
# Display charts
# --------------------------------------------------------------------------------------------------
index = 0
misclassifiedIndexes = []
misclassifications = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for label, predict in zip(y_test, predictions):
    if label != predict:
        misclassifiedIndexes.append(index)
    misclassifications[int(label)] += 1
    index += 1


# Calculate the misclassification %
misclassifications_perc = []
for i, num in enumerate(misclassifications):
    perc = num * 100 / y_test
    misclassifications_perc[i] = perc


# Display some misclassified images
plt.figure(figsize=(15, 4))
plt.title("Wrong prediction samples", fontsize=15)
for plotIndex, badIndex in enumerate(misclassifiedIndexes[0:5]):
    plt.subplot(1, 5, plotIndex + 1)
    plt.imshow(np.reshape(x_test[badIndex], (28, 28)), cmap=plt.cm.gray)
    plt.title("Predcted: {}, Actual: {}".format(predictions[badIndex], y_test[badIndex]), fontsize=15)

plt.show()


# Let's plot accuracy
fig = plt.figure()
plt.title("Wrong predictions by digit", fontsize=15)
error_ax = fig.add_subplot(1, 1, 1)  # create an axes object in the figure
perc_ax = fig.add_subplot(1, 1, 2)  # create an axes object in the figure
error_ax.set_ylabel("Wrong predictions")
perc_ax.set_ylabel("Wrong predictions")
labels = ['0','1','2','3','4','5','6','7','8','9']
error_ax.bar(labels, misclassifications, color="red")
perc_ax.bar(labels, misclassifications_perc, color="red")
plt.show()


input("Press ENTER to exit")