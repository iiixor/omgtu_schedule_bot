from aiogram import types
from loader import dp, bot

@dp.message_handler(commands=['support'])
async def sup(message:types.Message):
    await message.delete()
    await message.answer('чубзик поддержки')