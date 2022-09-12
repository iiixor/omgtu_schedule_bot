from aiogram import types
from loader import dp
from keyboards.inline.callback_datas import *
from aiogram.types import CallbackQuery
from keyboards.inline.inline_buildings import *



@dp.message_handler(text=f'Карта университета')
async def map(message: types.Message):
    await message.answer('Выберите корпус:', reply_markup=map_pg1)
    # return id

@dp.callback_query_handler(page_switcher_callback.filter(number = "1"))
async def M(call:CallbackQuery):
    await call.message.edit_text(text = "Выберите корпус:", reply_markup=map_pg1)
    print (call.message.message_id)


@dp.callback_query_handler(page_switcher_callback.filter(number = "2"))
async def D(call:CallbackQuery):
    await call.message.edit_text(text = "Выберите корпус:", reply_markup=map_pg2)
    print (call.message.message_id)

@dp.callback_query_handler(page_switcher_callback.filter(number = "3"))
async def M(call:CallbackQuery):
    await call.message.edit_text(text = "Выберите корпус:", reply_markup=map_pg3)
    print (call.message.message_id)


#-----------------------------------------------------------Гео кнопкам

@dp.callback_query_handler(map_callback.filter(type = "Main"))
async def main_map(call:CallbackQuery):
    # await call.message.delete()
    # await call.message.delete()
    # await call.message.answer('Выберите корпус:', reply_markup=map_pg1)
    # print (call.message.message_id)
    await call.message.answer_location(
        longitude = 73.290678,
        latitude = 55.026071)
    # print (call.message.message_id)
    # await call.message.edit_reply_markup()


@dp.callback_query_handler(map_callback.filter(type = "ulk-1"))
async def main_map(call:CallbackQuery):
    # id = id + 1
    # await call.message.delete()
    # await call.message.delete()
    #
    # await call.message.answer('Выберите корпус:', reply_markup=map_pg1)
    # print (call.message.message_id)
    await call.message.answer_location(
        longitude =  73.292188,
        latitude = 55.025415)
    # print (call.message.message_id)
    # await bot.delete_message(call.from_user.id, id)



@dp.callback_query_handler(map_callback.filter(type = "ulk-2"))
async def main_map(call:CallbackQuery):
    # id = id + 1
    # await call.message.delete()
    # await call.message.delete()
    # await call.message.delete()
    # await call.message.answer('Выберите корпус:', reply_markup=map_pg1)
    # print (call.message.message_id)
    await call.message.answer_location(
        longitude =  73.290197,
        latitude = 55.026075)
    # print (call.message.message_id)
    # await bot.delete_message(call.from_user.id, id)



@dp.callback_query_handler(map_callback.filter(type = "ulk-3"))
async def main_map(call:CallbackQuery):
    # await call.message.delete()
    # await call.message.delete()
    # # await call.message.delete()
    # await call.message.answer('Выберите корпус:', reply_markup=map_pg1)
    await call.message.answer_location(
        longitude =  73.356264,
        latitude = 55.016167)
    # await call.message.delete()


@dp.callback_query_handler(map_callback.filter(type = "ulk-4"))
async def main_map(call:CallbackQuery):
    await call.message.answer_location(
        longitude =  73.356264,
        latitude = 55.016167)


@dp.callback_query_handler(map_callback.filter(type = "ulk-5"))
async def main_map(call:CallbackQuery):
    await call.message.answer_location(
        longitude =  73.293499,
        latitude = 55.027129)


@dp.callback_query_handler(map_callback.filter(type = "ulk-6"))
async def main_map(call:CallbackQuery):
    await call.message.answer_location(
        longitude = 73.290678,
        latitude = 55.026071)

@dp.callback_query_handler(map_callback.filter(type = "ulk-7"))
async def main_map(call:CallbackQuery):
    await call.message.answer_location(
        longitude = 73.294263,
        latitude = 55.026855)

@dp.callback_query_handler(map_callback.filter(type = "ulk-8"))
async def main_map(call:CallbackQuery):
    await call.message.answer_location(
        longitude = 73.290678,
        latitude = 55.026071)

@dp.callback_query_handler(map_callback.filter(type = "ulk-9"))
async def main_map(call:CallbackQuery):
    await call.message.answer_location(
        longitude = 73.260459,
        latitude = 55.040348)


@dp.callback_query_handler(map_callback.filter(type = "ulk-10"))
async def main_map(call:CallbackQuery):
    await call.message.answer_location(
        longitude = 73.285729,
        latitude = 55.031355)


@dp.callback_query_handler(map_callback.filter(type = "ulk-11"))
async def main_map(call:CallbackQuery):
    await call.message.answer_location(
        longitude = 73.286052,
        latitude = 55.031861)


@dp.callback_query_handler(map_callback.filter(type = "ulk-12"))
async def main_map(call:CallbackQuery):
    await call.message.answer_location(
        longitude = 73.242645,
        latitude = 54.997910)


@dp.callback_query_handler(map_callback.filter(type = "ulk-13"))
async def main_map(call:CallbackQuery):
    await call.message.answer_location(
        longitude = 73.358726,
        latitude = 54.992239)


@dp.callback_query_handler(map_callback.filter(type = "ulk-14"))
async def main_map(call:CallbackQuery):
    await call.message.answer_location(
        longitude = 73.358672,
        latitude = 54.991149)


@dp.callback_query_handler(map_callback.filter(type = "UPM"))
async def main_map(call:CallbackQuery):
    await call.message.answer_location(
        longitude = 73.288325,
        latitude = 55.027139)


@dp.callback_query_handler(map_callback.filter(type = "FIZ"))
async def main_map(call:CallbackQuery):
    await call.message.answer_location(
        longitude = 73.290678,
        latitude = 55.026071)

@dp.callback_query_handler(map_callback.filter(type = "MEDST"))
async def main_map(call:CallbackQuery):
    await call.message.answer_location(
        longitude = 73.290678,
        latitude = 55.026071)

@dp.callback_query_handler(map_callback.filter(type = "BAS"))
async def main_map(call:CallbackQuery):
    await call.message.answer_location(
        longitude = 73.291918,
        latitude = 55.023640)


@dp.callback_query_handler(map_callback.filter(type = "vuk-1"))
async def main_map(call:CallbackQuery):
    await call.message.answer_location(
        longitude =  73.357145,
        latitude = 55.015614)

@dp.callback_query_handler(map_callback.filter(type = "vuk-2"))
async def main_map(call:CallbackQuery):
    await call.message.answer_location(
        longitude = 73.357558,
        latitude = 55.016435)


@dp.callback_query_handler(map_callback.filter(type = "vuk-3"))
async def main_map(call:CallbackQuery):
    await call.message.answer_location(
        longitude = 73.357145,
        latitude = 55.015614)


@dp.callback_query_handler(map_callback.filter(type = "vuk-4"))
async def main_map(call:CallbackQuery):
    await call.message.answer_location(
        longitude = 73.357145,
        latitude = 55.015614)


@dp.callback_query_handler(map_callback.filter(type = "vuk-5"))
async def main_map(call:CallbackQuery):
    await call.message.answer_location(
        longitude = 73.357145,
        latitude = 55.015614)


@dp.callback_query_handler(map_callback.filter(type = "vuk-6"))
async def main_map(call:CallbackQuery):
    await call.message.answer_location(
        longitude = 73.357558,
        latitude = 55.016435)



@dp.callback_query_handler(map_callback.filter(type = "vuk-7"))
async def main_map(call:CallbackQuery):
    await call.message.answer_location(
        longitude = 73.357145,
        latitude = 55.015614)

@dp.message_handler(content_types = types.ContentType.LOCATION)
async def main_map(message: types.Message):
    await message.delete()
















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
