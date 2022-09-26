from gettext import find
from aiogram import types
from loader import dp
from aiogram.types import CallbackQuery
from keyboards.inline.inline_subscribe import *
import datetime

from keyboards.inline.inline_days_of_week import *
from keyboards.inline.callback_datas import *
# from handlers.users.even_odd_week import *
from database.classes import *
from core.find_group_json import *

#-------------------------------------------------------Время + даты по омску

today = datetime.datetime.now().replace(second=0, microsecond=0)
print(today.isoweekday())
Omsk_hour = datetime.timedelta(hours=3)
date_time_tomorrow_for_OMSK = datetime.timedelta(days= 1, hours =3)

#--------------------------------------------------------
database = Database()
database.path = 'database/users.db'
path = database.path

weekdays = {
    "1_Верхняя неделя":"2022.09.12",
    "2_Верхняя неделя":"2022.09.13",
    "3_Верхняя неделя":"2022.09.14",
    "4_Верхняя неделя":"2022.09.15",
    "5_Верхняя неделя":"2022.09.16",
    "6_Верхняя неделя":"2022.09.17",
    "7_Верхняя неделя":"2022.09.18",
    "1_Нижняя неделя":"2022.09.19",
    "2_Нижняя неделя":"2022.09.20",
    "3_Нижняя неделя":"2022.09.21",
    "4_Нижняя неделя":"2022.09.22",
    "5_Нижняя неделя":"2022.09.23",
    "6_Нижняя неделя":"2022.09.24",
    "7_Нижняя неделя":"2022.09.25",
}

def even_odd():
    date = datetime.datetime.now().replace(second=0, microsecond=0)
    wk = date.isocalendar()[1]
    if (wk % 2 == 0):
        return "Нижняя неделя"
    else:
        return "Верхняя неделя"

def get_day(today):
    weekdays = {
    "1_Верхняя неделя":"2022.09.12",
    "2_Верхняя неделя":"2022.09.13",
    "3_Верхняя неделя":"2022.09.14",
    "4_Верхняя неделя":"2022.09.15",
    "5_Верхняя неделя":"2022.09.16",
    "6_Верхняя неделя":"2022.09.17",
    "7_Верхняя неделя":"2022.09.18",
    "1_Нижняя неделя":"2022.09.19",
    "2_Нижняя неделя":"2022.09.20",
    "3_Нижняя неделя":"2022.09.21",
    "4_Нижняя неделя":"2022.09.22",
    "5_Нижняя неделя":"2022.09.23",
    "6_Нижняя неделя":"2022.09.24",
    "7_Нижняя неделя":"2022.09.25",
    }
    weekday=today.isoweekday()
    week = even_odd()
    weekday_full = str(weekday)+"_"+week
    print(weekdays[weekday_full])
    return weekdays[weekday_full]





@dp.message_handler(text=f'Расписание')
async def mmm(message:types.Message):
    sub_format = database.find_value(path,'users', message.from_user.id , 'sub_format')
    group = database.find_value(path,'users', message.from_user.id , 'user_group')
    if sub_format == 'Full' or sub_format == "Free_pass":
        text = [
            f'Сейчас идет: <i>{even_odd()}</i> ',
            f'Ваша группа: {group}'
        ]
    else:
        text = [
            f'Сейчас идет: <i>{even_odd()}</i> ',
            f'Ваша группа: {group}',
            f'<i>В связи с бесплатной подпиской, часть полей недоступно</i>'
        ]
    await message.answer("\n".join(text), reply_markup=Raspisanie)

@dp.callback_query_handler(raspisanie_callback.filter(pn = '1'))
async def ponedelnik(call:CallbackQuery):
    group = database.find_value(path,'users', call.from_user.id , 'user_group')
    sub_format = database.find_value(path,'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.10.03'
    print(group)
    text = find_group_json(date, group, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)
    # await call.message.answer(text = "Понедельник верхней недели")

@dp.callback_query_handler(raspisanie_callback.filter(pn = '2'))
async def ponedelnik(call:CallbackQuery):
    group = database.find_value(path,'users', call.from_user.id , 'user_group')
    sub_format = database.find_value(path,'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.10.04'
    text = find_group_json(date, group, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)

@dp.callback_query_handler(raspisanie_callback.filter(pn = '3'))
async def ponedelnik(call:CallbackQuery):
    group = database.find_value(path,'users', call.from_user.id , 'user_group')
    sub_format = database.find_value(path,'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.10.05'
    text = find_group_json(date, group, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)

@dp.callback_query_handler(raspisanie_callback.filter(pn = '4'))
async def ponedelnik(call:CallbackQuery):
    group = database.find_value(path,'users', call.from_user.id , 'user_group')
    sub_format = database.find_value(path,'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.10.06'
    text = find_group_json(date, group, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)

@dp.callback_query_handler(raspisanie_callback.filter(pn = '5'))
async def ponedelnik(call:CallbackQuery):
    group = database.find_value(path,'users', call.from_user.id , 'user_group')
    sub_format = database.find_value(path,'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.10.07'
    text = find_group_json(date, group, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)

@dp.callback_query_handler(raspisanie_callback.filter(pn = '6'))
async def ponedelnik(call:CallbackQuery):
    group = database.find_value(path,'users', call.from_user.id , 'user_group')
    sub_format = database.find_value(path,'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.10.08'
    text = find_group_json(date, group, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)

@dp.callback_query_handler(raspisanie_callback.filter(pn = '7'))
async def ponedelnik(call:CallbackQuery):
    group = database.find_value(path,'users', call.from_user.id , 'user_group')
    sub_format = database.find_value(path,'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.10.09'
    text = find_group_json(date, group, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)

#Первая неделя---------------------------------------------------------

@dp.callback_query_handler(raspisanie_callback.filter(pn = '8'))
async def ponedelnik(call:CallbackQuery):
    group = database.find_value(path,'users', call.from_user.id , 'user_group')
    sub_format = database.find_value(path,'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.10.10'
    text = find_group_json(date, group, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)

@dp.callback_query_handler(raspisanie_callback.filter(pn = '9'))
async def ponedelnik(call:CallbackQuery):
    group = database.find_value(path,'users', call.from_user.id , 'user_group')
    sub_format = database.find_value(path,'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.10.11'
    text = find_group_json(date, group, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)

@dp.callback_query_handler(raspisanie_callback.filter(pn = '10'))
async def ponedelnik(call:CallbackQuery):
    group = database.find_value(path,'users', call.from_user.id , 'user_group')
    sub_format = database.find_value(path,'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.10.12'
    text = find_group_json(date, group, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)

@dp.callback_query_handler(raspisanie_callback.filter(pn = '11'))
async def ponedelnik(call:CallbackQuery):
    group = database.find_value(path,'users', call.from_user.id , 'user_group')
    sub_format = database.find_value(path,'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.10.13'
    text = find_group_json(date, group, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)

@dp.callback_query_handler(raspisanie_callback.filter(pn = '12'))
async def ponedelnik(call:CallbackQuery):
    group = database.find_value(path,'users', call.from_user.id , 'user_group')
    sub_format = database.find_value(path,'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.10.14'
    text = find_group_json(date, group, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)

@dp.callback_query_handler(raspisanie_callback.filter(pn = '13'))
async def ponedelnik(call:CallbackQuery):
    group = database.find_value(path,'users', call.from_user.id , 'user_group')
    sub_format = database.find_value(path,'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.10.15'
    text = find_group_json(date, group, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)


@dp.callback_query_handler(raspisanie_callback.filter(pn = '14'))
async def ponedelnik(call:CallbackQuery):
    group = database.find_value(path,'users', call.from_user.id , 'user_group')
    sub_format = database.find_value(path,'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.10.16'
    text = find_group_json(date, group, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)


#-------------------------------------------------------Кнопки сегодня + завтра  

@dp.callback_query_handler(raspisanie_callback.filter(pn = '15'))
async def segodnya(call: CallbackQuery):
    Omsk_hours = today + Omsk_hour
    # Omsk_hours = Omsk_hours.strftime("%Y.%m.%d")
    group = database.find_value(path,'users', call.from_user.id , 'user_group')
    sub_format = database.find_value(path,'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = Omsk_hours
    date = get_day(date)
    text = find_group_json(date, group, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)

@dp.callback_query_handler(raspisanie_callback.filter(pn = '16'))
async def segodnya(call: CallbackQuery):
    time_tomorrow_Omsk = today + date_time_tomorrow_for_OMSK
    # time_tomorrow_Omsk = time_tomorrow_Omsk.strftime("%Y.%m.%d")
    group = database.find_value(path,'users', call.from_user.id , 'user_group')
    sub_format = database.find_value(path,'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = time_tomorrow_Omsk
    date = get_day(date)
    text = find_group_json(date, group, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie)


