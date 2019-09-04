#!/usr/bin/python
#Thanks to: https://alvinalexander.com/python/python-script-read-rss-feeds-database
import feedparser
import time
from subprocess import check_output
import json
import pymongo
import sys

feed_name = 'TechCrunch'
url = 'http://techcrunch.com/feed/'

#feed_name = sys.argv[1]
#url = sys.argv[2]

#db = '/var/www/radio/data/feeds.db'
limit = 12 * 3600 * 1000

#
# function to get the current time
#
current_time_millis = lambda: int(round(time.time() * 1000))
current_timestamp = current_time_millis()

def post_is_in_db(title):
    with open(db, 'r') as database:
        for line in database:
            if title in line:
                return True
    return False

# return true if the title is in the database with a timestamp > limit
def post_is_in_db_with_old_timestamp(title):
    with open(db, 'r') as database:
        for line in database:
            if title in line:
                ts_as_string = line.split('|', 1)[1]
                ts = long(ts_as_string)
                if current_timestamp - ts > limit:
                    return True
    return False

#
# get the feed data from the url
#
feed = feedparser.parse(url)

#
# figure out which posts to print
#
posts_to_print = []
posts_to_skip = []

for post in feed.entries:
    # if post is already in the database, skip it
    # TODO check the time
    title = post.title
    link = post.link
    content = post.content
    published = post.published
    #if post_is_in_db_with_old_timestamp(title):
        #posts_to_skip.append(title)
    #else:
        #posts_to_print.append(title)
    posts_to_print.append(title)
#
# add all the posts we're going to print to the database with the current timestamp
# (but only if they're not already in there)
#
#f = open(db, 'a')
#for title in posts_to_print:
##    if not post_is_in_db(title):
#        f.write(title + "|" + str(current_timestamp) + "\n")
#f.close
    
#
# output all of the new posts
#

def write_mongo(json):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]

    mycol = mydb["db_name"]

    x = mycol.insert_one(json)

def write_json(dict):
    json_string = json.dumps(dict)
    #print(json_string)
    #print("\n")
    return json_string
   
count = 1
blockcount = 1
print("Looking for feed..")
for title in posts_to_print:
    if count % 5 == 1:
        print("Reading feed..")
        print("\n" + time.strftime("%a, %b %d %I:%M %p") + '  ((( ' + feed_name + ' - ' + str(blockcount) + ' )))')
        print("-----------------------------------------\n")
        blockcount += 1
    print(published + " | " + title + " | " + link)
    print(str(content) + "\n")
    dict = {}
    dict['Feed_Name'] = feed_name
    dict['Title'] = title
    dict['Link'] = link
    dict['Published'] = published
    dict['Content'] = content
    dict['Favorite'] = False
    write_mongo(write_json(dict))

    count += 1