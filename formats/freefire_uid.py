def freefire_uid_format(d):
    return f"""
╔══════════════════════════════════╗
║     🎮 FREE FIRE ID INFORMATION     ║
╚══════════════════════════════════╝

📌 Data fetched for UID : {d['uid']}

┌─ 👤 PROFILE DETAILS ─┐
 Nickname : {d['nickname']}
 User ID  : {d['uid']}
 Region   : {d['region']}
 Influencer : {d['influencer']}
└───────────────────────┘

┌─ 🎖️ ACCOUNT STATS ─┐
 Level          : {d['level']}
 Experience XP  : {d['xp']}
 Ranked Points  : {d['rank']}
 Prime Status   : {d['prime']}
 Likes          : {d['likes']}
└───────────────────────┘

┌─ 👕 SKINS & PROFILE ─┐
 Skins Equipped : {d['skins']}
 Signature / Bio:
 {d['bio']}
└───────────────────────┘

┌─ ⏱️ ACCOUNT ACTIVITY ─┐
 Last Login     : {d['last_login']}
 Account Created : {d['created']}
 Profile Updated : {d['updated']}
└───────────────────────┘

┌─ 📆 FETCH TIME ─┐
 Date : {d['date']}
 Time : {d['time']}
└───────────────────────┘

══════════════════════════════════
          BUY API - @SUBHXCOSMO
══════════════════════════════════
══════════════════════════════════
          MADE BY - @LingTech_Dev
══════════════════════════════════
"""
