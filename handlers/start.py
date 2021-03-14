from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b> Alo Kawan, {message.from_user.first_name}!</b>
ᴇᴜᴘʜᴏʀɪᴀ  ᴍᴜsɪᴄ  ᴀᴅᴀʟᴀʜ  ʙᴏᴛ   ᴍᴜsɪᴄ  ᴄᴀʟʟ  ɢʀᴜᴘ👑!
ᴍᴏʜᴏɴ  ᴍᴀᴋʟᴜᴍ  ᴊɪᴋᴀ  ᴀᴅᴀ  ᴍᴀsᴀʟᴀʜ  ᴘᴀᴅᴀ  ᴋᴜᴀʟɪᴛᴀs  ᴍᴜsɪᴋ.

Jika ingin menggunakan cukup ijin ke owner hehe
Owner ganteng @betterthaaanhecan
Support Channel Owner Ya @ruangpublikk

Tutorial menggunakan bot cek dibawah.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Cara Pakai", url="https://telegra.ph/ᴏ-ʟ-ᴀ-ɴ-ᴀ-03-14"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "Hai, mau nyari lagu ya?",
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
