import json

def pakistan_number_format(raw):
    try:
        data = json.loads(raw)
    except:
        return "❌ INVALID API RESPONSE"

    # 🔥 HANDLE ALL POSSIBLE STRUCTURES
    records = (
        data.get("records")
        or data.get("data", {}).get("records")
        or []
    )

    searched = data.get("searched") or data.get("number") or "Not Available"

    if not records:
        return "❌ NO DATA FOUND"

    msg = []
    msg.append("══════════════ 🇵🇰  P A K I S T A N  🇵🇰 ══════════════\n")

    msg.append("┃ 🔹 PHONE LOOKUP")
    msg.append(f"┃ 📞 Searched Phone : {searched}")
    msg.append("┃")

    for i, r in enumerate(records, 1):
        msg.append("┃────────────────────────────────")
        msg.append(f"┃ 🔹 RECORD {i}")
        msg.append(f"┃ 👤 Name        : {r.get('name','Not Available').strip()}")
        msg.append(f"┃ 📞 Mobile      : {r.get('mobile','Not Available').strip()}")

        cnic = r.get("cnic","").strip() or "Not Available"
        msg.append(f"┃ 🆔 CNIC        : {cnic}")

        # Address cleaning (!! / !)
        address = r.get("address","Not Available")
        address = address.replace("!!", "\n").replace("!", "\n")
        address = address.strip().replace("\n", "\n┃                 ")
        msg.append(f"┃ 📍 Address     : {address}")

        msg.append("┃ 🌍 Country     : Pakistan")

    msg.append("\n══════════════════════════════════")
    msg.append("          BUY API - @SUBHXCOSMO")
    msg.append("══════════════════════════════════")
    msg.append("══════════════════════════════════")
    msg.append("          MADE BY - @LingTech_Dev")
