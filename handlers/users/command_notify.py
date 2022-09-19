from email import message
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import logging
from loader import dp, bot
# достаем menu из дир-и delpy_bot -> keyboards -> default
from keyboards.default import menu
from filters.emoji import *
from database.classes import *
from data.config import admins
from database.classes import *

@dp.message_handler(text = 'notify_all')
async def notify_all(message: types.Message):
    if message.from_user.id in admins:
        await message.answer('Отправьте текст уведомления')
    else:
        await message.answer('Ты кто?')

@dp.message_handler(text_contains = '!n!')
async def on_startup_notify(message: types.Message):
    database = Database()
    database.path = 'database/users.db'
    path = database.path
    # print(database.find_all(path, 'user_id')
    message.text = message.text.replace('!n!','')
    for user in database.find_all(path, 'users', 'user_id'):
        try:
            await dp.bot.send_message(int(user[0]), message.text)
        except Exception as err:
            logging.exception(err)

