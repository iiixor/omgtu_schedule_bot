from asyncio.windows_events import NULL
from datetime import timedelta
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery
from loader import dp, bot
from keyboards.default import menu
from filters.emoji import *
from database.classes import *
import random

database = Database()
database.path = 'database/users.db'
path = database.path

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    


    
    user_id = message.from_user.id
    name = message.from_user.first_name
    user_name = message.from_user.username

    database.write_in_db(path,'users',[user_id, name, user_name])
    referrer_code = database.find_value(path, 'users', message.from_user.id, 'referrer_code')
    rand = random.randint(1000000000000000,9999999999999999)
    if user_id != 'Empty' and referrer_code == 'Empty':
        database.change_value(path,'users', message.from_user.id, 'referrer_code', rand)
    await message.delete()
    text = f'<b>Омский Поликек</b> приветсвует тебя, {message.from_user.full_name} 👋'
    await message.answer(text, reply_markup=menu)


# refferrer_code = database.find_value(path, 'users', 'referrer_code')
# sub_check = database.find_value(path, 'users', 'sub_format')
# today = datetime.date.today()

# if sub_check == 'Full':
#     add_time = timedelta(days = 14)
#     sub_time_now = database.find_value(path, 'users', 'sub_expiration')
#     sub_add = sub_time_now + add_time
#     database.change_value(path, 'users', 'sub_expiration', sub_add)

    