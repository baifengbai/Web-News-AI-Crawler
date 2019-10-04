'''
this function read rss content from mongo DB and call for AI model REST API
'''
import feedparser
import pymongo
import pprint
import requests
import re
from datetime import date
import telepot
import os
import json

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN'] #'826514544:AAH_yj9x0CD6auL-N49XGFRi7JqavhrJnaE'
TELEGRAM_CHAT_ID = os.environ['TELEGRAM_CHAT_ID'] #'-1001457839912'

def send_message(test_url):
    params = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': test_url
    }
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    r = requests.get(url, params=params)
    if r.status_code == 200:
        print(json.dumps(r.json(), indent=2))
    else:
        r.raise_for_status()
        
def send_data_to_ai(documents):
     for content in documents:
          r = requests.post('http://riohomecloud.ddns.net:5000/predict?input={}'.format(content)) 
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

start = date.today()
end = date.today()

# Open the rss file with read only permit and read line by line
f = open('feed_list.txt', "r")
lines = f.readlines()
contents=[]
#Parsing feed rss
for url in lines:
    feed = feedparser.parse(url) 
    feed_name=feed['feed']['title']
    mydocs = db[feed_name].find({'date': {'$lt': end, '$gt': start}})
    if re.match(r'^TechCrunch', feed_name): 
        for i in range(0, mydocs.count()):
            contents.append(mydocs[i]['content'][0]['value'], mydocs[i]['link'])
    else:
        for i in range(0, mydocs.count()):
            contents.append(mydocs[i]['content'], mydocs[i]['link']) 

for content in contents:
    if send_data_to_ai(content[0]):
        send_message(content[1]) 

