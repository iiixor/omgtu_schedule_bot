import aiogram
from aiogram import types
from loader import dp,bot
from aiogram.types import CallbackQuery

from keyboards.inline.inline_subscribe import subscribe_button_yes
from keyboards.inline.callback_datas import referral_callback
from database.classes import *
from database import *

database = Database()
database.path = 'database/users.db'
path = database.path

@dp.callback_query_handler(referral_callback.filter(ref='someone'))
async def referral(call:CallbackQuery):
    user_id = call.from_user.id
    referral = database.find_value(path,'users', user_id, 'referrer_code')
    text = f'Ваш реферальный код:<code>{referral}</code>'
    await call.message.answer(text)