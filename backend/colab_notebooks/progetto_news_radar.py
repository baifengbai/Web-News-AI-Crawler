from time import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from keras.utils import to_categorical

from keras.models import Sequential
from keras.layers import Dense

import feedparser
import time
import json
from subprocess import check_output
import pymongo
import sys
import re
import csv


def save_pickle(contents):
    #saving data to file
    train_dataset={}
    for i in range(0, len(contents)):
        train_dataset[i] = (contents[i], responses[i])
        
    try:
        import cPickle as pickle
    except ImportError:  # python 3.x
        import pickle

    with open('/content/drive/My Drive/Colab Notebooks/datasets/rss_train_dataset.p', 'wb') as fp:
        pickle.dump(train_dataset, fp, protocol=pickle.HIGHEST_PROTOCOL)

def load_pickle():
    #load saved data
    with open('/content/drive/My Drive/Colab Notebooks/datasets/rss_train_dataset.p', 'rb') as fp:
        data = pickle.load(fp)

def filter_data(string):
  '''
  THis removes usless characters
  '''
  filtered = string.replace('<p class="p1"><span class="s1">',' ')
  filtered = filtered.replace('<p ',' ')
  filtered = filtered.replace('<dev>',' ')
  return filtered

client = pymongo.MongoClient("mongodb://rio:onslario89@riohomecloud.ddns.net:27017")
db = client.rss_news

f = open('/content/drive/My Drive/Colab Notebooks/datasets/feed_list.txt', "r")
lines = f.readlines()
#contents=[]
#responses=[]
#for url in lines:
#    feed = feedparser.parse(url)
#    feed_name=feed['feed']['title']
#    mydocs = db[feed_name].find()
#    for i in range(0, mydocs.count()):
#        print("Title ", i, ": ", mydocs[i]['title'])
#        responses.append(input("are you interested (answer with 0 or 1): "))

#for url in lines:
feed = feedparser.parse('https://www.wired.com/feed/rss')
feed_name=feed['feed']['title']
mydocs = db[feed_name].find()
sum=0
for i in range(0, mydocs.count()):
  sum=sum+1
  contents.append(mydocs[i]['summary'])
      
print("Current feed: ", sum)      
len(contents)    
            #contents.append(mydocs[i]['summary'])
   
#data_array=contents
#y_train=responses

#putting data to arrays for RNN
data_array=contents
y_train=responses

#turning str responses to int 
y_train = [ int(x) for x in y_train ]
print(len(y_train))
print(type(y_train[0]))

#filtering data
for i in range(0, len(data_array)):
  data_array[i]=filter_data(data_array[i])

print(data_array[0])
print(len(data_array))

#data preparation

#The phrases must be converted into array or words sequence
#i.e. "After two years of work, the wrapper comes off" -> "After, two, years, of, work, the, wrapper, comes, off"
#this is being done by the text_to_word_sequence() method

from keras.preprocessing.text import text_to_word_sequence, one_hot
from keras.preprocessing.sequence import pad_sequences

#see: https://machinelearningmastery.com/prepare-text-data-deep-learning-keras/

tokenized_array=[]

# tokenize the document
for i in range(0, len(data_array)):
  word_sequence=text_to_word_sequence(filter_data(data_array[i]))
  words = set(word_sequence) #set() "groups by" the characters filtering duplicaded ones
  vocab_size=len(words) #getting vocabulary size, this will be the input 
  tokenized_array.append(one_hot(data_array[i], round(vocab_size*1.3))) #one hot encoding input data

len(tokenized_array)


#adding padding
maxlen = max(tokenized_array[0])
num=0
for i in range(0, len(tokenized_array)):
    if len(tokenized_array[i]) > maxlen:
      maxlen = len(tokenized_array[i])

X_train = pad_sequences(tokenized_array, maxlen = maxlen)

num_words=maxlen

from keras.layers import Embedding, LSTM

model = Sequential()

model.add(Embedding(num_words, 50)) 
model.add(LSTM(32, dropout=0.4, recurrent_dropout=0.2, return_sequences=True)) 
model.add(LSTM(32, dropout=0.5, recurrent_dropout=0.2))  
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

#start_at = time()
model.fit(X_train, y_train, batch_size=512, validation_split=0.2, epochs=50)
#print("Addestramento completato in %.f secondi (5 epoche)" % ((time()-start_at)))

model.save("/content/drive/My Drive/Colab Notebooks/models/rss_model.h5")