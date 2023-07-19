#!/usr/bin/env python3
from speedtest import Speedtest
from pyrogram.handlers import MessageHandler
from pyrogram.filters import command

from bot import bot, LOGGER
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.button_build import ButtonMaker
from bot.helper.telegram_helper.message_utils import sendMessage, deleteMessage, editMessage
from bot.helper.ext_utils.bot_utils import get_readable_file_size, new_task

@new_task
async def speedtest(_, message):
    speed = await sendMessage(message, "<i>Initializing Speedtest...</i>")
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    path = result['share']
    string_speed = f'''
☞ <b><i>SPEEDTEST INFO</i></b>
• <b>Upload:</b> <code>{get_readable_file_size(result['upload'] / 8)}/s</code>
• <b>Download:</b>  <code>{get_readable_file_size(result['download'] / 8)}/s</code>
• <b>Ping:</b> <code>{result['ping']} ms</code>
• <b>Time:</b> <code>{result['timestamp']}</code>
• <b>Data Sent:</b> <code>{get_readable_file_size(int(result['bytes_sent']))}</code>
• <b>Data Received:</b> <code>{get_readable_file_size(int(result['bytes_received']))}</code>

☞ <b><i>SPEEDTEST SERVER</i></b>
• <b>Name:</b> <code>{result['server']['name']}</code>
• <b>Country:</b> <code>{result['server']['country']}, {result['server']['cc']}</code>
• <b>Sponsor:</b> <code>{result['server']['sponsor']}</code>
• <b>Latency:</b> <code>{result['server']['latency']}</code>
• <b>Latitude:</b> <code>{result['server']['lat']}</code>
• <b>Longitude:</b> <code>{result['server']['lon']}</code>

☞ <b><i>CLIENT DETAILS</i></b>
• <b>IP Address:</b> <code>{result['client']['ip']}</code>
• <b>Latitude:</b> <code>{result['client']['lat']}</code>
• <b>Longitude:</b> <code>{result['client']['lon']}</code>
• <b>Country:</b> <code>{result['client']['country']}</code>
• <b>ISP:</b> <code>{result['client']['isp']}</code>
• <b>ISP Rating:</b> <code>{result['client']['isprating']}</code>
'''
    buttons = ButtonMaker()
    buttons.ubutton("🌟 Suport Me", "https://telegra.ph/Pikabot-Donate-06-13", 'header')
    try:
       sp = await message.reply_photo(photo=path, reply_to_message_id=message.id,
                                                 caption=string_speed, reply_markup=buttons.build_menu(1), disable_notification=True)
       await deleteMessage(speed)
    except Exception as e:
        LOGGER.error(str(e))
        sp = await editMessage(speed, string_speed)

bot.add_handler(MessageHandler(speedtest, filters=command(
    BotCommands.SpeedtsCommand) & CustomFilters.authorized))
