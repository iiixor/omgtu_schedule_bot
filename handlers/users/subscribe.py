from email import message
from aiogram import types
from loader import dp, bot
from aiogram.types import CallbackQuery

from keyboards.inline.inline_switсh_language import *
from keyboards.inline.callback_datas import *
from filters.emoji import *
from parsing_data.parsing_main import *
from keyboards.default.menu import *
from keyboards.inline import inline_subscribe 

all_groups='БИТ-202 : 21, Хм-221 : 749 Э-203 : 775ТЭ-212 : 724Э-194 : 771ПИН-201 : 548ТСН-192 : 712'

@dp.callback_query_handler(subscribe_callback.filter(type='yes'))
async def bot_get_russian(call: CallbackQuery):
    allert_text = f'# ДОБАВИТЬ ПЛАТЕЖКУ'
    await call.answer(allert_text, show_alert=False)

@dp.callback_query_handler(subscribe_callback.filter(type='cancel'))
async def bot_get_russian(call: CallbackQuery):
    allert_text = f'# ДОБАВИТЬ ПЛАТЕЖКУ'
    await call.answer(allert_text, show_alert=False)
