import asyncio
from pyrogram.types import Message
from pyrogram import Client 
from Yukinon import app
from config import OWNER_ID
from Yukinon.utils.caching import ADMIN_CACHE, TEMP_ADMIN_CACHE_BLOCK, admin_cache_reload
from Yukinon.utils.custom_filters import restrict_filter
from Yukinon.utils.commands import *

BANNED_USERS = filters.user()

@app.on_message(
 command(["بوت","البوت"]) & filters.user(OWNER_ID)
)
async def bot(client: Client, message: Message):
   await message.reply_text(f"◍ نعم حبيبى المطور 🥺❤️\n√")

@app.on_message(
 command(["بوت","البوت"])
& ~filters.edited
& ~BANNED_USERS
)
async def bot(client: Client, message: Message):
   await message.reply_text(f"◍ اسمى شادو ياحب 🙄❤️\n√")

@app.on_message(command(["بوت","البوت"]) & ADMIN_CACHE)
async def bot(client: Client, message: Message):
   await message.reply_text(f"◍ نعم حبيبى الادمن 🥺❤️\n√")
