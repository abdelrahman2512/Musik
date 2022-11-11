import asyncio
from pyrogram.types import Message
from pyrogram import Client 
from Yukinon import app
from config import OWNER_ID
from Yukinon.utils.custom_filters import restrict_filter
from Yukinon.utils.commands import *

@app.on_message(
 command(["بوت","البوت"]) & filters.user(OWNER_ID)
)
async def bot(client: Client, message: Message):
   await message.reply_text(f"◍ نعم حبيبى المطور 🥺❤️\n√")
