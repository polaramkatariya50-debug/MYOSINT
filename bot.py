from pyrogram import Client
from config import BOT_TOKEN

app = Client(
    "osint-bot",
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)

app.run()
