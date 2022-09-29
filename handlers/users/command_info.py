from aiogram import types
from loader import dp, bot
import aiogram.utils.markdown as fmt

@dp.message_handler(commands=['info'])
async def information(message: types.Message):
    await message.delete()
    text = [

    ]
    await message.answer('\n'.join(text))