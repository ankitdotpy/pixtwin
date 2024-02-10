import numpy as np
from pprint import pprint

import tensorflow as tf
from vit_keras import vit, utils
from search import Search
from flask import Flask, render_template, request

app = Flask(__name__)
es = Search()

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
#     return encoded_features[0].tolist()

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

@app.route('/', methods=['GET', 'POST'])
def index():
    images = []
    if request.method == 'POST':
        if 'image' in request.files:
            image_file = request.files['image']
            image_path = 'uploads/' + image_file.filename
            image_file.save(image_path)
            query_vector = encode_image(image_path)
            result = es.similarity_by_nn(query_vector)
            images = [{
                'url': hit['_source']['image'],
                'score': hit['_score']
            } for hit in result['hits']['hits']]

    return render_template('index.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)
