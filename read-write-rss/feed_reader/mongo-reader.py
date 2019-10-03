'''
this function read rss content from mongo DB and call for AI model REST API
'''

import pymongo
import pymongo
import pprint
import requests
import re
from datetime import date
import telepot
import os

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
bot = telepot.Bot(TELEGRAM_TOKEN)

def send_telegram(msg): #see https://ludusrusso.cc/2017/04/27/implementiamo-un-bot-telegram-con-python/
    bot.sendMessage(msg)

def send_data_to_ai(documents):
     for content in documents:
          r = requests.post('http://riohomecloud.ddns.net:5000/predict?msg={}'.format(content)) 
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
    feed = feedparser.parse(url) #TODO add more feeds to parse
    feed_name=feed['feed']['title']
    mydocs = db[feed_name].find({'date': {'$lt': end, '$gt': start}})
    if re.match(r'^TechCrunch', feed_name):
        for i in range(0, mydocs.count()):
            contents.append(mydocs[i]['link'])
    if re.match(r'^DZone ', feed_name):
        for i in range(0, mydocs.count()):
            contents.append(mydocs[i]['link']) #TODO: test link saving
    if re.match(r'^Entrepreneur', feed_name):
        for i in range(0, mydocs.count()):
            contents.append(mydocs[i]['link'])
    if re.match(r'^Hacker Noon', feed_name):
        for i in range(0, mydocs.count()):
            contents.append(mydocs[i]['link'])
    if re.match(r'^Wired', feed_name):
        for i in range(0, mydocs.count()):
            contents.append(mydocs[i]['link'])

for content in contents:
    if send_data_to_ai(content['value']):
        send_telegram(content['link']) 

