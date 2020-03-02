"""
@Author: Alberto Geniola
@Date: 02-03-2020

This example script shows how simple is to get started with AutoKeras to build ML solvers for
certain complex tasks as image classification.

Before using the Google Vision API you need to install the autokeras library
    pip install --upgrade autokeras
    pip install --upgrade tensorflow
"""

import autokeras as ak
from tensorflow.keras.datasets import mnist


# -----------------------
# Load the MNIST dataset
# -----------------------
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# --------------------------------------------------------------------------------------------------
# SETUP THE IMAGE CLASSIFIER
# --------------------------------------------------------------------------------------------------
# Builds an image classifier, telling to the AutoKeras system to test up to 10 different models.
print("Defining classifier...")
clf = ak.ImageClassifier(max_trials=10)

# --------------------------------------------------------------------------------------------------
# AUTO TUNE
# --------------------------------------------------------------------------------------------------
# Train the classifier and select the best model (the one with highest accuracy)
print("Training...")
clf.fit(x_train, y_train, epochs=10)
print("Training completed")


# Evaluate on the testing data.
print("Measuring accuracy")
accuracy = clf.evaluate(x_test, y_test)
print('Accuracy: {accuracy}'.format(accuracy=accuracy))
