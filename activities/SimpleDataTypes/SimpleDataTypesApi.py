# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
import string
import random

# creating a Flask app
app = Flask(__name__)


# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
@app.route('/', methods = ['GET'])
def home():
    if(request.method == 'GET'):

        data = "hello world"
        return jsonify({'data': data})

@app.route('/string/<int:length>', methods = ['GET'])
def generate_strings(length):
    rsp = []
    for i in range(length):
        rsp.append(random.choice(string.ascii_letters))

    return jsonify({'data': rsp})

@app.route('/integer/<int:length>', methods = ['GET'])
def generate_integers(length):
    rsp = []
    for i in range(length):
        rsp.append(int(random.random()*100))

    return jsonify({'data': rsp})

@app.route('/float/<int:length>', methods = ['GET'])
def generate_floats(length):
    rsp = []
    for i in range(length):
        rsp.append(random.random()*100)

    return jsonify({'data': rsp})


# driver function
if __name__ == '__main__':

    app.run(debug = True)
