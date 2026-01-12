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
    "indian": ("https://subhxcosmo-osint-api.onrender.com/api?key=VNIOX&type=mobile&term={}", indian_number_format),
    "pak": ("https://paknum.amorinthz.workers.dev/?key=AMORINTH&number={}", pakistan_number_format),
    "vehicle": ("https://vnioxcyber.vercel.app/api/vehicle?rc={}", vehicle_rc_format),
    "vehmobile": ("https://subhxcosmo-osint-api.onrender.com/api?key=VNIOX&type=vehicle_num&term={}", vehicle_to_mobile_format),
    "aadhaar": ("https://subhxcosmo-osint-api.onrender.com/api?key=VNIOX&type=id_family&term={}", aadhaar_family_format),
    "ff": ("https://api-cr-ffinfo.kesug.com/ff.php?uid={}", freefire_uid_format),
    "ifsc": ("https://ab-ifscinfoapi.vercel.app/info?ifsc={}", bank_ifsc_format),
    "trace": ("https://ab-calltraceapi.vercel.app/info?number={}", call_trace_format),
    "fampay": ("https://fampay-2-number.vercel.app/get-number?id={}", fampay_format),
}

@Client.on_message(filters.command(list(API_MAP.keys())))
async def search_handler(client, message):
    user = get_user(message.from_user.id)

    if not user or user["credits"] < SEARCH_COST:
        return await message.reply("❌ Not enough credits")

    if len(message.command) != 2:
        return await message.reply("Usage: /command <value>")

    deduct_credit(message.from_user.id, SEARCH_COST)

    cmd = message.command[0][1:]
    term = message.command[1]

    url, formatter = API_MAP[cmd]
    r = requests.get(url.format(term), timeout=30)

    if cmd in ["vehicle", "ff"]:
        await message.reply(formatter(r.json()), disable_web_page_preview=True)
    else:
        await message.reply(formatter(r.text), disable_web_page_preview=True)
