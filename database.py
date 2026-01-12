from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

users = db.users


def get_user(uid):
    return users.find_one({"_id": uid})


def add_user(uid, ref=None):
    users.insert_one({
        "_id": uid,
        "credits": 0,
        "verified": False,
        "ref_by": ref
    })


def add_credit(uid, amount):
    users.update_one({"_id": uid}, {"$inc": {"credits": amount}})


def deduct_credit(uid, amount):
    users.update_one({"_id": uid}, {"$inc": {"credits": -amount}})


def set_verified(uid):
    users.update_one(
        {"_id": uid},
        {"$set": {"verified": True}},
        upsert=True
    )
