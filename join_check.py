from pyrogram.errors import (
    UserNotParticipant,
    ChatAdminRequired,
    PeerIdInvalid,
)

async def check_join(client, user_id):
    from config import MUST_JOIN_CHANNELS

    for channel_id in MUST_JOIN_CHANNELS.keys():
        try:
            await client.get_chat_member(channel_id, user_id)

        except UserNotParticipant:
            return False

        except (ChatAdminRequired, PeerIdInvalid):
            # Bot admin nahi / channel private
            # Skip safely (no crash)
            continue

        except Exception:
            continue

    return True
