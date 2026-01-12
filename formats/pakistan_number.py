import json

def pakistan_number_format(raw):
    # HTML safety
    if "<html" in raw.lower():
        return "❌ PAK API BLOCKED / DOWN\nTry again later."

    try:
        data = json.loads(raw)
    except:
        return "❌ INVALID RESPONSE FROM PAK API"

    records = data.get("records", [])
    searched = data.get("phone", "Not Available")

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
        msg.append(f"┃ 👤 Name        : {r.get('Name','Not Available').strip()}")
        msg.append(f"┃ 📞 Mobile      : {r.get('Mobile','Not Available').strip()}")

        cnic = r.get("CNIC","").strip() or "Not Available"
        msg.append(f"┃ 🆔 CNIC        : {cnic}")

        address = r.get("Address","Not Available")
        address = address.replace("  ", " ").strip()
        address = address.replace("\n", "\n┃                 ")
        msg.append(f"┃ 📍 Address     : {address}")

        msg.append(f"┃ 🌍 Country     : {r.get('Country','Pakistan')}")

    msg.append("\n══════════════════════════════════")
    msg.append("          BUY API - @SUBHXCOSMO")
    msg.append("══════════════════════════════════")
    msg.append("══════════════════════════════════")
    msg.append("          MADE BY - @LingTech_Dev")
    msg.append("══════════════════════════════════")

    return "\n".join(msg)
