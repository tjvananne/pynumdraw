#!/usr/bin/env python
# coding: utf-8

# # This will be the file that is converted to a .py and deployed to server

# In[ ]:


print("importing...")
import numpy as np
import tensorflow as tf
import tensorflow.keras as keras
from skimage.io import imread
from skimage.transform import resize
from flask import Flask, request, jsonify
import json



# In[ ]:


# load model immediately
print("loading tensorflow model weights...")
probability_model = keras.models.load_model(filepath='pynumdraw_model.hdf5', compile=False)





app = Flask(__name__)


# def predict_number_test(data):
#     print("in predict_number function now")
#     print(type(data))
#     print(data.keys())
#     print(type(data['new_data']))
#     print(len((data['new_data'])))
#     print(data['new_data'][0:10])

#     results = {}

#     # new_data = reshape_and_resize_image(data['new_data'])
#     new_data = np.asarray(data['new_data']).reshape((1, 28, 28))
#     predicted_probabilities = probability_model.predict(new_data)
#     # results["predicted_probabilities"] = predicted_probabilities
#     results["predicted_number"] = int(np.argmax(predicted_probabilities))
#     results["confidence"] =  str(int(100 * np.max(predicted_probabilities)))

#     return json.dumps(results)


@app.route('/predict_number/', methods=['POST'])
def predict_number():
    print("in predict_number function now")
    data = request.json
    print(type(data))
    print(data.keys())
    print(type(data['new_data']))
    print(len((data['new_data'])))
    print(data['new_data'][0:10])

    results = {}

    new_data = reshape_and_resize_image(data['new_data'])
    predicted_probabilities = probability_model.predict(new_data)
    # results["predicted_probabilities"] = predicted_probabilities
    results["predicted_number"] = int(np.argmax(predicted_probabilities))
    results["confidence"] =  str(int(100 * np.max(predicted_probabilities)))

    return jsonify(results)

@app.route("/hello/")
def hello():
    print("in hello function now")
    return "hello_world"



# In[ ]:


def read_mnist_image_data(image_data_file):
    """
    image_data_file: path to the mnist image data file on disk.
    
    returns a dictionary with the following keys:
    - magic_number: to be compared against the magic number for each file on MNIST website
    - number_of_images: the number of images included in the dataset
    - pixel_rows: the number of pixels per row per image
    - pixel_cols: the number of pixels per column per image
    - data: the actual image data as ndarray with shape of (number_of_images, pixel_rows, pixel_cols)
    """
    
    results = {}
    
    with open(image_data_file, 'rb') as f:
        _data = f.read()
        
    results['magic_number'] = int.from_bytes(_data[0:4], 'big')
    results['number_of_images'] = int.from_bytes(_data[4:8], 'big')
    results['pixel_rows'] = int.from_bytes(_data[8:12], 'big')
    results['pixel_cols'] = int.from_bytes(_data[12:16], 'big')
    
    pixel_data = np.asarray([pixel for pixel in _data[16:]])
    pixel_data = pixel_data.reshape(results['number_of_images'], results['pixel_rows'], results['pixel_cols'])
    results['data'] = pixel_data
    
    return results



def read_mnist_label_data(label_data_file):
    """
    label_data_file: path to the mnist label data file on disk.
    
    returns a dictionary with the following keys:
    - magic_number: to be compared against the magic number for each file on MNIST website
    - number_of_labels: the number of labels included in the dataset
    - labels: the actual label data as ndarray (1 dimensional)
    """
    
    results = {}
    
    with open(label_data_file, 'rb') as f:
        _data = f.read()
        
    results['magic_number'] = int.from_bytes(_data[0:4], 'big')
    results['number_of_labels'] = int.from_bytes(_data[4:8], 'big')    
    results['labels'] = np.asarray([(label / 1.0) for label in _data[8:]]).astype('int')
    
    return results


# In[ ]:


def reshape_and_resize_image(p_image_data):
    
    """
    expect a one-dimensional list of pixel values that make up a single-channel 300x300 pixel image.
    The pixels are in row-wise order. 
    
    #expected_pixel_width = 300
    #expected_pixel_height = 300
    #model_required_pixel_width = 28
    #model_required_pixel_height = 28
    """
    
    
    # we're expecting a 300x300 pixel image (one channel) from our front-end
    x = np.asarray(p_image_data)
    x = x.reshape(300, 300)
    x = resize(x, output_shape=(28, 28))
    x = x.reshape(1, 28, 28)
    return x
    


# In[ ]:



import bjoern


print("starting bjoern server now!")
bjoern.run(app, '127.0.0.1', 8080)

