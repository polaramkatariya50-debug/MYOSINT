from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import get_user, add_user
from config import MUST_JOIN_CHANNELS

@Client.on_message(filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id
    ref = None

    # Referral handling
    if len(message.command) > 1 and message.command[1].startswith("ref_"):
        try:
            ref = int(message.command[1].split("_")[1])
        except:
            ref = None

    # Create user if not exists
    if not get_user(user_id):
        add_user(user_id, ref)

    # Build JOIN buttons
    join_buttons = [
        [InlineKeyboardButton("🔗 JOIN CHANNEL", url=link)]
        for link in MUST_JOIN_CHANNELS.values()
    ]

    # Add verify button
    join_buttons.append(
        [InlineKeyboardButton("✅ VERIFY", callback_data="verify")]
    )

    keyboard = InlineKeyboardMarkup(join_buttons)

    text = (
        "👋 **WELCOME TO OSINT BOT**\n\n"
        "🔹 Join all required channels\n"
        "🔹 Click **VERIFY** to get **10 FREE CREDITS**\n\n"
        "📌 **AVAILABLE SEARCH COMMANDS**:\n\n"
        "📱 `/indian <number>` – Indian Number Info\n"
        "🇵🇰 `/pak <number>` – Pakistan Number Info\n"
        "🚗 `/vehicle <rc>` – Vehicle RC Details\n"
        "🚘 `/vehmobile <rc>` – Vehicle → Mobile\n"
        "🆔 `/aadhaar <number>` – Aadhaar Family Info\n"
        "🎮 `/ff <uid>` – Free Fire UID Info\n"
        "🏦 `/ifsc <code>` – Bank IFSC Info\n"
        "📞 `/trace <number>` – Call Trace Info\n"
        "💳 `/fampay <id>` – FamPay Info\n\n"
        "💰 Each search costs **2 credits**"
    )

    await message.reply(
        text,
        reply_markup=keyboard,
        disable_web_page_preview=True
    )
