from pyrogram.errors import UserNotParticipant
from config import MUST_JOIN_CHANNELS

async def check_join(client, user_id):
    for channel in MUST_JOIN_CHANNELS:
        try:
            await client.get_chat_member(channel, user_id)
        except UserNotParticipant:
            return False
    return True
