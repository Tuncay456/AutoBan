import asyncio
from time import time
from pyrogram import Client as Bot, filters, idle
from pyrogram.types import Message, User
from config import API_ID, API_HASH, BOT_TOKEN

bot = Bot(
    ':memory:',
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    sleep_threshold=1800
)

@bot.on_message(filters.command('start'))
async def start(bot, message):
    text = 'Hey, I am Autoban Bot \n\n I Can Ban a Member After Joining The group. \n\n 📖 Note - Added Member will not be banned. \n\n ⚠️Warning- My use is for personal Groups.\n\n ©️ @sillybots'
    await message.reply(text, quote=True)
    return

@bot.on_message(filters.new_chat_members)
async def kick(bot, m: Message):
    try:
	await m.chat.kick_member(m.from_user.id, until_date=time() + 31)
    except Exception as e:
        print(e)

	
bot.start()
idle()
