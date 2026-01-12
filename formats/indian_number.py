import json

def indian_number_format(raw):
    try:
        data = json.loads(raw)
        results = data.get("results", [])
    except:
        return "❌ NO DATA FOUND"

    msg = []
    msg.append("══════════════  I N D I A N   N U M B E R   I N F O R M A T I O N  ══════════════\n")

    for i, r in enumerate(results, 1):
        msg.append(f"┃ 🔹 RESULT {i}")
        msg.append(f"┃ 👤 Name        : {r.get('name','Not Available')}")
        msg.append(f"┃ 📞 Mobile      : {r.get('mobile','Not Available')}")
        msg.append(f"┃ 👨‍👦 Father     : {r.get('father','Not Available')}")
        addr = r.get("address","Not Available").replace("\n","\n┃                 ")
        msg.append(f"┃ 📍 Address     : {addr}")
        msg.append(f"┃ 📱 Alt Mobile  : {r.get('alt_mobile','Not Available')}")
        msg.append(f"┃ 📡 Circle      : {r.get('circle','Not Available')}")
        msg.append(f"┃ 🆔 ID Number   : {r.get('id_number','Not Available')}")
        msg.append(f"┃ 📧 Email       : {r.get('email','Not Available')}")
        msg.append(f"┃ 🆔 Record ID   : {r.get('record_id','Not Available')}")
        msg.append("┃")
        msg.append("┃────────────────────────────────")

    msg.append("\n══════════════════════════════════")
    msg.append("          BUY API - @SUBHXCOSMO")
    msg.append("══════════════════════════════════")
    msg.append("══════════════════════════════════")
    msg.append("          MADE BY - @LingTech_Dev")
    msg.append("══════════════════════════════════")

    return "\n".join(msg)
