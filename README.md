# pynumdraw


![demo gif](pynumdraw.gif)


This project is a very simple web application where you draw a number on the provided canvas and click "predict". That canvas data is converted into json and sent to the backend RESTful Flask API. This backend API then preprocesses the json data, passes it into a trained neural network (trained on MNIST), and then reports back both the prediction of what number you drew and the confidence of that prediction.

**I wish I could say that this project was my idea**, but I saw this project presented on YouTube at a conference. I can't seem to find either the presentation nor the github repo for who originally built a project like this. I used that to my advantage and tried to implement the concept myself - learning quite a bit in the process.


## Why I made this project:

[This article](https://stackoverflow.blog/2020/03/05/a-modern-hello-world-program-needs-more-than-just-code/) talking about the "modern-day 'Hello World!'" application really resonated with me. There was a time where it wasn't trivial to create a "Hello World!" program. There were no friendly interpreters and virtual machines that provided guardrails for all the things that can go wrong in a program. That doesn't mean we should do away with the "Hello World!" philosophy, it just means that we can make our "Hello World!" programs that much more powerful/expressive. 

There were also many technologies / techniques I wanted to test out by building this project:


* bjoern wsgi (I like how this is a python package with extension written in C rather than an OS package)
* nginx reverse proxy into the bjoern wsgi
* converting a canvas drawing into JSON
* exposing a "deep learning" model (trained with Tensorflow 2.0.1 and `tensorflow.keras` instead of stand-alone keras)
* returning those results from the model to the front end
* using tmux to execute background jobs
* maybe docker / kubernetes as an alternate deployment method (phase 2?)



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


## Deployment steps

1. You'll need to edit the `deploy_remote.sh` and `deploy_dev.sh` shell scripts. I'm using git-bash to execute those shell commands. I'm also using Lubuntu 18.04 (basically Ubuntu) in virtualbox as my local development environment. 


## Using `tmux` with anaconda:

I haven't scripted anything yet with tmux, but [these are the general high level steps](https://askubuntu.com/questions/8653/how-to-keep-processes-running-after-ending-ssh-session) I'm using in order to execute my python prediction server in the background. It's also worth noting that I'm using miniconda environments in my project. It seems like tmux and conda sometimes don't play nice, but [here](https://unix.stackexchange.com/questions/366553/tmux-is-causing-anaconda-to-use-a-different-python-source) is the solution to that. You have to make sure your conda environment has been activated before entering tmux to run the prediction server.

Steps (on remote server):

1. activate conda environment being used by the project: `source activate pynumdraw`
2. navigate to the back end directory
3. create a tmux session: `tmux`
4. run the script: `python prediction_server.py`
5. detatch from the tmux session: `CTRL+b; d`


## Front-end canvas resources

* [SO Post](https://stackoverflow.com/questions/60688935/my-canvas-drawing-app-wont-work-on-mobile) and associated [code pen](https://codepen.io/mero789/pen/qBdYWxY)
* Current limitation/issue on desktop browsers when user zooms in on the browser. The area where they are drawing on the canvas no longer aligns with cursor location. Doesn't appear to be an issue on mobile. Best collection of answers at this [SO Post](https://stackoverflow.com/questions/995914/catch-browsers-zoom-event-in-javascript). I think Abilogos has the best answer so far.



