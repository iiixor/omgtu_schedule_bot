from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot
# достаем menu из дир-и delpy_bot -> keyboards -> default
from keyboards.default import menu
from filters.emoji import *
from database.classes import *

database = Database()
database.path = 'database/users.db'
path = database.path

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    
    user_id = message.from_user.id
    name = message.from_user.first_name
    user_name = message.from_user.username

    database.write_in_db(path,[user_id, name, user_name])    # database.write_in_db([message.from_user.id])
    
    await message.delete()
    text = f'<b>OmGTU_bot</b> приветсвует тебя, {message.from_user.full_name} 👋'
    await message.answer(text, reply_markup=menu)