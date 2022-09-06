from aiogram import types
from keyboards.inline import callback_datas
from loader import dp,bot
from keyboards.inline import map_inline
from keyboards.inline.callback_datas import *
from aiogram.types import CallbackQuery
from keyboards.inline.map_inline import *


@dp.message_handler(text=f'Карта университета')
async def map(message: types.Message):
    await message.answer('Выберите корпус', reply_markup=map_pg1)


@dp.callback_query_handler(page_switcher_callback.filter(number = "1"))
async def M(call:CallbackQuery):
    await call.message.edit_text(text = "Страница 1", reply_markup=map_pg1)
    

@dp.callback_query_handler(page_switcher_callback.filter(number = "2"))
async def D(call:CallbackQuery):
    await call.message.edit_text(text = "Страница 2", reply_markup=map_pg2)

@dp.callback_query_handler(page_switcher_callback.filter(number = "3"))
async def M(call:CallbackQuery):
    await call.message.edit_text(text = "Страница 3", reply_markup=map_pg3)

#-----------------------------------------------------------Гео кнопкам

@dp.callback_query_handler(page_switcher_callback.filter(number = "3"))
async def M(call:CallbackQuery):
    await call.message.edit_text(text = "Страница 3", reply_markup=map_pg3)












# @dp.callback_query_handler(text_startswith="prev")
# async def prev_page(call: types.CallbackQuery):
#     await call.answer()
#     data = int(call.data.split(":")[1]) - 1

#     markup = InlineKeyboardMarkup().add(
#         InlineKeyboardButton("PREV", callback_data=f"prev:{data}"),
#         #InlineKeyboardButton(str(data), callback_data="null"),
#         InlineKeyboardButton("NEXT", callback_data=f"next:{data}"),
#     )
#     await call.message.edit_text("text", reply_markup=markup)


# @dp.callback_query_handler(text_startswith="next")
# async def next_page(call: types.CallbackQuery):
#     await call.answer()
#     data = int(call.data.split(":")[1]) + 1

#     markup = InlineKeyboardMarkup().add(
#         InlineKeyboardButton("PREV", callback_data=f"prev:{data}"),
#         #InlineKeyboardButton(str(data), callback_data="null"),
#         InlineKeyboardButton("NEXT", callback_data=f"next:{data}"),
#     )
#     await call.message.edit_text("Стр 2", reply_markup=markup)


# @dp.message_handler(commands=["uuu"])
# async def handler(msg: types.Message):
#     markup = InlineKeyboardMarkup().add(
#         InlineKeyboardButton("<<", callback_data=f"prev:0"),
#         #InlineKeyboardButton("0", callback_data="null"),
#         InlineKeyboardButton(">>", callback_data=f"next:1")
#     )
#     await msg.answer("Выберите один из корпусов", reply_markup=map_pg1)
#     await msg.answer('aaa', reply_markup=markup)


