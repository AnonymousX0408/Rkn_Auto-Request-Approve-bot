from configs import rkn1
from pyrogram import Client, filters, enums
from pyrogram.errors import UserNotParticipant
from RknDeveloper.untils.database import add_user
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


@Client.on_callback_query(filters.regex("rkn_developer"))
async def chk(bot, cb : CallbackQuery):
    try:
        await bot.get_chat_member(rkn1.UPDATECHANNEL_ID, cb.from_user.id)
        if cb.message.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("─シ｡Aʙᴏᴜᴛ｡シ─", callback_data = "about")
                    ],[
                InlineKeyboardButton("𖣘 Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ", url="https://t.me/ProCoderZBots"),
                InlineKeyboardButton("⚘ Oғғɪᴄɪᴀʟ Cʜᴀɴɴᴇʟ ⚘", url="https://t.me/Pro_CoderZ")
                ],[
                InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ ࿇", url=f"https://t.me/{rkn1.BOT_USERNAME}?startchannel=ProCoderZBots&admin=invite_users+manage_chat")],[
                InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ࿇", url=f"https://t.me/{rkn1.BOT_USERNAME}?startgroup=ProCoderZBots&admin=invite_users+manage_chat")
                
            ]])            
            add_user(cb.from_user.id)
            await cb.message.edit("**👋 Hᴇʟʟᴏ {}!\n\nI'ᴍ Aɴ Aᴜᴛᴏ Aᴘᴘʀᴏᴠᴇ [Aᴅᴍɪɴ Jᴏɪɴ Rᴇǫᴜᴇsᴛs]({}) Bᴏᴛ.\nI Cᴀɴ Aᴘᴘʀᴏᴠᴇ Usᴇʀs Iɴ Cʜᴀɴɴᴇʟs & Gʀᴏᴜᴘs.Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ Aɴᴅ Gʀᴏᴜᴘ ᴀɴᴅ Pʀᴏᴍᴏᴛᴇ Mᴇ Tᴏ Aᴅᴍɪɴ Wɪᴛʜ Aᴅᴅ Mᴇᴍʙᴇʀs Pᴇʀᴍɪssɪᴏɴ.\n\n__Pᴏᴡᴇʀᴅ Bʏ : @ProCoderZBots__**".format(cb.from_user.mention, "https://t.me/telegram/153"), reply_markup=keyboard, disable_web_page_preview=True)
            
        print(cb.from_user.first_name +" Is started Your Bot!")
    except UserNotParticipant:
        await cb.answer(f"Hey, {cb.from_user.first_name}\nI Lɪᴋᴇ Yᴏᴜʀ Sᴍᴀʀᴛɴᴇss, Bᴜᴛ Dᴏɴ'ᴛ Bᴇ Oᴠᴇʀsᴍᴀʀᴛ! 🤓 \nJᴏɪɴ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ Fɪʀsᴛ 🥇‌‌", show_alert=True)

#🔥 Please Don't Remove Credit 💳 # ❣️ 
@Client.on_callback_query(filters.regex('about'))
async def about(bot,update):
	await update.message.edit_text(
	    #⚠️ don't change source code & source link ⚠️ #
	    text = """<b>» Mʏ Nᴀᴍᴇ: <a href='http://t.me/AutoAcceptProBot'>Aᴜᴛᴏ Jᴏɪɴ Rᴇǫᴜᴇsᴛ Bᴏᴛ</a>
‣ Cʀᴇᴀᴛᴏʀ : <a href='tg://settings'>ᴛʜɪs Pᴇʀsᴏɴ</a>
‣ Dᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/Mr_RoleXG'>ᴍʀ.ʀᴏʟᴇx</a>
‣ Lɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org'>Pʏʀᴏɢʀᴀᴍ</a>
‣ Lᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org'>Pʏᴛʜᴏɴ 3</a>
‣ Dᴀᴛᴀ Bᴀsᴇ : <a href='https://www.mongodb.com/'>Mᴏɴɢᴏ Dʙ</a>
‣ Bᴜɪʟᴅ Sᴛᴀᴛᴜs : ᴠ3.8.3 [sᴛᴀʙʟᴇ]</b>""",
	    reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("→ Bᴀᴄᴋ", callback_data = "rkn_developer")
               ]]
            )
    )
