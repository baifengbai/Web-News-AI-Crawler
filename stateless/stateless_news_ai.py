#reader
#Thanks to: https://alvinalexander.com/python/python-script-read-rss-feeds-database
import feedparser
import time
from subprocess import check_output
import pymongo
import sys
import telepot
import requests
import json
import re

test_url='http://tracking.feedpress.it/link/17798/12832957'

TELEGRAM_BOT_TOKEN='826514544:AAH_yj9x0CD6auL-N49XGFRi7JqavhrJnaE'
TELEGRAM_CHAT_ID='-1001457839912'


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

import requests
def send_data_to_ai(content):
      r = requests.get('http://localhost:5000/predict?input={}'.format(content)) 
      print(r.json()['predictions'])
      return r.json()['predictions'][0]

# Open the rss file with read only permit and read line by line
f = open('feed_list.txt', "r")
lines = f.readlines()
for url in lines:
    try: 
        feed = feedparser.parse(url)
        feed_name=feed['feed']['title']
        print("##########Reading feed: ", feed_name)
        print('\n') 
        for post in feed.entries:
            print(post['title'])
            if re.match(r'^TechCrunch', post['title']): #TODO add more feeds to parse
                if send_data_to_ai(post['content'][0]['value']) > 0.5:
                    send_message(post['link']) 
                print('\n') 
            else:
                if send_data_to_ai(post['summary']) > 0.5:
                    send_message(post['link'])
                print('\n') 
    except Exception as e:
        print("Error while reading feed", feed_name)
        print("Ecxception: ", e)
