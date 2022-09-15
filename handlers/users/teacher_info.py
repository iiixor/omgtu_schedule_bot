from aiogram import types
from loader import dp, bot


from core import *
from keyboards.inline.callback_datas import *
from parsing_data.parsing_main import *
from keyboards.default.menu import *
from keyboards.inline.inline_subscribe import *
from keyboards.default.menu import menu
from core.find_teacher import *

@dp.message_handler(text=f'Найти преподавателя')
async def prep(message:types.Message):
    await message.answer('Введите фамилию преподавателя:', reply_markup=menu)


@dp.message_handler()
async def prep(message:types.Message):
    surmane = message.text
    text = find_teacher(surmane)
    if '  ' in text:
        text = text.replace('  ','')
    await message.answer(text)