from pyrogram import Client, filters
from config import OWNER_IDS
from database import users

@Client.on_message(filters.command("stats") & filters.user(OWNER_IDS))
async def stats(client, message):
    await message.reply(f"📊 TOTAL USERS: {users.count_documents({})}")
