from aiogram import types
from loader import dp, bot
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import *
from filters.emoji import *
from parsing_data.parsing_main import *
from keyboards.default.menu import *
from keyboards.inline.inline_subscribe import *
from data.config import admins
from core.check_group import * 


@dp.message_handler(text=f'Личный кабинет')
async def bot_data_request(message: types.Message):
    subscribe_format=''
    if message.from_user.id in admins:
        subscribe_format='Полный ✅'
    else:
        subscribe_format='Бесплатный ❌'

    if subscribe_format == 'Бесплатный ❌':
        text = [
        f'<b>Ваше имя:</b> {message.from_user.full_name}',
        f'<b>Ваш ID:</b> {message.from_user.id}',
        f'<b>Номер группы:</b>',
        f'<b>Формат подписки</b>: {subscribe_format}',
        ]
        markup = subscribe_button_yes
    else:
        text = [
        f'<b>Ваше имя:</b> {message.from_user.full_name}',
        f'<b>Ваш ID:</b> {message.from_user.id}',
        f'<b>Номер группы:</b>',
        f'<b>Формат подписки</b>: {subscribe_format}',
        f'<b>Подписка истекает:</b> 01.01.2077',
        ]
        markup = subscribe_button_cancel
    await message.answer("\n".join(text), reply_markup=markup)

@dp.callback_query_handler(subscribe_callback.filter(type='group'))
async def group_choose(call:CallbackQuery):
    text = 'Введите номер группы\n <i>Например: ПМм-221/1</i>'
    await call.message.answer(text)

@dp.message_handler()
async def check_group_tg(message:types.Message):
    text = check_group(message.text)
    await message.answer(text)








