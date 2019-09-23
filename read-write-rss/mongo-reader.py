'''
this function read rss content from mongo DB and call for AI model REST API
'''

import pymongo
import pymongo
import pprint
import requests

def send_data_to_ai(documents):
     for content in documents:
          #TODO: extract content from each document 
          r = requests.post('http://riohomecloud.ddns.net:5000/predict?msg={}'.format(content)) #TODO: open port 5000 on server
          return r

def get_ducuments(url):
     try: 
        feed = feedparser.parse(url)
        feed_name=feed['feed']['title']
        mydocs = db[feed_name].find()
     except:
        print("Error while reading feed", feed_name)
     return mydocs

#Connect to mongoDB
client = pymongo.MongoClient("mongodb://rio:onslario89@riohomecloud.ddns.net:27017")
db = client.rss_news #database name

# Open the rss file with read only permit and read line by line
f = open('feed_list.txt', "r")
lines = f.readlines()

for url in lines:
    documents=get_ducuments(url)
    result=send_data_to_ai(documents)
    #TODO: parse results from AI


