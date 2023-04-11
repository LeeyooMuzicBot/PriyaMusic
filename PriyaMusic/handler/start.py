from cache.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from PriyaMusic.config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from cache.filters import other_filters2
from time import time
from datetime import datetime
from cache.decorators import authorized_users_only

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 ** 2 * 24),
    ("hour", 60 ** 2),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)

start_keyboard = InlineKeyboardMarkup( [[
      InlineKeyboardButton("💫ɢɪᴛʜᴜʙ ʀᴇᴘᴏ", url=f"https://github.com/LeeyooMuzicBot/PriyaMusic"),
      InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅs💫", url=f"https://graph.org/file/9df7f53d1a3473e80b68f.jpg"
      ],[
      InlineKeyboardButton("🌺sᴜᴘᴘᴏʀᴛ", url=f"t.me/{GROUP_SUPPORT}"), 
      InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs🌺", url=f"t.me/{UPDATES_CHANNEL}"), 
      ],[
      InlineKeyboardButton("🥀 ᴀᴅᴅ ᴍᴇ ᴍᴏᴏᴅᴇʟ 🥀", url=f"t.me/{BOT_USERNAME}?startgroup=True")
      ]]
      ) 


@Client.on_message(filters.command("start") & filters.private)
async def start_(client: Client, message: Message):
    await message.reply_text(
        text=f"**ʜᴇʟʟᴏ {message.from_user.mention()}\n\n🥀 ʜɪ ɪᴀᴍ {BOT_NAME} ᴀᴅᴠᴀɴᴄᴇ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜsɪᴄ♪♪ ʙᴏᴛ\n😇ʀᴜɴ ᴏɴ ᴘʀɪᴠᴀᴛᴇ 💫 ᴠᴘs 🥀 sᴇʀᴠᴇʀ 🌎 \nғᴇᴇʟ 😊 ʜɪɢʜ ǫᴜᴀʟɪᴛʏ ᴍᴜsɪᴄ 🎧 ɪɴ ᴠᴄ 😎🤟 \n⭐ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ  [ᴘʀɪʏᴀ ᴍᴜsɪᴄ](https://t.me/priyaupdates)💞..**", 
        disable_web_page_preview=True,
        reply_markup=start_keyboard, 
    )
