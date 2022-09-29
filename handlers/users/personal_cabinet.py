from aiogram import types
import data
from loader import dp, bot
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import *
from keyboards.default.menu import *
from keyboards.inline.inline_subscribe import *
from data.config import admins
from database.classes import *
from handlers.users.subscribe import *

@dp.message_handler(text=f'Личный кабинет')
async def bot_data_request(message: types.Message):
    user_id = message.from_user.id
    text = [
        f'<b>Ваше имя:</b> {message.from_user.full_name}',
        f'<b>Ваш ID:</b> {message.from_user.id}',
        ]
    await message.answer(text)
    await message.answer("\n".join(text))








