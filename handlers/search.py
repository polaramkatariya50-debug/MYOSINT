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


# ===============================
# COMMAND → API MAP
# ===============================
API_MAP = {
    "num": (
        "https://subhxcosmo-osint-api.onrender.com/api?key=VNIOX&type=mobile&term={}",
        indian_number_format
    ),
    "paknum": (
        "https://paknum.amorinthz.workers.dev/?key=AMORINTH&number={}",
        pakistan_number_format
    ),
    "vehicle": (
        "https://vnioxcyber.vercel.app/api/vehicle?rc={}",
        vehicle_rc_format
    ),
    "vehmobile": (
        "https://subhxcosmo-osint-api.onrender.com/api?key=VNIOX&type=vehicle_num&term={}",
        vehicle_to_mobile_format
    ),
    "aadhar": (
        "https://subhxcosmo-osint-api.onrender.com/api?key=VNIOX&type=id_family&term={}",
        aadhaar_family_format
    ),
    "ff": (
        "https://api-cr-ffinfo.kesug.com/ff.php?uid={}",
        freefire_uid_format
    ),
    "ifsc": (
        "https://ab-ifscinfoapi.vercel.app/info?ifsc={}",
        bank_ifsc_format
    ),
    "numtrace": (
        "https://ab-calltraceapi.vercel.app/info?number={}",
        call_trace_format
    ),
    "fam": (
        "https://fampay-2-number.vercel.app/get-number?id={}",
        fampay_format
    ),
}


# ===============================
# SEARCH HANDLER (FINAL)
# ===============================
@Client.on_message(filters.command())
async def search_handler(client, message):
    user_id = message.from_user.id

    # -------------------------------
    # USER / CREDIT CHECK
    # -------------------------------
    user = get_user(user_id)
    if not user or user.get("credits", 0) < SEARCH_COST:
        return await message.reply(
            "❌ NOT ENOUGH CREDITS\n💳 BUY CREDIT"
        )

    # -------------------------------
    # COMMAND FORMAT CHECK
    # -------------------------------
    if not message.command or len(message.command) != 2:
        return await message.reply(
            "❌ Usage:\n"
            "/num <number>\n"
            "/paknum <number>\n"
            "/vehicle <rc>\n"
            "/vehmobile <rc>\n"
            "/aadhar <aadhaar>\n"
            "/ff <uid>\n"
            "/ifsc <code>\n"
            "/numtrace <number>\n"
            "/fam <id>"
        )

    # -------------------------------
    # COMMAND NORMALIZE
    # -------------------------------
    cmd = message.command[0][1:].lower()
    term = message.command[1]

    # -------------------------------
    # INVALID COMMAND SAFETY
    # -------------------------------
    if cmd not in API_MAP:
        return await message.reply(
            "❌ INVALID COMMAND\n\n"
            "✅ Available Commands:\n"
            "/num  /paknum\n"
            "/vehicle  /vehmobile\n"
            "/aadhar  /ff\n"
            "/ifsc  /numtrace\n"
            "/fam"
        )

    api_url, formatter = API_MAP[cmd]

    # -------------------------------
    # API REQUEST
    # -------------------------------
    try:
        if cmd == "paknum":
            response = requests.get(
                api_url.format(term),
                timeout=40,
                headers={
                    "User-Agent": "Mozilla/5.0",
                    "Accept": "application/json"
                },
                verify=False
            )
        else:
            response = requests.get(
                api_url.format(term),
                timeout=30,
                headers={
                    "User-Agent": "Mozilla/5.0",
                    "Accept": "application/json"
                }
            )

        if response.status_code != 200:
            return await message.reply(
                "❌ API TEMPORARILY DOWN\nTry again later."
            )

        output = formatter(response.text)

        if not output or "NO DATA" in output.upper():
            return await message.reply("❌ NO DATA FOUND")

        # -------------------------------
        # CREDIT DEDUCT (SUCCESS ONLY)
        # -------------------------------
        deduct_credit(user_id, SEARCH_COST)

        await message.reply(
            output,
            disable_web_page_preview=True
        )

    except Exception:
        await message.reply(
            "⚠️ API ERROR\nTry again later."
        )
