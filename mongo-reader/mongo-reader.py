'''
this function read rss content from mongo DB and call for AI model REST API
'''

#see: https://www.mydatahack.com/how-to-get-data-from-mongodb-with-python/

import pymongo
from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://<user>:<pass>@<ip_or_fqdm>:27017/<db_name>')
db = client.test
#restaurants = db.restaurants
print('Total Record for the collection: ' + str(restaurants.count()))
for record in restaurants.find().limit(10):
     pprint.pprint(record)