from pyrogram import Client, filters
from database import get_user, add_user
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("start"))
async def start(client, message):
    uid = message.from_user.id
    ref = None

    if len(message.command) > 1 and message.command[1].startswith("ref_"):
        ref = int(message.command[1].split("_")[1])

    if not get_user(uid):
        add_user(uid, ref)

    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("✅ VERIFY", callback_data="verify")],
        [InlineKeyboardButton("📢 JOIN CHANNELS", url="https://t.me/heroku_club")]
    ])

    await message.reply(
        "👋 WELCOME\n\n🔐 Join all channels & verify to get **10 FREE CREDITS**.",
        reply_markup=kb
    )
