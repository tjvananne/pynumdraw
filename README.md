# pynumdraw
Very simple web application where you draw a number on the provided canvas and click "predict". That canvas data is converted into json and sent to the backend RESTful Flask API. This backend API then preprocesses the json data, passes it into a trained neuralnetwork (trained on MNIST), and then reports back both the prediction and the confidence of that prediction.
