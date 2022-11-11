from pyrogram.types import Client, Message
from Yukinon import app 
from Yukinon.utils.custom_filters import admin_filter, command
from Yukinon.utils.kbhelpers import rkb as ikb
from Yukinon.utils.string import build_keyboard, parse_button
from Yukinon.utils.lang import *
from button import *


@app.on_message(command(["رمزيات ولاد", "رمزيات شباب]))
async def shadow(client: Client, message: Message):
    await message.reply_photo(
        photo=IMG,
        caption=f"#تيست",
        reply_markup=InlineKeyboardMarkup(
            [
        [InlineKeyboardButton(text="سورس", url=f"https://t.me/FA9SH"),]
        ]
     ),
  )

IMG = ["https://telegra.ph/file/c8f5c1dd990ca9a3d8516.jpg",
       "https://telegra.ph/file/77cc3154b752ce822fd52.jpg",
       "https://telegra.ph/file/e72fb0b6a7fba177cf4c7.jpg",
       "https://telegra.ph/file/8738a478904238e367939.jpg",
       "https://telegra.ph/file/68d7830ba72820f44bda0.jpg"
]
