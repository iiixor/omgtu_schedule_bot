import aiogram
from aiogram import types
from loader import dp,bot
from aiogram.types import CallbackQuery

from keyboards.inline.inline_subscribe import subscribe_button_yes
from keyboards.inline.callback_datas import referral_callback

@dp.callback_query_handler(referral_callback.filter(ref='someone'))
async def referral(call:CallbackQuery):
    await call.message.answer('asd')