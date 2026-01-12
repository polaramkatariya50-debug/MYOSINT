from pyrogram import Client, filters
from join_check import check_join
from database import get_user, add_credit, set_verified
from config import NEW_USER_CREDIT, REF_OWNER

@Client.on_callback_query(filters.regex("verify"))
async def verify(client, cq):
    user = get_user(cq.from_user.id)

    if user.get("verified", False):
        return await cq.answer("Already verified!", show_alert=True)

    if not await check_join(client, cq.from_user.id):
        return await cq.answer("Join all channels first!", show_alert=True)

    add_credit(cq.from_user.id, NEW_USER_CREDIT)

    if user.get("ref_by"):
        add_credit(user["ref_by"], REF_OWNER)

    set_verified(cq.from_user.id)

    await cq.message.edit("✅ VERIFIED\n💰 10 CREDITS ADDED")
