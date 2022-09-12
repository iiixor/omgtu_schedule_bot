from gettext import find
from aiogram import types
from loader import dp
from aiogram.types import CallbackQuery
from keyboards.inline.inline_subscribe import *
import datetime

from keyboards.inline.inline_days_of_week import *
from keyboards.inline.callback_datas import *
from handlers.users.even_odd_week import *
from database.classes import *
from core.find_group import *

#-------------------------------------------------------Время + даты по омску

today = datetime.datetime.now().replace(second=0, microsecond=0)
Omsk_hour = datetime.timedelta(hours=3)
date_time_tomorrow_for_OMSK = datetime.timedelta(days= 1, hours =3)

#--------------------------------------------------------
database = Database()
database.path = 'database/users.db'
path = database.path





@dp.message_handler(text=f'Расписание')
async def mmm(message:types.Message):
    group = database.find_value(path, message.from_user.id , 'user_group')
    text = [
        f'Сейчас идет: <i>{even_odd()}</i> ',
        f'Ваша группа: {group}'
    ]
    await message.answer("\n".join(text), reply_markup=Raspisanie)

@dp.callback_query_handler(raspisanie_callback.filter(pn = '1'))
async def ponedelnik(call:CallbackQuery):
    group = database.find_value(path, call.from_user.id , 'user_group')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full':
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.09.05'
    text = find_group(group, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)
    # await call.message.answer(text = "Понедельник верхней недели")

@dp.callback_query_handler(raspisanie_callback.filter(pn = '2'))
async def ponedelnik(call:CallbackQuery):
    group = database.find_value(path, call.from_user.id , 'user_group')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full':
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.09.06'
    text = find_group(group, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)

@dp.callback_query_handler(raspisanie_callback.filter(pn = '3'))
async def ponedelnik(call:CallbackQuery):
    group = database.find_value(path, call.from_user.id , 'user_group')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full':
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.09.07'
    text = find_group(group, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)

@dp.callback_query_handler(raspisanie_callback.filter(pn = '4'))
async def ponedelnik(call:CallbackQuery):
    group = database.find_value(path, call.from_user.id , 'user_group')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full':
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.09.08'
    text = find_group(group, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)

@dp.callback_query_handler(raspisanie_callback.filter(pn = '5'))
async def ponedelnik(call:CallbackQuery):
    group = database.find_value(path, call.from_user.id , 'user_group')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full':
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.09.09'
    text = find_group(group, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)

@dp.callback_query_handler(raspisanie_callback.filter(pn = '6'))
async def ponedelnik(call:CallbackQuery):
    group = database.find_value(path, call.from_user.id , 'user_group')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full':
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.09.10'
    text = find_group(group, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)

@dp.callback_query_handler(raspisanie_callback.filter(pn = '7'))
async def ponedelnik(call:CallbackQuery):
    group = database.find_value(path, call.from_user.id , 'user_group')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full':
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.09.11'
    text = find_group(group, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)

#Первая неделя---------------------------------------------------------

@dp.callback_query_handler(raspisanie_callback.filter(pn = '8'))
async def ponedelnik(call:CallbackQuery):
    group = database.find_value(path, call.from_user.id , 'user_group')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full':
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.09.12'
    text = find_group(group, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)

@dp.callback_query_handler(raspisanie_callback.filter(pn = '9'))
async def ponedelnik(call:CallbackQuery):
    group = database.find_value(path, call.from_user.id , 'user_group')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full':
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.09.13'
    text = find_group(group, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)

@dp.callback_query_handler(raspisanie_callback.filter(pn = '10'))
async def ponedelnik(call:CallbackQuery):
    group = database.find_value(path, call.from_user.id , 'user_group')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full':
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.09.14'
    text = find_group(group, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)

@dp.callback_query_handler(raspisanie_callback.filter(pn = '11'))
async def ponedelnik(call:CallbackQuery):
    group = database.find_value(path, call.from_user.id , 'user_group')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full':
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.09.15'
    text = find_group(group, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)

@dp.callback_query_handler(raspisanie_callback.filter(pn = '12'))
async def ponedelnik(call:CallbackQuery):
    group = database.find_value(path, call.from_user.id , 'user_group')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full':
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.09.16'
    text = find_group(group, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)

@dp.callback_query_handler(raspisanie_callback.filter(pn = '13'))
async def ponedelnik(call:CallbackQuery):
    group = database.find_value(path, call.from_user.id , 'user_group')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full':
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.09.17'
    text = find_group(group, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)


@dp.callback_query_handler(raspisanie_callback.filter(pn = '14'))
async def ponedelnik(call:CallbackQuery):
    group = database.find_value(path, call.from_user.id , 'user_group')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full':
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.09.18'
    text = find_group(group, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)


#-------------------------------------------------------Кнопки сегодня + завтра + даты

@dp.callback_query_handler(raspisanie_callback.filter(pn = '15'))
async def segodnya(call: CallbackQuery):
    Omsk_hours = today + Omsk_hour
    Omsk_hours = Omsk_hours.strftime("%Y.%m.%d")
    group = database.find_value(path, call.from_user.id , 'user_group')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full':
        sub_bool = True
    else:
        sub_bool = False
    date = Omsk_hours
    text = find_group(group, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)

@dp.callback_query_handler(raspisanie_callback.filter(pn = '16'))
async def segodnya(call: CallbackQuery):
    time_tomorrow_Omsk = today + date_time_tomorrow_for_OMSK
    time_tomorrow_Omsk = time_tomorrow_Omsk.strftime("%Y.%m.%d")
    group = database.find_value(path, call.from_user.id , 'user_group')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full':
        sub_bool = True
    else:
        sub_bool = False
    date = time_tomorrow_Omsk
    text = find_group(group, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)


@dp.callback_query_handler(raspisanie_callback.filter(pn = '17'))
async def segodnya(call: CallbackQuery):
    text = f'Введите дату в формате:\n\n<b>Год.День.Месяц</b>\n\n<i>Например: 1980.05.29</i>'
    await call.message.answer(text)


@dp.message_handler(text_contains = ".")
async def testtt(message:types.Message):
    text = f'Проверка дата'
    await message.answer(text)
    


