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
      InlineKeyboardButton("🔎How to Use?Commands Menu.", url=f"https://graph.org/file/9df7f53d1a3473e80b68f.jpg")
      ],[
      InlineKeyboardButton("💡Git Repo", url=f"https://github.com/LeeyooMuzicBot/PriyaMusic"),
      InlineKeyboardButton("👤Bot Owner", url=f"https://t.me/tg://settings"),
      ],[
      InlineKeyboardButton("📨Channel", url=f"t.me/{GROUP_CHANNEL}"), 
      InlineKeyboardButton("Support📨", url=f"t.me/{UPDATES_SUPPORT}"), 
      ],[
      InlineKeyboardButton("➕Add me to your Group", url=f"t.me/{BOT_USERNAME}?startgroup=True")
      ]]
      ) 


@Client.on_message(filters.command("start") & filters.private)
async def start_(client: Client, message: Message):
    await message.reply_text(
        text=f"Hello, {message.from_user.mention()} My name is {BOT_NAME} \n\nI'm a telegram streaming bot with some useful features. Supporting platforms like Youtube, Spotify, Resso, AppleMusic , Soundcloud etc. \n\nFeel free to add me to your groups.", 
        disable_web_page_preview=True,
        reply_markup=start_keyboard, 
    )
