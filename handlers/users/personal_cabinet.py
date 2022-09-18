from aiogram import types
import data
from loader import dp, bot
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import *
from filters.emoji import *
from parsing_data.parsing_main import *
from keyboards.default.menu import *
from keyboards.inline.inline_subscribe import *
from data.config import admins
from core.check_group import * 
from database.classes import *
from handlers.users.subscribe import *

database = Database()
database.path = 'database/users.db'
path = database.path


def str_to_date(str_date):
    return datetime.datetime.strptime(str_date,'%Y.%m.%d').date()

@dp.message_handler(text=f'Личный кабинет')
async def bot_data_request(message: types.Message):
    user_id = message.from_user.id
    sub_expiration = database.find_value(path, message.from_user.id, 'sub_expiration')
    sub_expiration = str_to_date(sub_expiration)
    sub_format = database.find_value(path, message.from_user.id, 'sub_format')
    group = database.find_value(path, user_id, 'user_group')
    today = datetime.date.today()
    if today >= sub_expiration and sub_format=="Free_pass":
        database.change_value(path, message.from_user.id, 'sub_format', 'Free_pass_used')
    # print(group)

    subscribe_format=''
    if sub_format == 'Full' or sub_format == 'Free_pass':
        subscribe_format='Полный ✅'
    else:
        subscribe_format='Бесплатный ❌'

    if sub_format == 'Free':
        text = [
        f'<b>Ваше имя:</b> {message.from_user.full_name}',
        f'<b>Ваш ID:</b> {message.from_user.id}',
        f'Группы: <code>{group}</code>',
        f'<b>Формат подписки</b>: {subscribe_format}',
        ]
        markup = subscribe_button_free_pass
    elif sub_format == 'Full' :
        sub_expiration = database.find_value(path, user_id, 'sub_expiration')
        text = [
        f'<b>Ваше имя:</b> {message.from_user.full_name}',
        f'<b>Ваш ID:</b> {message.from_user.id}',
        f'Группы: <code>{group}</code>',
        f'<b>Формат подписки</b>: {subscribe_format}',
        f'<b>Подписка истекает:</b> {sub_expiration}',
        ]
        markup = subscribe_button_cancel
    elif sub_format == 'Free_pass':
        sub_expiration = database.find_value(path, user_id, 'sub_expiration')
        text = [
        f'<b>Ваше имя:</b> {message.from_user.full_name}',
        f'<b>Ваш ID:</b> {message.from_user.id}',
        f'Группы: <code>{group}</code>',
        f'<b>Формат подписки</b>: {subscribe_format}',
        f'<b>Подписка истекает:</b> {sub_expiration}',
        ]
        markup = subscribe_button_cancel
    elif sub_format == 'Free_pass_used':
        text = [
        f'<b>Ваше имя:</b> {message.from_user.full_name}',
        f'<b>Ваш ID:</b> {message.from_user.id}',
        f'Группы: <code>{group}</code>',
        f'<b>Формат подписки</b>: {subscribe_format}',
        ]
        markup = subscribe_button_yes

    await message.answer("\n".join(text), reply_markup=markup)

@dp.callback_query_handler(subscribe_callback.filter(type='group'))
async def group_choose(call:CallbackQuery):
    text = 'Введите номер группы\nНапример: <code>ПМм-221/1</code>'
    await call.message.answer(text)

@dp.message_handler(text_contains = "-")
async def check_group_tg(message:types.Message):
    text = check_group(message.text)
    if text == 'Группа найдена':
        user_id = message.from_user.id
        new_value = message.text
        column = 'user_group'
        database.change_value(path, user_id, column, new_value)
        await message.answer(text)
    else:
        await message.answer(text)








