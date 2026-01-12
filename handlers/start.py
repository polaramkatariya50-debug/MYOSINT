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
        [InlineKeyboardButton("✅ VERIFY", callback_data="verify")]
    ])

    await message.reply(
        "👋 Welcome!\n\nJoin all channels & click VERIFY to get 10 credits.",
        reply_markup=kb
    )
