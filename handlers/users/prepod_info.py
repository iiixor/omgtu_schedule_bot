from aiogram import types
from loader import dp, bot
from aiogram.types import CallbackQuery

from keyboards.inline.inline_switсh_language import *
from keyboards.inline.callback_datas import *
from filters.emoji import *
from parsing_data.parsing_main import *
from keyboards.default.menu import *
from keyboards.inline.subscribe_inline_button import *
from data.config import admins
from keyboards.default.menu import menu
# from core import *
from core.find_teacher import *

@dp.message_handler(text=f'Получить данные о преподавателе')
async def prep(message:types.Message):
    await message.answer('Введите фамилию преподавателя', reply_markup=menu)

@dp.message_handler()
async def prep(message:types.Message):
    surmane = message.text
    text = find_teacher(surmane)
    if '  ' in text:
        text = text.replace('  ','')
    print(text)
    await message.answer(text)



# @dp.message_handler()
# async def prep(message:types.Message):
#     await message.answer('Введите фамилию преподавателя')




@dp.callback_query_handler(prepod_callback.filter(fio = 'fioo'))
async def prepod(call:CallbackQuery):
    await call.message.answer(text ='Введите номер группы:')
