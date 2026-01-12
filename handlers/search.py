import requests
from pyrogram import Client, filters
from database import get_user, deduct_credit
from config import SEARCH_COST

from formats.indian_number import indian_number_format
from formats.pakistan_number import pakistan_number_format
from formats.vehicle_rc import vehicle_rc_format
from formats.vehicle_to_mobile import vehicle_to_mobile_format
from formats.aadhaar_family import aadhaar_family_format
from formats.freefire_uid import freefire_uid_format
from formats.bank_ifsc import bank_ifsc_format
from formats.call_trace import call_trace_format
from formats.fampay import fampay_format


API_MAP = {
    "indian": (
        "https://subhxcosmo-osint-api.onrender.com/api?key=VNIOX&type=mobile&term={}",
        lambda text: indian_number_format(text)
    ),
    "pak": (
        "https://paknum.amorinthz.workers.dev/?key=AMORINTH&number={}",
        lambda text: pakistan_number_format(text)
    ),
    "vehicle": (
        "https://vnioxcyber.vercel.app/api/vehicle?rc={}",
        lambda data: vehicle_rc_format(data)
    ),
    "vehmobile": (
        "https://subhxcosmo-osint-api.onrender.com/api?key=VNIOX&type=vehicle_num&term={}",
        lambda text: vehicle_to_mobile_format(text)
    ),
    "aadhaar": (
        "https://subhxcosmo-osint-api.onrender.com/api?key=VNIOX&type=id_family&term={}",
        lambda text: aadhaar_family_format(text)
    ),
    "ff": (
        "https://api-cr-ffinfo.kesug.com/ff.php?uid={}",
        lambda data: freefire_uid_format(data)
    ),
    "ifsc": (
        "https://ab-ifscinfoapi.vercel.app/info?ifsc={}",
        lambda text: bank_ifsc_format(text)
    ),
    "trace": (
        "https://ab-calltraceapi.vercel.app/info?number={}",
        lambda text: call_trace_format(text)
    ),
    "fampay": (
        "https://fampay-2-number.vercel.app/get-number?id={}",
        lambda text: fampay_format(text)
    ),
}


@Client.on_message(filters.command(list(API_MAP.keys())))
async def search_handler(client, message):
    user = get_user(message.from_user.id)

    if not user or user["credits"] < SEARCH_COST:
        return await message.reply("❌ NOT ENOUGH CREDITS\n💳 BUY CREDIT")

    if len(message.command) != 2:
        return await message.reply("❌ Usage: /command <value>")

    deduct_credit(message.from_user.id, SEARCH_COST)

    cmd = message.command[0][1:]
    term = message.command[1]
    url, formatter = API_MAP[cmd]

    try:
        res = requests.get(url.format(term), timeout=30)

        if cmd in ["vehicle", "ff"]:
            await message.reply(
                formatter(res.json()),
                disable_web_page_preview=True
            )
        else:
            await message.reply(
                formatter(res.text),
                disable_web_page_preview=True
            )

    except Exception as e:
        await message.reply("⚠️ API ERROR\nTry again later")
