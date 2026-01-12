import os
from dotenv import load_dotenv

load_dotenv()

# ===============================
# TELEGRAM BOT
# ===============================
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

# ===============================
# DATABASE
# ===============================
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "vni0x")

# ===============================
# OWNER (tuple required)
# ===============================
OWNER_IDS = tuple(
    int(x) for x in os.getenv("OWNER_IDS", "").split(",") if x
)

# ===============================
# MUST JOIN CHANNELS
# KEY   = CHANNEL ID (for checking)
# VALUE = JOIN LINK (for button)
# ===============================
MUST_JOIN_CHANNELS = {
    -1002401784535: "https://t.me/OsintInformationGroup",
    -1001596819852: "https://t.me/+whz_G-xn0KdkZWI1",
    -1003389483500: "https://t.me/heroku_club",
    -1001511253627: "https://t.me/NOBITA_SUPPORT",
    -1002363071054: "https://t.me/+Ah7RcBKx4zQ2YTE1",
}

# ===============================
# CREDIT SYSTEM
# ===============================
SEARCH_COST = 2
NEW_USER_CREDIT = 10
REF_OWNER = 5
