from pyrogram import Client, filters
from database import get_user

@Client.on_message(filters.command("profile"))
async def profile(client, message):
    u = get_user(message.from_user.id)
    await message.reply(
        f"👤 ID: {message.from_user.id}\n"
        f"💰 Credits: {u['credits']}\n"
        f"👥 Referrals: {u['refs']}"
    )
