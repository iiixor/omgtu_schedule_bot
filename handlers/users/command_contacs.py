from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.default import menu
from loader import dp, bot
from aiogram import types

@dp.message_handler(commands=['contacs'])
async def mm(message: types.Message):
    await message.delete()
    text = [
        f" Кафедра 1: <code>89854763245</code>",
        f'Кафедра 2: <code>89854763245</code>'
    ]
    await message.answer("\n\n".join(text), reply_markup=menu)
    