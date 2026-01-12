from pyrogram import Client, filters
from database import get_user

@Client.on_message(filters.command("profile"))
async def profile(client, message):
    user = get_user(message.from_user.id)

    if not user:
        return await message.reply("❌ User not found")

    await message.reply(
        f"👤 **YOUR PROFILE**\n\n"
        f"🆔 ID: `{message.from_user.id}`\n"
        f"💰 Credits: **{user.get('credits', 0)}**\n"
        f"✅ Verified: **{user.get('verified', False)}**"
    )
