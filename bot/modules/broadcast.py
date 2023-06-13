from asyncio import sleep
from pymongo import MongoClient
from pyrogram import filters
from pyrogram.errors import FloodWait

from pyrogram.handlers import MessageHandler
from pyrogram.filters import command
from bot import bot, config_dict, LOGGER, user_data
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.message_utils import sendMessage, editMessage


async def broadcast(bot, message):
    mess = message.text
    replied = message.reply_to_message
    if len(mess) > 1 :
        mess = mess.split(maxsplit=1)[1]
        totals = len(user_data)
        for chat_id in user_data:
            try:
                await bot.send_message(chat_id=chat_id, text= mess)
            except Exception as e:
               LOGGER.error(e)
               continue
        msg = f"Broadcasting Completed ✅\n"
        msg += f"Total {totals} users in Database\n"
        await message.reply(msg, message)
    else:
        await message.reply("🥷 Please input a message that you want to broadcast ", message)

@bot.on_message(filters.command(["copys"]))
async def copy_bcp(_, message):
    replied = message.reply_to_message
    if len(message.command) == 1 :
       if not message.reply_to_message:
          return await message.reply("Please reply the chat that you want to copy", message)
          try:
              await message.reply_to_message.copy(
                message.from_user.id,
                caption_entities = message.reply_to_message.entities,
                reply_markup = message.reply_to_message.reply_markup,
            )
              return await message.reply_text("✅ Message sent", message)
          except Exception as e:
              return await message.reply(f"ERROR: {str(e)}")
    elif replied:
       try: 
          idtujuan = message.command[1]
          await message.reply_to_message.copy(
                idtujuan,
                caption_entities = message.reply_to_message.entities,
                reply_markup = message.reply_to_message.reply_markup,
            )
          return await message.reply_text("Message sent", message)
       except Exception as e:
          return await message.reply(f"ERROR: {e}", message)
    else:
        await message.reply("Please reply the chat that you want to copy", message)
  
  
bot.add_handler(MessageHandler(broadcast, filters= command(BotCommands.Broadcast) & CustomFilters.sudo))
bot.add_handler(MessageHandler(copy_bcp, filters= command(BotCommands.CopysCommand) & CustomFilters.sudo))