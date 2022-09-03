from aiogram import types
from loader import dp,bot

from keyboards.inline.raspisanie_dnya import *

@dp.message_handler(text=f'Выбор дня')
async def mmm(message:types.Message):
    text = [
        '<b>-Верхняя неделя</b>',
        '<b>-Нижняя неделя</b>'
    ]
    await message.answer("\n".join(text), reply_markup=Raspisanie)