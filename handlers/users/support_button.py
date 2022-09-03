from aiogram import types
from loader import dp, bot

from keyboards.default import menu

@dp.message_handler(text=f'Обратная связь')
async def supsup(message:types.Message):
    await message.delete()
    await message.answer('чубзик поддержки', reply_markup=menu)
