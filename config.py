import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "vni0x")
OWNER_IDS = {int(x) for x in os.getenv("OWNER_IDS", "").split(",") if x}

MUST_JOIN_CHANNELS = [
    "whz_G-xn0KdkZWI1",
    "heroku_club",
    "NOBITA_SUPPORT",
    "OsintInformationGroup",
    "Ah7RcBKx4zQ2YTE1",
]

SEARCH_COST = 2
NEW_USER_CREDIT = 10
REF_NEW_USER = 10
REF_OWNER = 5
