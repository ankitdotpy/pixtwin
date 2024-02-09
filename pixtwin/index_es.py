import os
import csv
import time
import requests
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import tensorflow as tf
from search import Search

MAX_IMAGES = 200000

base_model = tf.keras.applications.VGG16(weights='imagenet', include_top=False)
feature_extractor = tf.keras.models.Model(inputs=base_model.input, outputs=base_model.get_layer('block5_pool').output)

def encode_image(image_path):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.vgg16.preprocess_input(img_array)
    features = feature_extractor.predict(img_array)
    flattened_features = features.flatten()
    encoded_features = flattened_features[:512]
    return encoded_features


if __name__ == '__main__':
    es = Search()
    es.create_index()
    
    with open('./dataset/google_image_url.txt') as file:
        reader = csv.reader(file)
        cnt = 1
        for row in reader:
            image_path = tf.keras.utils.get_file('image.jpg', row[0])
            image_vector = encode_image(image_path)
            body = {
                'image': row[0],
                'image_vector': image_vector
            }
            res = es.insert_document(document=body)
            # print(res)
            if cnt == MAX_IMAGES:
                break

            cnt+=1
        