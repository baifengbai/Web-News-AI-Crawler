'''
this function read rss content from mongo DB and call for AI model REST API
'''
import feedparser
import pymongo
import pprint
import requests
import re
from datetime import date
import datetime
import telepot
import os
import json

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
TELEGRAM_CHAT_ID = os.environ['TELEGRAM_CHAT_ID']

def send_message(text):
    params = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': text
    }
    url = "https://api.telegram.org/bot{}/sendMessage".format(TELEGRAM_TOKEN)
    r = requests.get(url, params=params)
    if r.status_code == 200:
        print(json.dumps(r.json(), indent=2))
    else:
        r.raise_for_status()

def send_data_to_ai(content):
        r = requests.post('http://0.0.0.0:5000/predict?input={}'.format(content))
        return r.json()['predictions'][0]

def get_ducuments(url):
     try:
        feed = feedparser.parse(url)
        feed_name=feed['feed']['title']
        mydocs = db[feed_name].find().limit(10) #{"date": {"$gt": datetime.datetime.today()}}
     except:
        print("Error while reading feed", feed_name)
     return mydocs

#Connect to mongoDB
client = pymongo.MongoClient("mongodb://rio:onslario89@localhost:27017")
db = client.rss_news #database name

start = date.today()
end = date.today()

# Open the rss file with read only permit and read line by line
f = open('feed_list.txt', "r")
lines = f.readlines()
contents=[]
#Parsing feed rss
for url in lines:
    try:
        feed = feedparser.parse(url)
        feed_name=feed['feed']['title']
        print("found feed: ", feed_name)
        mydocs = db[feed_name].find().limit(10) #{"date": {"$gt": datetime.datetime.today()}}
        print("found: ",  mydocs.count(with_limit_and_skip=True), " feed")
        if re.match(r'^TechCrunch', feed_name):
            for i in range(0, mydocs.count(with_limit_and_skip=True)):
                contents.append([mydocs[i]['content'][0]['value'], mydocs[i]['link']])
        else:
            for i in range(0, mydocs.count(with_limit_and_skip=True)):
                contents.append([mydocs[i]['summary'], mydocs[i]['link']])
    except Exception as e:
        print(e)
        pass
for content in contents:
    try:
        if send_data_to_ai(content[0]) > 0.5:
            send_message(content[1])
            print('sent to telegram..')
    except Exception as e:
        print(e)
        pass