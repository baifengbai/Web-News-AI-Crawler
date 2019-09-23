#!/usr/bin/python
#Thanks to: https://alvinalexander.com/python/python-script-read-rss-feeds-database
import feedparser
import time
from subprocess import check_output
import pymongo
import sys

limit = 12 * 3600 * 1000
#
# function to get the current time
#
current_time_millis = lambda: int(round(time.time() * 1000))
current_timestamp = current_time_millis()


def write_mongo(post): #see https://www.thepolyglotdeveloper.com/2019/01/getting-started-mongodb-docker-container-deployment/
    #use: docker run -d -p 27017-27019:27017-27019 --name mongodb mongo:4.0.4
    client = pymongo.MongoClient("mongodb://rio:onslario89@riohomecloud.ddns.net:27017")
    db = client.rss_news
    db[feed_name].insert_one(post)

for post in feed.entries: #check feed list file
    
    feed = feedparser.parse(url)
    feed_name=feed['feed']['title']
    #write
    for post in feed.entries:
        write_mongo(post)

