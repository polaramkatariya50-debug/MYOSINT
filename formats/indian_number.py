import json

def indian_number_format(raw):
    try:
        data = json.loads(raw)
    except:
        return "❌ INVALID API RESPONSE"

    # ✅ CORRECT PATH BASED ON REAL API
    results = (
        data.get("result", {})
            .get("result", [])
    )

    if not results:
        return "❌ NO DATA FOUND"

    msg = []
    msg.append("══════════════  I N D I A N   N U M B E R   I N F O R M A T I O N  ══════════════\n")

    for i, r in enumerate(results, 1):
        msg.append(f"┃ 🔹 RESULT {i}")
        msg.append(f"┃ 👤 Name        : {r.get('name','Not Available').strip()}")
        msg.append(f"┃ 📞 Mobile      : {r.get('mobile','Not Available').strip()}")
        msg.append(f"┃ 👨‍👦 Father     : {r.get('father_name','Not Available').strip()}")

        # Address clean ( !! / ! ko line break )
        address = r.get("address","Not Available")
        address = address.replace("!!", "\n").replace("!", "\n")
        address = address.strip().replace("\n", "\n┃                 ")
        msg.append(f"┃ 📍 Address     : {address}")

        msg.append(f"┃ 📱 Alt Mobile  : {r.get('alt_mobile','Not Available').strip()}")
        msg.append(f"┃ 📡 Circle      : {r.get('circle','Not Available').strip()}")

        id_num = r.get("id_number","").strip() or "Not Available"
        email = r.get("email","").strip() or "Not Available"

        msg.append(f"┃ 🆔 ID Number   : {id_num}")
        msg.append(f"┃ 📧 Email       : {email}")
        msg.append(f"┃ 🆔 Record ID   : {r.get('id','Not Available')}")
        msg.append("┃")
        msg.append("┃────────────────────────────────")

    msg.append("\n══════════════════════════════════")
    msg.append("          BUY API - @SUBHXCOSMO")
    msg.append("══════════════════════════════════")
    msg.append("══════════════════════════════════")
    msg.append("          MADE BY - @LingTech_Dev")
    msg.append("══════════════════════════════════")

    return "\n".join(msg)
