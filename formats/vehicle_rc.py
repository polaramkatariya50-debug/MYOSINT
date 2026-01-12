def vehicle_rc_format(d):
    return f"""
╔══════════════════════════════════╗
║     🚗 VEHICLE DETAILS: {d['rc']}     ║
╚══════════════════════════════════╝

📸 CAR PHOTO:
{d['photo']}

┌─ 👤 OWNER INFORMATION ─┐
 Owner Name     : {d['owner']}
 Also Known As  : {d['aka']}
 Father’s Name : {d['father']}
└───────────────────────┘

┌─ 🏠 ADDRESS DETAILS ─┐
 Address : {d['address']}
 City    : {d['city']}
 State   : {d['state']}
 Pincode : {d['pincode']}
└───────────────────────┘

┌─ 🔧 VEHICLE SPECIFICATIONS ─┐
 Manufacturer  : {d['manufacturer']}
 Model         : {d['model']}
 Vehicle Class : {d['vehicle_class']}
 Fuel Type     : {d['fuel']}
└───────────────────────┘

┌─ 📋 REGISTRATION DETAILS ─┐
 Registration No. : {d['rc']}
 Registration Dt.: {d['reg_date']}
 Registered RTO  : {d['rto']}
└───────────────────────┘

┌─ 🛡 INSURANCE STATUS ─┐
 Insurance Valid Till : {d['insurance_valid']}
 Status               : {d['insurance_status']}
└───────────────────────┘

══════════════════════════════════
          BUY API - @SUBHXCOSMO
══════════════════════════════════
══════════════════════════════════
          MADE BY - @LingTech_Dev
══════════════════════════════════
"""
