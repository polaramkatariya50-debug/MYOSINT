from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

MAIN_MENU = InlineKeyboardMarkup([
    [InlineKeyboardButton("🔍 SEARCH API", callback_data="search")],
    [InlineKeyboardButton("🎁 REFER & EARN", callback_data="refer"),
     InlineKeyboardButton("👤 MY PROFILE", callback_data="profile")],
    [InlineKeyboardButton("💰 MY CREDIT", callback_data="credit")],
    [InlineKeyboardButton("🛒 BUY API", url="https://t.me/SUBHXCOSMO"),
     InlineKeyboardButton("💳 BUY CREDIT", url="https://t.me/SUBHXCOSMO")]
])
