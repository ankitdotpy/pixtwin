import os
import csv
import time
import requests
import warnings
warnings.filterwarnings('ignore')

import tensorflow as tf
from search import Search


es = Search()

if __name__ == '__main__':
    with open('./dataset/google_image_url.txt') as file:
        reader = csv.reader(file)
        id = 1
        for row in reader:
            image_path = tf.keras.utils.get_file('image.jpg', row[0])
            image = tf.keras.preprocessing.image.load_img(image_path)
            image_arr = tf.keras.preprocessing.image.img_to_arr(image)
            image_vector = None
            body = {
                'image': row[0],
                'image_vector': image_vector
            }
            res = es.index(index=es.index, id=id, body=body)
            # print(res)
            cnt+=1