from aiogram import types
from loader import dp

@dp.message_handler()
async def unknown_msg(message: types.Message):
    await message.answer(f'К сожалению, я не знаю такой команды')
