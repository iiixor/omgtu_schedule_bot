from aiogram import types
from loader import dp, bot
from aiogram.types import CallbackQuery

from keyboards.inline.inline_switсh_language import *
from keyboards.inline.callback_datas import *
from filters.emoji import *
from parsing_data.parsing_main import *
from keyboards.default.menu import *
from keyboards.inline import subscribe_inline_button


@dp.callback_query_handler(subscribe_callback.filter(type='yes'))
async def bot_get_russian(call: CallbackQuery):
    allert_text = f'# ДОБАВИТЬ ПЛАТЕЖКУ'
    await call.answer(allert_text, show_alert=False)

@dp.callback_query_handler(subscribe_callback.filter(type='cancel'))
async def bot_get_russian(call: CallbackQuery):
    allert_text = f'# ДОБАВИТЬ ПЛАТЕЖКУ'
    await call.answer(allert_text, show_alert=False)
