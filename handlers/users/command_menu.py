from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.default import menu
from loader import dp, bot
from aiogram import types

@dp.message_handler(commands=['menu'])
async def mm(message: types.Message):
    await message.delete()
    await message.answer("Вы перешли в главное меню", reply_markup=menu)
