from datetime import timedelta
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery
from loader import dp, bot
from keyboards.default import menu
from keyboards.default import y_n
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
    sub_format = database.find_value(path, "users", message.from_user.id,'sub_format')
    referrer_code = database.find_value(path, 'users', message.from_user.id, 'referrer_code')
    rand = random.randint(1000000000000000,9999999999999999)
    if user_id != 'Empty' and referrer_code == 'Empty':
        database.change_value(path,'users', message.from_user.id, 'referrer_code', rand)
    if sub_format == 'Free':
        await message.answer('У вас есть реферальный код?', reply_markup=y_n)
    else:
        text = f'<b>Омский Поликек</b> приветсвует тебя, {message.from_user.full_name} 👋'
        await message.answer(text, reply_markup=menu)
        await message.delete()


@dp.message_handler(text=f'Да')
async def bot_data_request(message: types.Message):
    await message.answer("Введите реферальный код")


@dp.message_handler(text=f'Нет')
async def bot_data_request(message: types.Message):
    text = f'<b>Омский Поликек</b> приветсвует тебя, {message.from_user.full_name} 👋'
    await message.answer(text, reply_markup=menu)

for i in range(10):
    @dp.message_handler(text_contains = str(i))
    async def bot_data_request(message: types.Message):
        text = database.check_ref_code(path, "users", message.text, 'referrer_code')
        reffer_code_id = database.check_ref_code(path, "users", message.text, 'user_id')
        if reffer_code_id == message.from_user.id:
            await message.answer('Вы не можете вводить свой реферальный код')
        elif text == 'Ваш код не верный\nПорпробуйте еще раз!':
            await message.answer(text)
        else:     
            database.change_value(path,"users",message.from_user.id, 'referral_types',message.text)
            await message.answer('Ваш реферальный код найден!', reply_markup=menu)
            await message.answer(f'<b>Омский Поликек</b> приветсвует тебя, {message.from_user.full_name} 👋')



# refferrer_code = database.find_value(path, 'users', 'referrer_code')
# sub_check = database.find_value(path, 'users', 'sub_format')
# today = datetime.date.today()

# if sub_check == 'Full':
#     add_time = timedelta(days = 14)
#     sub_time_now = database.find_value(path, 'users', 'sub_expiration')
#     sub_add = sub_time_now + add_time
#     database.change_value(path, 'users', 'sub_expiration', sub_add)

    