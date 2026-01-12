import json

def aadhaar_family_format(raw):
    d = json.loads(raw)

    msg = []
    msg.append("══════════════  A A D H A A R   T O   F A M I L Y   I N F O R M A T I O N  ══════════════\n")
    msg.append("┃ 🔹 SEARCH DETAILS")
    msg.append("┃ 🔍 Search Type       : AADHAAR")
    msg.append("┃ ✅ Success           : True\n")

    rc = d.get("ration",{})
    msg.append("┃ 🔹 RATION CARD DETAILS")
    msg.append(f"┃ 🆔 Ration Card No.   : {rc.get('number','N/A')}")
    msg.append(f"┃ 🪪 Card Type         : {rc.get('type','N/A')}")
    msg.append(f"┃ 📜 Scheme            : {rc.get('scheme','N/A')}")
    msg.append(f"┃ 📅 Issue Date        : {rc.get('issue','N/A')}")
    msg.append(f"┃ 🏛 State             : {rc.get('state','N/A')}")
    msg.append(f"┃ 🗺 District          : {rc.get('district','N/A')}")
    msg.append(f"┃ 🏠 Address           : {rc.get('address','N/A')}\n")

    msg.append("┃────────────────────────────────")
    msg.append("┃ 🔹 FAMILY MEMBERS\n")

    for i,m in enumerate(d.get("members",[]),1):
        msg.append(f"┃ 👤 Member {i}")
        msg.append(f"┃ 🆔 Member ID         : {m.get('id','N/A')}")
        msg.append(f"┃ 👤 Name              : {m.get('name','N/A')}")
        msg.append(f"┃ ⚧️ Gender            : {m.get('gender','N/A')}")
        msg.append(f"┃ 🔐 Aadhaar (Masked)  : {m.get('aadhaar','N/A')}")
        msg.append(f"┃ 🔗 Relationship      : {m.get('relation','N/A')}")
        msg.append(f"┃ ✅ eKYC Status       : {m.get('ekyc','N/A')}\n")

    msg.append("══════════════════════════════════")
    msg.append("          BUY API - @SUBHXCOSMO")
    msg.append("══════════════════════════════════")
    msg.append("══════════════════════════════════")
    msg.append("          MADE BY - @LingTech_Dev")
    msg.append("══════════════════════════════════")

    return "\n".join(msg)
