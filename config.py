import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Telegram API (Pyrogram requirement)
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

# Database
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "vni0x")

# Owner IDs (⚠️ tuple REQUIRED for pyrogram)
OWNER_IDS = tuple(
    int(x) for x in os.getenv("OWNER_IDS", "").split(",") if x
)

# Must Join Channels
MUST_JOIN_CHANNELS = [
    "whz_G-xn0KdkZWI1",
    "heroku_club",
    "NOBITA_SUPPORT",
    "OsintInformationGroup",
    "Ah7RcBKx4zQ2YTE1",
]

# Credit System
SEARCH_COST = 2
NEW_USER_CREDIT = 10
REF_NEW_USER = 10
REF_OWNER = 5
