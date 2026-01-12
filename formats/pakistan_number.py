import json

def pakistan_number_format(raw):
    try:
        data = json.loads(raw)
        records = data.get("records", [])
        phone = data.get("searched", "N/A")
    except:
        return "❌ NO DATA FOUND"

    msg = []
    msg.append("══════════════ 🇵🇰  P A K I S T A N  🇵🇰 ══════════════\n")
    msg.append("┃ 🔹 PHONE LOOKUP")
    msg.append(f"┃ 📞 Searched Phone : {phone}")
    msg.append("┃")

    for i, r in enumerate(records, 1):
        msg.append("┃────────────────────────────────")
        msg.append(f"┃ 🔹 RECORD {i}")
        msg.append(f"┃ 👤 Name        : {r.get('name','N/A')}")
        msg.append(f"┃ 📞 Mobile      : {r.get('mobile','N/A')}")
        msg.append(f"┃ 🆔 CNIC        : {r.get('cnic','N/A')}")
        addr = r.get("address","N/A").replace("\n","\n┃                 ")
        msg.append(f"┃ 📍 Address     : {addr}")
        msg.append("┃ 🌍 Country     : Pakistan")

    msg.append("\n══════════════════════════════════")
    msg.append("          BUY API - @SUBHXCOSMO")
    msg.append("══════════════════════════════════")
    msg.append("══════════════════════════════════")
    msg.append("          MADE BY - @LingTech_Dev")
    msg.append("══════════════════════════════════")

    return "\n".join(msg)
