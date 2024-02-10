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
# IMAGE_SIZE = 384

# model = vit.vit_b16(
#     image_size=IMAGE_SIZE,
#     activation='sigmoid',
#     pretrained=True,
#     include_top=False,
#     pretrained_top=False
# )

# def encode_image(image_path):
#     image = utils.read(image_path, IMAGE_SIZE)
#     X = vit.preprocess_inputs(image).reshape(1, IMAGE_SIZE, IMAGE_SIZE, 3)
#     encoded_features = model.predict(X)
#     return encoded_features[0]

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
            try:
                image_path = tf.keras.utils.get_file('image.jpg', row[0])
            except Exception as exp:
                print(f'error fetching {row[0]} - {exp}')
                continue

            image_vector = encode_image(image_path).tolist()
            os.remove(image_path)

            body = {
                'image': row[0],
                'image_vector': image_vector
            }
            res = es.insert_document(document=body)
            # print(res)
            if cnt == MAX_IMAGES:
                break

            cnt+=1
        