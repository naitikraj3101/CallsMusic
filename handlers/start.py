from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async  def  start_ ( client : Client , message : Message ):
    await message.reply_text(
        f"""<b> Alo Kawan, {message.from_user.first_name}!</b>
If you want to use just permission from the owner hehe 😂
Handsome owner: @Naitikraj3101



@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async  def  start ( client : Client , message : Message ):
    await message.reply_text(
If you want to use just permission from the owner hehe 😂
Handsome owner: @Naitikraj3101
        "Hi, want to find a song?" ,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Ya", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "Tidak ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
