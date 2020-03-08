import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://pretty:printed@cluster0-oqlkk.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test"]
post = {"_id": 0, "name": "Adi", "score": 7}

collection.insert_one(post)

