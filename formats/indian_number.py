import json

def indian_number_format(raw):
    try:
        data = json.loads(raw)
    except:
        return "❌ INVALID API RESPONSE"

    # 🔥 HANDLE ALL POSSIBLE STRUCTURES
    if isinstance(data, list):
        results = data
    elif isinstance(data, dict):
        results = (
            data.get("results")
            or data.get("records")
            or data.get("data")
            or []
        )
        # Agar single object ho
        if isinstance(results, dict):
            results = [results]
    else:
        results = []

    if not results:
        return (
            "❌ NO DATA FOUND\n\n"
            "⚠️ API returned empty response.\n"
            "Check number or API status."
        )

    msg = []
    msg.append("══════════════  I N D I A N   N U M B E R   I N F O R M A T I O N  ══════════════\n")

    for i, r in enumerate(results, 1):
        msg.append(f"┃ 🔹 RESULT {i}")
        msg.append(f"┃ 👤 Name        : {r.get('name','Not Available')}")
        msg.append(f"┃ 📞 Mobile      : {r.get('mobile','Not Available')}")
        msg.append(f"┃ 👨‍👦 Father     : {r.get('father','Not Available')}")

        address = r.get("address") or r.get("addr") or "Not Available"
        address = address.replace("\n", "\n┃                 ")
        msg.append(f"┃ 📍 Address     : {address}")

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
