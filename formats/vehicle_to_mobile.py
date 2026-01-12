import json

def vehicle_to_mobile_format(raw):
    d = json.loads(raw)
    return f"""╔══════════════════════════════════╗
║   🚗 VEHICLE NUM TO OWNER NUM   ║
╚══════════════════════════════════╝

┌─ 🔍 MAPPING DETAILS ─┐
 Vehicle Number : {d.get('vehicle','N/A')}
 Mobile Number  : {d.get('mobile','N/A')}
└───────────────────────┘

┌─ ℹ️ STATUS INFO ─┐
 Mapping Type : Vehicle → Owner Mobile
 Record Status: SUCCESS
└───────────────────────┘

══════════════════════════════════
          BUY API - @SUBHXCOSMO
══════════════════════════════════
══════════════════════════════════
          MADE BY - @LingTech_Dev
══════════════════════════════════"""
