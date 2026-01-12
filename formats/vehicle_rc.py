def vehicle_rc_format(d):
    v = d.get("data",{})

    return f"""╔══════════════════════════════════╗
║     🚗 VEHICLE DETAILS: {v.get('rc','N/A')}     ║
╚══════════════════════════════════╝

📸 CAR PHOTO:
{v.get('image','Not Available')}

┌─ 👤 OWNER INFORMATION ─┐
 Owner Name     : {v.get('owner','N/A')}
 Also Known As  : {v.get('aka','N/A')}
 Father’s Name : {v.get('father','N/A')}
└───────────────────────┘

┌─ 🏠 ADDRESS DETAILS ─┐
 Address : {v.get('address','N/A')}
 City    : {v.get('city','N/A')}
 State   : {v.get('state','N/A')}
 Pincode : {v.get('pincode','N/A')}
└───────────────────────┘

┌─ 🔧 VEHICLE SPECIFICATIONS ─┐
 Manufacturer  : {v.get('manufacturer','N/A')}
 Model         : {v.get('model','N/A')}
 Vehicle Class : {v.get('class','N/A')}
 Fuel Type     : {v.get('fuel','N/A')}
└───────────────────────┘

┌─ 📋 REGISTRATION DETAILS ─┐
 Registration No. : {v.get('rc','N/A')}
 Registration Dt.: {v.get('reg_date','N/A')}
 Registered RTO  : {v.get('rto','N/A')}
└───────────────────────┘

┌─ 🛡 INSURANCE STATUS ─┐
 Insurance Valid Till : {v.get('insurance','N/A')}
 Status               : {v.get('insurance_status','N/A')}
└───────────────────────┘

══════════════════════════════════
          BUY API - @SUBHXCOSMO
══════════════════════════════════
══════════════════════════════════
          MADE BY - @LingTech_Dev
══════════════════════════════════"""
