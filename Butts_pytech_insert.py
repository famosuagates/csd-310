import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.mbglzal.mongodb.net/pytech")
db = client["pytech"]
collection = db["students"]

post1 = {"_id": 1007, "First Name": "Ian", "Last Name": "Mckellen"}
post2 = {"_id": 1008, "First Name": "Benedict", "Last Name": "Cumberbatch"}
post3 = {"_id": 1009, "First Name": "Elijah", "Last Name": "Wood"}

collection.insert_many([post1, post2, post3])