def freefire_uid_format(d):
    return f"""╔══════════════════════════════════╗
║     🎮 FREE FIRE ID INFORMATION     ║
╚══════════════════════════════════╝

📌 Data fetched for UID : {d.get('uid','N/A')}

┌─ 👤 PROFILE DETAILS ─┐
 Nickname : {d.get('nickname','N/A')}
 User ID  : {d.get('uid','N/A')}
 Region   : {d.get('region','N/A')}
 Influencer : {d.get('influencer','No')}
└───────────────────────┘

┌─ 🎖️ ACCOUNT STATS ─┐
 Level          : {d.get('level','N/A')}
 Experience XP  : {d.get('xp','N/A')}
 Ranked Points  : {d.get('rank','N/A')}
 Prime Status   : {d.get('prime','N/A')}
 Likes          : {d.get('likes','N/A')}
└───────────────────────┘

══════════════════════════════════
          BUY API - @SUBHXCOSMO
══════════════════════════════════
══════════════════════════════════
          MADE BY - @LingTech_Dev
══════════════════════════════════"""
