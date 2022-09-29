from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot
from keyboards.default import menu
from database.classes import *
URL = 'https://lolz.guru/threads/1888814/'

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    
    user_id = message.from_user.id
    name = message.from_user.first_name
    user_name = message.from_user.username

    await message.delete()
    text = f'<b>Web_shop приветствует вас</b>, {message.from_user.full_name}!\n {URL}'
    await message.answer(text, reply_markup=menu)