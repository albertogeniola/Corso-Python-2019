"""
@Author: Alberto Geniola
@Date: 02-03-2020

This example script shows how to rely on Google Vision API online ML model in order to classify
objects/detect faces and extract context labels from a images.

Before using the Google Vision API you need to:
    1. Register to Google Cloud Platform  -> http://console.cloud.google.com (python2019.camplus)
    2. Apply for the $300 credit          -> Simply click on the banner on the top. The process asks for a credit card
                                             but no charge is performed. Feel free to use an empty pre-paid card.
    3. Create a GCP project               -> Chose any name you like
    4. Enable Vision API                  -> search "Cloud Vision API" and enable
    5. Create a service account           -> vision-api-test, assign AutoML Prediction role, create a key
    6. Install vision library             -> pip install --upgrade google-cloud-vision

Note: Google Vision API is a pay-as-you-go service, so they are subject to costs. However, Google offers a
$ 300 waiver for newcomers, so you might be able to use this service for a while for free.
"""

import io
import os
from google.oauth2 import service_account

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Load the service account key
credentials = service_account.Credentials.from_service_account_file(
    'service-account.json',
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

# Instantiates a client
client = vision.ImageAnnotatorClient(credentials=credentials)

# The name of the image file to annotate
image1 = os.path.abspath('img/image1.jfif')
#image2 = os.path.abspath('img/image2.jfif')

# Loads the image into memory
with io.open(image1, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print("------------------------")
print("Labels:")
print("------------------------")
for label in labels:
    print(label.description)


# Perform face detection
response = client.face_detection(image=image)
faces = response.face_annotations

# Names of likelihood from google.cloud.vision.enums
likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                   'LIKELY', 'VERY_LIKELY')
print("\n------------------------")
print("Face detection:")
print("------------------------")
for face in faces:
    print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
    print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
    print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

    vertices = (['({},{})'.format(vertex.x, vertex.y)
                for vertex in face.bounding_poly.vertices])

    print('face bounds: {}'.format(','.join(vertices)))


# Performs object detection
print("\n------------------------")
print("Object detection:")
print("------------------------")
objects = client.object_localization(image=image).localized_object_annotations
for object_ in objects:
        print('\n{} (confidence: {})'.format(object_.name, object_.score))
        print('Normalized bounding polygon vertices: ')
        for vertex in object_.bounding_poly.normalized_vertices:
            print(' - ({}, {})'.format(vertex.x, vertex.y))


