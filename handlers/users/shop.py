from loader import dp,bot
from aiogram import types
from keyboards.default.menu import *

@dp.message_handler(text=f'Магазин')
async def shop_menu(message:types.message):
    await message.answer('Salat alevkum')