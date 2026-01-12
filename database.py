from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

users = db.users
logs = db.logs

def get_user(uid):
    return users.find_one({"_id": uid})

def add_user(uid, ref=None):
    users.insert_one({
        "_id": uid,
        "credits": 0,
        "verified": False,
        "ref_by": ref,
        "refs": 0
    })

def add_credit(uid, amt):
    users.update_one({"_id": uid}, {"$inc": {"credits": amt}})

def deduct_credit(uid, amt):
    users.update_one({"_id": uid}, {"$inc": {"credits": -amt}})

def set_verified(uid):
    users.update_one({"_id": uid}, {"$set": {"verified": True}})
