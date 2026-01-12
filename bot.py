from pyrogram import Client
from config import BOT_TOKEN, API_ID, API_HASH

app = Client(
    "osint-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)

print("🤖 Bot starting...")
app.run()
