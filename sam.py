#For Learning
#Feel free to use
#Share with those who are interested in learning

import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#=======================================================================

START_MSG = '<b>Hai {},\nIam A Simple Bot</b>>'

START_IMG = ["https://telegra.ph/file/00b0aa858250ec4229e54.jpg",
             "https://telegra.ph/file/eb6f76fbd5c3228d7babe.jpg",
             "https://telegra.ph/file/5b7a670096a54e3183b51.jpg"]

#=======================================================================


Bot = Client(session_name="Moon_Knight_Bot",
             api_id=12859368, #Put Your API ID Here 
             api_hash="f5b9904a8cb9eaf66bcb3a178503fb92", # Put Your API Hash Here                 
             bot_token="5097218470:AAEVPEWIezxF81pi8WSjE1zR9cHvY-ezb18") # Put Your Bot Token Here

#==COMMANDS=====================================================================

@Bot.on_message(filters.command(['start']))
async def start(bot, message):
         buttons = [
                     [InlineKeyboardButton('Help', callback_data="help"),
                      InlineKeyboardButton('Source Code', url='https://github.com')],
                     [InlineKeyboardButton('Channel', url='https://t.me/Baby_xd')]
                   ]
         await message.reply_photo(photo=random.choice(START_IMG), caption=START_MSG.format(message.from_user.mention), reply_markup=InlineKeyboardMarkup(buttons))
               
         
#==CALLBACK=====================================================================

@Bot.on_callback_query(filters.regex("help"))
async def about(bot, update):
    await update.message.edit("No help😏")
      
    
    
#=======================================================================

Bot.run()

#=======================================================================
