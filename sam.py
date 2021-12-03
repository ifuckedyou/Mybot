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


Bot = Client(session_name="my-first-bot",
             api_id=1234567, #Put Your API ID Here 
             api_hash="t5h8a4ndg9ba59mgs58lo2h90ndr72bins", # Put Your API Hash Here                 
             bot_token="61952638:AbCdEfGhIjKlMnOp") # Put Your Bot Token Here

#==COMMANDS=====================================================================

@Bot.on_message(filters.command(['start']))
async def start(bot, message):
         buttons = [
                     [InlineKeyboardButton('Help', callback_data="help"),
                      InlineKeyboardButton('Source Code', url='https://github.com/Arun-TG/MyBot')],
                     [InlineKeyboardButton('Channel', url='https://t.me/CC_ChannelNew')]
                   ]
         await message.reply_photo(photo=random.choice(START_IMG), caption=START_MSG.format(message.from_user.mention), reply_markup=InlineKeyboardMarkup(buttons))
               
         
#==CALLBACK=====================================================================

@Bot.on_callback_query(filters.regex("help"))
async def about(bot, update):
    await update.message.edit("No help😏")
      
    
    
#=======================================================================

Bot.run()

#=======================================================================
