import pymongo
from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.vwv5p.mongodb.net/module_5"
client=MongoClient(url)
db=client.module_5
print(db.list_collection_names)