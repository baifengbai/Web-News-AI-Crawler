'''
this function read rss content from mongo DB and call for AI model REST API
'''

import pymongo
import pymongo
import pprint
import requests
import re

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
contents=[]
#Parsing feed rss
for url in lines:
    feed = feedparser.parse(url)
    feed_name=feed['feed']['title']
    mydocs = db[feed_name].find()
    if re.match(r'^TechCrunch ', feed_name):
        for i in range(0, mydocs.count()):
            contents.append(mydocs[0]['content'][0]['value'])
    if re.match(r'^DZone ', feed_name):
        for i in range(0, mydocs.count()):
            contents.append(mydocs[0]['summary'])
    if re.match(r'^Entrepreneur ', feed_name):
        for i in range(0, mydocs.count()):
            contents.append(mydocs[0]['summary'])
    if re.match(r'^Hacker Noon', feed_name):
        for i in range(0, mydocs.count()):
            contents.append(mydocs[0]['summary'])
    if re.match(r'^Wired', feed_name):
        for i in range(0, mydocs.count()):
            contents.append(mydocs[0]['summary'])

#TODO send contents to API
#TODO add more feeds to parse