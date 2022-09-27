from aiogram import types
from keyboards.inline.inline_days_of_week import *
from loader import dp, bot


from core import *
from core.find_teacher import *
from keyboards.inline.callback_datas import *
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
    sub_format = database.find_value(path, 'users', message.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        await message.answer(f'Введите фамилию преподавателя или его Ф.И.О:\n\n В формате: <b>Фамилия.И.О</b>\n\nНапример: <code>Панин.Ю.Н</code>', reply_markup=menu)
    elif sub_format == 'Free':
        await message.answer(f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Вы можете оформить пробную подписку на 2 недели в личном кабинете</b></u> \n\n Введите фамилию преподавателя или его Ф.И.О:\n\n В формате: <b>Фамилия.И.О</b>\n\nНапример: <code>Панин.Ю.Н</code>', reply_markup=menu)
    else:
        await message.answer(f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Подписку можно оформить в личном кабинете</b></u> \n\n Введите фамилию преподавателя или его Ф.И.О:\n\n В формате: <b>Фамилия.И.О</b>\n\nНапример: <code>Панин.Ю.Н</code>', reply_markup=menu)    
        


@dp.message_handler()
async def prep(message:types.Message):
    text = find_teacher(message.text)
    if '  ' in text:
        text = text.replace('  ','')
    if text != 'Преподатель с такой фамилией не найден!\nПопробуйте еще раз!':
        await message.answer(text, reply_markup = Raspisanie_2)
        text = text.split()
        text = f'{text[1]}.{text[2][0]}.{text[3][0]}'
        database.change_value(path, 'users', message.from_user.id, 'find_teacher', text)
    else:
        await message.answer(text)

    

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '1p'))
async def ponedelnik(call:CallbackQuery):
    teacher = database.find_value(path, 'users', call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, 'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.10.09'
    if sub_format == 'Full' or sub_format == "Free_pass":
        text = get_teacher_schedule(teacher, date, sub_bool)
    elif sub_format == 'Free':
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Вы можете оформить пробную подписку на 2 недели в личном кабинете</b></u>\n{get_teacher_schedule(teacher, date, sub_bool)}'
    else:
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Подписку можно оформить в личном кабинете</b></u> \n{get_teacher_schedule(teacher, date, sub_bool)}'
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '2p'))
async def ponedelnik(call:CallbackQuery):
    teacher = database.find_value(path, 'users', call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, 'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.10.10'
    if sub_format == 'Full' or sub_format == "Free_pass":
        text = get_teacher_schedule(teacher, date, sub_bool)
    elif sub_format == 'Free':
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Вы можете оформить пробную подписку на 2 недели в личном кабинете</b></u>\n,{get_teacher_schedule(teacher, date, sub_bool)}'
    else:
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Подписку можно оформить в личном кабинете</b></u>\n\nВведите фамилию преподавателя или его Ф.И.О:\n\nВ формате: <b>Фамилия.И.О</b>\n\nНапример: <code>Панин.Ю.Н</code>',{get_teacher_schedule(teacher, date, sub_bool)}
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '3p'))
async def ponedelnik(call:CallbackQuery):
    teacher = database.find_value(path, 'users', call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, 'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.10.11'
    if sub_format == 'Full' or sub_format == "Free_pass":
        text = get_teacher_schedule(teacher, date, sub_bool)
    elif sub_format == 'Free':
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Вы можете оформить пробную подписку на 2 недели в личном кабинете</b></u>\n{get_teacher_schedule(teacher, date, sub_bool)}'
    else:
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Подписку можно оформить в личном кабинете</b></u>\n\nВведите фамилию преподавателя или его Ф.И.О:\n\nВ формате: <b>Фамилия.И.О</b>\n\nНапример: <code>Панин.Ю.Н</code>',{get_teacher_schedule(teacher, date, sub_bool)}
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '4p'))
async def ponedelnik(call:CallbackQuery):
    teacher = database.find_value(path, 'users', call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, 'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.10.12'
    if sub_format == 'Full' or sub_format == "Free_pass":
        text = get_teacher_schedule(teacher, date, sub_bool)
    elif sub_format == 'Free':
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Вы можете оформить пробную подписку на 2 недели в личном кабинете</b></u>\n{get_teacher_schedule(teacher, date, sub_bool)}'
    else:
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Подписку можно оформить в личном кабинете</b></u>\n\nВведите фамилию преподавателя или его Ф.И.О:\n\nВ формате: <b>Фамилия.И.О</b>\n\nНапример: <code>Панин.Ю.Н</code>',{get_teacher_schedule(teacher, date, sub_bool)}
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)    

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '5p'))
async def ponedelnik(call:CallbackQuery):
    teacher = database.find_value(path, 'users', call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, 'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.10.13'
    if sub_format == 'Full' or sub_format == "Free_pass":
        text = get_teacher_schedule(teacher, date, sub_bool)
    elif sub_format == 'Free':
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Вы можете оформить пробную подписку на 2 недели в личном кабинете</b></u>\n{get_teacher_schedule(teacher, date, sub_bool)}'
    else:
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Подписку можно оформить в личном кабинете</b></u>\n\nВведите фамилию преподавателя или его Ф.И.О:\n\nВ формате: <b>Фамилия.И.О</b>\n\nНапример: <code>Панин.Ю.Н</code>',{get_teacher_schedule(teacher, date, sub_bool)}
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '6p'))
async def ponedelnik(call:CallbackQuery):
    teacher = database.find_value(path, 'users', call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, 'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.10.14'
    if sub_format == 'Full' or sub_format == "Free_pass":
        text = get_teacher_schedule(teacher, date, sub_bool)
    elif sub_format == 'Free':
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Вы можете оформить пробную подписку на 2 недели в личном кабинете</b></u>\n{get_teacher_schedule(teacher, date, sub_bool)}'
    else:
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Подписку можно оформить в личном кабинете</b></u>\n\nВведите фамилию преподавателя или его Ф.И.О:\n\nВ формате: <b>Фамилия.И.О</b>\n\nНапример: <code>Панин.Ю.Н</code>',{get_teacher_schedule(teacher, date, sub_bool)}
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '7p'))
async def ponedelnik(call:CallbackQuery):
    teacher = database.find_value(path, 'users', call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, 'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.10.15'
    if sub_format == 'Full' or sub_format == "Free_pass":
        text = get_teacher_schedule(teacher, date, sub_bool)
    elif sub_format == 'Free':
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Вы можете оформить пробную подписку на 2 недели в личном кабинете</b></u>\n{get_teacher_schedule(teacher, date, sub_bool)}'
    else:
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Подписку можно оформить в личном кабинете</b></u>\n\nВведите фамилию преподавателя или его Ф.И.О:\n\nВ формате: <b>Фамилия.И.О</b>\n\nНапример: <code>Панин.Ю.Н</code>',{get_teacher_schedule(teacher, date, sub_bool)}
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '8p'))
async def ponedelnik(call:CallbackQuery):
    teacher = database.find_value(path, 'users', call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, 'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.10.03'
    if sub_format == 'Full' or sub_format == "Free_pass":
        text = get_teacher_schedule(teacher, date, sub_bool)
    elif sub_format == 'Free':
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Вы можете оформить пробную подписку на 2 недели в личном кабинете</b></u>\n{get_teacher_schedule(teacher, date, sub_bool)}'
    else:
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Подписку можно оформить в личном кабинете</b></u>\n\nВведите фамилию преподавателя или его Ф.И.О:\n\nВ формате: <b>Фамилия.И.О</b>\n\nНапример: <code>Панин.Ю.Н</code>',{get_teacher_schedule(teacher, date, sub_bool)}
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '9p'))
async def ponedelnik(call:CallbackQuery):
    teacher = database.find_value(path, 'users', call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, 'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.10.04'
    if sub_format == 'Full' or sub_format == "Free_pass":
        text = get_teacher_schedule(teacher, date, sub_bool)
    elif sub_format == 'Free':
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Вы можете оформить пробную подписку на 2 недели в личном кабинете</b></u>\n{get_teacher_schedule(teacher, date, sub_bool)}'
    else:
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Подписку можно оформить в личном кабинете</b></u>\n\nВведите фамилию преподавателя или его Ф.И.О:\n\nВ формате: <b>Фамилия.И.О</b>\n\nНапример: <code>Панин.Ю.Н</code>',{get_teacher_schedule(teacher, date, sub_bool)}
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '10p'))
async def ponedelnik(call:CallbackQuery):
    teacher = database.find_value(path, 'users', call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, 'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.10.05'
    if sub_format == 'Full' or sub_format == "Free_pass":
        text = get_teacher_schedule(teacher, date, sub_bool)
    elif sub_format == 'Free':
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Вы можете оформить пробную подписку на 2 недели в личном кабинете</b></u>\n{get_teacher_schedule(teacher, date, sub_bool)}'
    else:
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Подписку можно оформить в личном кабинете</b></u>\n\nВведите фамилию преподавателя или его Ф.И.О:\n\nВ формате: <b>Фамилия.И.О</b>\n\nНапример: <code>Панин.Ю.Н</code>',{get_teacher_schedule(teacher, date, sub_bool)}
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '11p'))
async def ponedelnik(call:CallbackQuery):
    teacher = database.find_value(path, 'users', call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, 'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.10.06'
    if sub_format == 'Full' or sub_format == "Free_pass":
        text = get_teacher_schedule(teacher, date, sub_bool)
    elif sub_format == 'Free':
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Вы можете оформить пробную подписку на 2 недели в личном кабинете</b></u>\n{get_teacher_schedule(teacher, date, sub_bool)}'
    else:
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Подписку можно оформить в личном кабинете</b></u>\n\nВведите фамилию преподавателя или его Ф.И.О:\n\nВ формате: <b>Фамилия.И.О</b>\n\nНапример: <code>Панин.Ю.Н</code>',{get_teacher_schedule(teacher, date, sub_bool)}
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '12p'))
async def ponedelnik(call:CallbackQuery):
    teacher = database.find_value(path, 'users', call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, 'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.10.07'
    if sub_format == 'Full' or sub_format == "Free_pass":
        text = get_teacher_schedule(teacher, date, sub_bool)
    elif sub_format == 'Free':
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Вы можете оформить пробную подписку на 2 недели в личном кабинете</b></u>\n{get_teacher_schedule(teacher, date, sub_bool)}'
    else:
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Подписку можно оформить в личном кабинете</b></u>\n\nВведите фамилию преподавателя или его Ф.И.О:\n\nВ формате: <b>Фамилия.И.О</b>\n\nНапример: <code>Панин.Ю.Н</code>',{get_teacher_schedule(teacher, date, sub_bool)}
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '13p'))
async def ponedelnik(call:CallbackQuery):
    teacher = database.find_value(path, 'users', call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, 'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = '2022.10.08'
    if sub_format == 'Full' or sub_format == "Free_pass":
        text = get_teacher_schedule(teacher, date, sub_bool)
    elif sub_format == 'Free':
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Вы можете оформить пробную подписку на 2 недели в личном кабинете</b></u>\n{get_teacher_schedule(teacher, date, sub_bool)}'
    else:
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Подписку можно оформить в личном кабинете</b></u>\n\nВведите фамилию преподавателя или его Ф.И.О:\n\nВ формате: <b>Фамилия.И.О</b>\n\nНапример: <code>Панин.Ю.Н</code>',{get_teacher_schedule(teacher, date, sub_bool)}
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '15p'))
async def ponedelnik(call:CallbackQuery):
    Omsk_hours = today + Omsk_hour
    Omsk_hours = Omsk_hours.strftime("%Y.%m.%d")
    teacher = database.find_value(path, 'users', call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, 'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = Omsk_hours
    if sub_format == 'Full' or sub_format == "Free_pass":
        text = get_teacher_schedule(teacher, date, sub_bool)
    elif sub_format == 'Free':
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Вы можете оформить пробную подписку на 2 недели в личном кабинете</b></u>\n{get_teacher_schedule(teacher, date, sub_bool)}'
    else:
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Подписку можно оформить в личном кабинете</b></u>\n\nВведите фамилию преподавателя или его Ф.И.О:\n\nВ формате: <b>Фамилия.И.О</b>\n\nНапример: <code>Панин.Ю.Н</code>',{get_teacher_schedule(teacher, date, sub_bool)}
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)

@dp.callback_query_handler(raspisanie_callback_2.filter(pn = '16p'))
async def ponedelnik(call:CallbackQuery):
    time_tomorrow_Omsk = today + date_time_tomorrow_for_OMSK
    time_tomorrow_Omsk = time_tomorrow_Omsk.strftime("%Y.%m.%d")
    teacher = database.find_value(path, 'users', call.from_user.id , 'find_teacher')
    sub_format = database.find_value(path, 'users', call.from_user.id , 'sub_format')
    if sub_format == 'Full' or sub_format == "Free_pass":
        sub_bool = True
    else:
        sub_bool = False
    date = time_tomorrow_Omsk
    if sub_format == 'Full' or sub_format == "Free_pass":
        text = get_teacher_schedule(teacher, date, sub_bool)
    elif sub_format == 'Free':
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Вы можете оформить пробную подписку на 2 недели в личном кабинете</b></u>\n{get_teacher_schedule(teacher, date, sub_bool)}'
    else:
        text = f'<u><b>В связи с бесплатной подпиской, часть полей недоступно</b></u>,\n<u><b>Подписку можно оформить в личном кабинете</b></u>\n\nВведите фамилию преподавателя или его Ф.И.О:\n\nВ формате: <b>Фамилия.И.О</b>\n\nНапример: <code>Панин.Ю.Н</code>',{get_teacher_schedule(teacher, date, sub_bool)}
    await call.message.edit_text(text, disable_web_page_preview=True, reply_markup=Raspisanie_2)