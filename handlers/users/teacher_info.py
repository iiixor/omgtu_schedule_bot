from aiogram import types
from keyboards.inline.inline_days_of_week import *
from loader import dp, bot


from core import *
from core.find_teacher import *
from keyboards.inline.callback_datas import *
from parsing_data.parsing_main import *
from keyboards.default.menu import *
from keyboards.inline.inline_subscribe import *
from keyboards.default.menu import menu
from core.find_teacher import *
from database.classes import *
from core.find_group import *
from aiogram.types import CallbackQuery

database = Database()
database.path = 'database/users.db'
path = database.path

today = datetime.datetime.now().replace(second=0, microsecond=0)
Omsk_hour = datetime.timedelta(hours=3)
date_time_tomorrow_for_OMSK = datetime.timedelta(days= 1, hours =3)

@dp.message_handler(text=f'Найти преподавателя')
async def prep(message:types.Message):
    await message.answer(f'Введите фамилию преподавателя или его Ф.И.О:\n\n В формате: <b>Фамилия.И.О</b>\n\nНапример: <code>Панин.Ю.Н</code>', reply_markup=menu)


@dp.message_handler()
async def prep(message:types.Message):
    print(message.text)
    text = find_teacher(message.text)
    print(text)
    if '  ' in text:
        text = text.replace('  ','')
    if text != 'Преподатель с такой фамилией не найден!\nПопробуйте еще раз!':
        await message.answer(text, reply_markup = Raspisanie_2)
        text = text.split()
        print(text[1:4])
        text = f'{text[1]}.{text[2][0]}.{text[3][0]}'
        database.change_value(path, message.from_user.id, 'find_teacher', text)
    else:
        await message.answer(text)

    

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '1p'))
async def ponedelnik(call:CallbackQuery):
    teacher = database.find_value(path, call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.09.05'
    text = get_teacher_schedule (teacher, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '2p'))
async def ponedelnik(call:CallbackQuery):
    teacher = database.find_value(path, call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.09.06'
    text = get_teacher_schedule (teacher, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '3p'))
async def ponedelnik(call:CallbackQuery):
    teacher = database.find_value(path, call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.09.07'
    text = get_teacher_schedule (teacher, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '4p'))
async def ponedelnik(call:CallbackQuery):
    teacher = database.find_value(path, call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.09.08'
    text = get_teacher_schedule (teacher, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)    

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '5p'))
async def ponedelnik(call:CallbackQuery):
    teacher = database.find_value(path, call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.09.09'
    text = get_teacher_schedule (teacher, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '6p'))
async def ponedelnik(call:CallbackQuery):
    teacher = database.find_value(path, call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.09.10'
    text = get_teacher_schedule (teacher, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '7p'))
async def ponedelnik(call:CallbackQuery):
    teacher = database.find_value(path, call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.09.11'
    text = get_teacher_schedule (teacher, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '8p'))
async def ponedelnik(call:CallbackQuery):
    teacher = database.find_value(path, call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.09.12'
    text = get_teacher_schedule (teacher, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '9p'))
async def ponedelnik(call:CallbackQuery):
    teacher = database.find_value(path, call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.09.13'
    text = get_teacher_schedule (teacher, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '10p'))
async def ponedelnik(call:CallbackQuery):
    teacher = database.find_value(path, call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.09.14'
    text = get_teacher_schedule (teacher, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '11p'))
async def ponedelnik(call:CallbackQuery):
    teacher = database.find_value(path, call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.09.15'
    text = get_teacher_schedule (teacher, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '12p'))
async def ponedelnik(call:CallbackQuery):
    teacher = database.find_value(path, call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.09.16'
    text = get_teacher_schedule (teacher, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '13p'))
async def ponedelnik(call:CallbackQuery):
    teacher = database.find_value(path, call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.09.17'
    text = get_teacher_schedule (teacher, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '15p'))
async def ponedelnik(call:CallbackQuery):
    Omsk_hours = today + Omsk_hour
    Omsk_hours = Omsk_hours.strftime("%Y.%m.%d")
    teacher = database.find_value(path, call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = Omsk_hours
    text = get_teacher_schedule (teacher, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '16p'))
async def ponedelnik(call:CallbackQuery):
    time_tomorrow_Omsk = today + date_time_tomorrow_for_OMSK
    time_tomorrow_Omsk = time_tomorrow_Omsk.strftime("%Y.%m.%d")
    teacher = database.find_value(path, call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = time_tomorrow_Omsk
    text = get_teacher_schedule (teacher, date, sub_bool)
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)