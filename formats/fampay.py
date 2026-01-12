import json

def fampay_format(raw):
    d = json.loads(raw)

    return f"""══════════════  F A M P A Y   I N F O R M A T I O N  ══════════════

┃ 🔹 CONTACT DETAILS
┃ 🆔 Fam ID      : {d.get('id','N/A')}
┃ 👤 Name        : {d.get('name','N/A')}
┃ 📞 Phone       : {d.get('phone','N/A')}
┃ 📡 Source      : {d.get('source','N/A')}
┃ ✅ Status      : {d.get('status','N/A')}
┃ 🗂 Type        : {d.get('type','N/A')}

══════════════════════════════════
          BUY API - @SUBHXCOSMO
══════════════════════════════════
══════════════════════════════════
          MADE BY - @LingTech_Dev
══════════════════════════════════"""
