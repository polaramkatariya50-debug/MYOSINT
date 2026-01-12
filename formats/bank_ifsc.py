import json

def bank_ifsc_format(raw):
    d = json.loads(raw)

    return f"""══════════════  B A N K   I F S C   C O D E   I N F O R M A T I O N  ══════════════

┃ 🔹 BANK DETAILS
┃ 🏦 Bank Name   : {d.get('BANK','N/A')}
┃ 🆔 Bank Code   : {d.get('BANKCODE','N/A')}
┃ 🌿 Branch      : {d.get('BRANCH','N/A')}
┃ 🏢 Address     : {d.get('ADDRESS','N/A')}
┃ 🌆 Centre      : {d.get('CENTRE','N/A')}
┃ 🌇 City        : {d.get('CITY','N/A')}
┃ 🗺 District    : {d.get('DISTRICT','N/A')}
┃ 🏛 State       : {d.get('STATE','N/A')}
┃ 🌍 ISO3166     : {d.get('ISO3166','N/A')}
┃ ☎️ Contact     : {d.get('CONTACT','N/A')}
┃
┃ 🔐 IFSC Code   : {d.get('IFSC','N/A')}
┃ 🧾 MICR Code   : {d.get('MICR','N/A')}
┃ 🌐 SWIFT Code  : {d.get('SWIFT','N/A')}
┃
┃ 💸 NEFT        : {d.get('NEFT','N/A')}
┃ ⚡️ RTGS        : {d.get('RTGS','N/A')}
┃ 📲 IMPS        : {d.get('IMPS','N/A')}
┃ 📱 UPI         : {d.get('UPI','N/A')}

══════════════════════════════════
          BUY API - @SUBHXCOSMO
══════════════════════════════════
══════════════════════════════════
          MADE BY - @LingTech_Dev
══════════════════════════════════"""
