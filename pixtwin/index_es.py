import os
import csv
import time
import requests
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import tensorflow as tf
from vit_keras import vit, utils
from search import Search

MAX_IMAGES = 200000
IMAGE_SIZE = 384

model = vit.vit_b16(
    image_size=IMAGE_SIZE,
    activation='sigmoid',
    pretrained=True,
    include_top=False,
    pretrained_top=False
)

def encode_image(image_path):
    image = utils.read(image_path, IMAGE_SIZE)
    X = vit.preprocess_inputs(image).reshape(1, IMAGE_SIZE, IMAGE_SIZE, 3)
    encoded_features = model.predict(X)
    return encoded_features[0]

if __name__ == '__main__':
    es = Search()
    es.create_index()

    with open('./dataset/google_image_url.txt') as file:
        reader = csv.reader(file)
        cnt = 1
        for row in reader:
            image_path = tf.keras.utils.get_file('image.jpg', row[0])
            image_vector = encode_image(image_path).tolist()
            body = {
                'image': row[0],
                'image_vector': image_vector
            }
            res = es.insert_document(document=body)
            # print(res)
            if cnt == MAX_IMAGES:
                break

            cnt+=1
        