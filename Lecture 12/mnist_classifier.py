"""
@Author: Alberto Geniola
@Date: 09/02/2020
@Description:
  MNIST image classifier example using Decision Tree.
  This python script takes advantage of scikit-learn library in order to apply decision tree ML algorithm
  to the famous MNIST problem. MNIST dataset is fetched from OpenML data.
  Please note that in order to run this script, you might need some RAM memory (>4Gb).
  Python x64 bit version runs it better as it can leverage large memory space.

  Before running this script, make sure you have installed all the required dependencies.
  pip install pip3 install scikit-learn matplotlib numpy
"""
# Importing libraries
from sklearn.datasets import fetch_openml           # Dataset utility to fetch data from public datasets
from sklearn.tree import DecisionTreeClassifier     # Implementation of a DecisionTree classifier
import random                                       # We'll use it to randomly select the training set
import matplotlib                                   # Library used to plot images/charts
import matplotlib.pyplot as plt
import numpy as np                                  # Numerical manipulation library


# Loading public MNIST dataset: 28x28 pixel, grayscale (0 to 255)
# The mnist dataset contains 70.000 images of hand-written digits (from 0 to 9).
# Each image is a 28x28 matrix = 784 pixels. Each pixel is in gray scale.
# An integer represents the quantity of "black ink": 0 means totally WHITE, 255 means totally BLACK.
print("Loading public MNIST dataset...")
mnist = fetch_openml('mnist_784', data_home="./data")
print("Data loaded.")

x_data = mnist.data.tolist()
y_data = mnist.target.tolist()

# Let's split the set into TRAINING and TEST SET.
# Let's use 60.000 records as training set and 10.000 records as test-set
train_x = []
train_y = []
while len(train_x) < 60000:
    random_index = random.randint(0, len(x_data)-1)
    x = x_data.pop(random_index)
    y = y_data.pop(random_index)
    train_x.append(x)
    train_y.append(y)

test_x = x_data
test_y = y_data

print("Training set and test set created. Training set size: %d, Test set size: %d" % (len(train_x), len(test_x)))

# Let's train the algorithm on the input data
tree_clf = DecisionTreeClassifier()
print("Training the algorithm...")
trained_model = tree_clf.fit(train_x, train_y)
print("Training ended")


# Let's pick a random image from the test-set
i = 0
while True:
    # Select the next item of the test_set
    test_input = test_x[i]
    test_label = test_y[i]

    # Now apply the prediction
    predicted_value = trained_model.predict([test_input])
    # Print some info
    print("Expected output: %s" % test_label)
    print("Predicted output: %s" % predicted_value)
    if test_label == predicted_value:
        print("Awesome! The algorithm was right!")
    else:
        print("Too bad: the algorithm was wrong...")

    # Plot the item
    test_input_plt = np.asarray(test_x[i]).reshape(28, 28)
    plt.imshow(test_input_plt, cmap=matplotlib.cm.binary, interpolation="nearest")
    plt.text(0, 0, "Expected: %s. Predicted: %s" % (test_label, predicted_value))
    plt.axis("off")
    print("Expected label: %s" % test_y[i])
    plt.show()

    selection = input("Do you want to test it again? [y/n]")
    if selection.lower().strip() != 'y':
        break
    plt.close()
    i += 1


# Let's evaluate the model
wrong_predictions = {}
digit_count = {
    '0': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0}

for i in range(0, len(test_x)):
    x = test_x[i]
    y = test_y[i]
    predicted_value = trained_model.predict([x])

    # Keep track for every label of the missed predictions
    if y != predicted_value:
        errors = wrong_predictions.get(y, 0)
        wrong_predictions[y] = errors + 1

    # Also count total digit occurrences
    digit_count[y]+=1

# Let's print error rate
for y in wrong_predictions:
    precision = (1 - wrong_predictions[y])/digit_count[y]
    print("{label}: {errors_label}".format(label=y, errors_label=wrong_predictions[y]))

# Let's plot it!
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
labels = wrong_predictions.keys()
errors = wrong_predictions.values()
ax.bar(labels, errors)
plt.show()
