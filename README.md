# pynumdraw

This project is a very simple web application where you draw a number on the provided canvas and click "predict". That canvas data is converted into json and sent to the backend RESTful Flask API. This backend API then preprocesses the json data, passes it into a trained neural network (trained on MNIST), and then reports back both the prediction of what number you drew and the confidence of that prediction.

**I wish I could say that this project was my idea, but I saw this project presented on YouTube at a conference. I can't seem to find either the presentation nor the github repo for who originally built a project like this. I used that to my advantage and tried to implement the concept myself - learning quite a bit in the process.**



## Why I made this project:

There were a number of things I wanted to test out by building this project:


* bjoern wsgi (I like how this is a python package with extension written in C rather than an OS package)
* nginx reverse proxy into the bjoern wsgi
* converting a canvas drawing into JSON
* exposing a "deep learning" model 
* returning those results from the model to the front end



## What's missing from this project (potential Phase 2):

* the front end leaves much to be desired (very ugly)
	- css lives in a style tag
	- javascript lives in a script tag
* deployment / CI pipeline
* tests for the API (only a single route with a single way it can be called, so this feels low risk)
* proper logging
* I use the term "confidence" very loosely in terms of what the model provides
	- this is really just the maximum value of the last layer of the neural network before it goes into softmax
	- I'd love to come back and figure out a way to make it less confident about things that clearly aren't numbers


## Data for model training:

I wanted to use the actual raw data from the [MNIST site](http://yann.lecun.com/exdb/mnist/) for training my neural network (never pass up an opportunity to dip down into the raw bytes of a weird file format you're not familiar with).

So in the `/data/` directory of this project root, you should put the following files:

* t10k-images-idx3-ubyte  
* t10k-labels-idx1-ubyte  
* train-images-idx3-ubyte  
* train-labels-idx1-ubyte

