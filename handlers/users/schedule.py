from aiogram import types
from loader import dp,bot
from aiogram.types import CallbackQuery
from keyboards.inline.inline_subscribe import *


from keyboards.inline.inline_days_of_week import *
from keyboards.inline.callback_datas import *

@dp.message_handler(text=f'Расписание')
async def mmm(message:types.Message):
    text = [
        'Расписание на две недели'
    ]
    await message.answer("\n".join(text), reply_markup=Raspisanie)

@dp.callback_query_handler(raspisanie_callback.filter(pn = '1'))
async def ponedelnik(call:CallbackQuery):
    await call.message.answer(text = "Понедельник верхней недели")

@dp.callback_query_handler(raspisanie_callback.filter(pn = '2'))
async def ponedelnik(call:CallbackQuery):
    await call.message.answer(text = "Вторник верхней недели")

@dp.callback_query_handler(raspisanie_callback.filter(pn = '3'))
async def ponedelnik(call:CallbackQuery):
    await call.message.answer(text = "Среда верхней недели")

@dp.callback_query_handler(raspisanie_callback.filter(pn = '4'))
async def ponedelnik(call:CallbackQuery):
    await call.message.answer(text = "Четверг верхней недели")

@dp.callback_query_handler(raspisanie_callback.filter(pn = '5'))
async def ponedelnik(call:CallbackQuery):
    await call.message.answer(text = "Пятница верхней недели")

@dp.callback_query_handler(raspisanie_callback.filter(pn = '6'))
async def ponedelnik(call:CallbackQuery):
    await call.message.answer(text = "Суббота верхней недели")

@dp.callback_query_handler(raspisanie_callback.filter(pn = '7'))
async def ponedelnik(call:CallbackQuery):
    await call.message.answer(text = "Воскресенье верхней недели")

#Первая неделя---------------------------------------------------------

@dp.callback_query_handler(raspisanie_callback.filter(pn = '8'))
async def ponedelnik(call:CallbackQuery):
    await call.message.answer(text = "Понедельник нижней недели")

@dp.callback_query_handler(raspisanie_callback.filter(pn = '9'))
async def ponedelnik(call:CallbackQuery):
    await call.message.answer(text = "Вторник нижней недели")

@dp.callback_query_handler(raspisanie_callback.filter(pn = '10'))
async def ponedelnik(call:CallbackQuery):
    await call.message.answer(text = "Среда нижней недели?")

@dp.callback_query_handler(raspisanie_callback.filter(pn = '11'))
async def ponedelnik(call:CallbackQuery):
    await call.message.answer(text = "Четверг нижней недели")

@dp.callback_query_handler(raspisanie_callback.filter(pn = '12'))
async def ponedelnik(call:CallbackQuery):
    await call.message.answer(text = "Пятница нижней недели")

@dp.callback_query_handler(raspisanie_callback.filter(pn = '13'))
async def ponedelnik(call:CallbackQuery):
    await call.message.answer(text = "Суббота нижней недели")

@dp.callback_query_handler(raspisanie_callback.filter(pn = '14'))
async def ponedelnik(call:CallbackQuery):
    await call.message.answer(text = "Воскресенье нижней недели")


@dp.callback_query_handler(raspisanie_callback.filter(pn = '15'))
async def segodnya(call: CallbackQuery):
    await call.message.answer(text = 'Сегоднящнее расписание')

@dp.callback_query_handler(raspisanie_callback.filter(pn = '16'))
async def segodnya(call: CallbackQuery):
    await call.message.answer(text = 'Завтрашнее расписание')

@dp.callback_query_handler(raspisanie_callback.filter(pn = '17'))
async def segodnya(call: CallbackQuery):
    await call.message.answer(text = 'Выберите дату:')
