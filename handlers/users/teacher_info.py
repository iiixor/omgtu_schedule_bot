from aiogram import types
from loader import dp, bot
from aiogram.types import CallbackQuery


from core import *
from keyboards.inline.callback_datas import *
from filters.emoji import *
from parsing_data.parsing_main import *
from keyboards.default.menu import *
from keyboards.inline.inline_subscribe import *
from data.config import admins
from keyboards.default.menu import menu

# из core импортируем файл find_teacher

from core.find_teacher import *

@dp.message_handler(text=f'Найти преподавателя')
async def prep(message:types.Message):
    await message.answer('Введите фамилию преподавателя:', reply_markup=menu)

#@dp.message_handler() хавает любой месседж без филтрации,
# поэтому с ним надо поаккуратнее

@dp.message_handler()
async def prep(message:types.Message):

    # в переменную surmane присваиваем то, что отправил пользователь

    surmane = message.text

    # вызывает метод find_teacher() из файла find_teacher.py
    # в качестве аругмента передаем фамилию преподавателя, которую
    # ввел пользователь

    # результат записывает в text

    text = find_teacher(surmane)

    # форматируем ответ

    if '  ' in text:
        text = text.replace('  ','')
    print(text)

    # вводим результат

    await message.answer(text)



# #@dp.message_handler()
# async def prep(message:types.Message):
#     await message.answer('Введите фамилию преподавателя')




#@dp.callback_query_handler(prepod_callback.filter(fio = 'fioo'))
#async def prepod(call:CallbackQuery):
#await call.message.answer(text ='Введите номер группы:')
