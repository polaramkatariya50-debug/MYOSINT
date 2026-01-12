from pyrogram import Client, filters

@Client.on_message(filters.command("menu"))
async def menu(client, message):
    await message.reply(
        "📜 **COMMAND MENU**\n\n"
        "/indian <number>\n"
        "/pak <number>\n"
        "/vehicle <rc>\n"
        "/vehmobile <rc>\n"
        "/aadhaar <number>\n"
        "/ff <uid>\n"
        "/ifsc <code>\n"
        "/trace <number>\n"
        "/fampay <id>\n\n"
        "💳 Each search = 2 credits"
    )
