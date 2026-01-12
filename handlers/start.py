from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import MUST_JOIN_CHANNELS

buttons = [
    [InlineKeyboardButton("🔗 JOIN CHANNEL", url=link)]
    for link in MUST_JOIN_CHANNELS.values()
]

buttons.append([InlineKeyboardButton("✅ VERIFY", callback_data="verify")])

kb = InlineKeyboardMarkup(buttons)
