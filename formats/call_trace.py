import json

def call_trace_format(raw):
    d = json.loads(raw)

    return f"""╔══════════════════════════════════╗
║   📞 INDIAN CALL TRACE INFORMATION   ║
╚══════════════════════════════════╝

┌─ 📱 BASIC DETAILS ─┐
 Mobile Number : {d.get('number','N/A')}
 Connection    : {d.get('connection','N/A')}
 SIM Operator  : {d.get('operator','N/A')}
 Country       : India
 Language      : {d.get('language','N/A')}
└───────────────────────┘

┌─ 👤 OWNER DETAILS ─┐
 Owner Name     : {d.get('owner','N/A')}
 Owner Address  : N/A
 Hometown       : N/A
└───────────────────────┘

══════════════════════════════════
          BUY API - @SUBHXCOSMO
══════════════════════════════════
══════════════════════════════════
          MADE BY - @LingTech_Dev
══════════════════════════════════"""
