from pyrogram.types import BotCommand


# Commond Automatic Set 📐
#(©) @RknDeveloper Repo - https://github.com/RknDeveloper/Rkn_Auto-Request-Approve-bot 
# Please Don't Remove Credit 🙏
async def set_commands(app):
    RKN = [
        BotCommand("start", "Check Bot Alive."),
        BotCommand("users", "Total Users Check.(Aᴅᴍɪɴ Oɴʟʏ)"),
        BotCommand("broadcast", "Broadcast Massage Send All Users In Bot (Aᴅᴍɪɴ Oɴʟʏ)."),
        BotCommand("fd_broadcast", "Broadcast massage Forward Not Remove (Aᴅᴍɪɴ Oɴʟʏ)."),
        BotCommand("restart", "To Restart The Bot (Aᴅᴍɪɴ Oɴʟʏ).")
 
    ]
    await app.set_bot_commands(RKN)
  
