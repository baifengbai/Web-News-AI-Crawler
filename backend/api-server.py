# import the necessary packages
import numpy as np
import flask
import io
import pandas as pd
import tensorflow as tf
import keras
from keras.models import load_model

# initialize our Flask application and the Keras model
app = flask.Flask(__name__)
model = None

def filter_data(string):
    '''
    Removes usless characters
    '''
    filtered = string.replace('<p class="p1"><span class="s1">',' ')
    filtered = filtered.replace('<p ',' ')
    filtered = filtered.replace('<dev>',' ')
    return filtered

def preprocess_data(stored_contents):
    from keras.preprocessing.text import text_to_word_sequence, one_hot
    from keras.preprocessing.sequence import pad_sequences

    #see: https://machinelearningmastery.com/prepare-text-data-deep-learning-keras/
    
    # tokenize the document
    word_sequence=text_to_word_sequence(filter_data(stored_contents))
    words = set(word_sequence) #set() "groups by" the characters filtering duplicaded ones
    vocab_size=len(words) #getting vocabulary size, this will be the input 
    tokenized_array=one_hot(stored_contents, round(vocab_size)) #one hot encoding input data

    #data_to_predict = pad_sequences(tokenized_array, maxlen = 9000)
    #return data_to_predict
    return tokenized_array

# instantiate flask 
app = flask.Flask(__name__)

# define a predict function as an endpoint 
@app.route("/predict", methods=["GET","POST"])
def predict():
    data = {"success": False, "predictions": []}

    params = flask.request.json
    if (params == None):
        params = flask.request.args

    # if parameters are found, return a prediction
    if (params != None):
            
            data_to_predict=preprocess_data(params['input'])
            model=load_model('models/rss_model.h5') #requieres keras 2.2.4!!!
            results = model.predict(data_to_predict)
            data["predictions"] = []

            for prob in results:
                r = float(prob)
                data["predictions"].append(r)
            # indicate that the request was a success
            data["success"] = True

    # return a response in json format 
    return flask.jsonify(data)    

# start the flask app, allow remote connections 
app.run(host='0.0.0.0')