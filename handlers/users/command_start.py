from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot
# достаем menu из дир-и delpy_bot -> keyboards -> default
from keyboards.default import menu
from filters.emoji import *


# @dp.message_handler ловит только комманду /start
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    # выводим текст методом message.answer
    # и в аргументе предаем прям тот, текст, который выведется
    # при вводе /start также появляется menu с кнпоками, благодаря
    # reply_markup=menu
    # menu указывается в keyboards->default->menu
    # gif = 'media/space.gif'
    await message.delete()
    text = f'<b>Omgtu_bot</b> приветсвует тебя, {message.from_user.full_name} 👋'
    # await message.answer_animation(types.InputFile(gif))
    await message.answer(text, reply_markup=menu)


# @dp.message_handler()
# async def bot_delete(message: types.Message):
#     if message.from_user.id == (await bot.me).id:
#         await message.delete()
