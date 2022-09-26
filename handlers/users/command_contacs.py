from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.default import menu
from loader import dp, bot
from aiogram import types

@dp.message_handler(commands=['contacs'])
async def mm(message: types.Message):
    await message.delete()
    text = [
        f'Деканат ФИТиКс: <code>83812652208</code>',
        f'Деканат ФТНГ: <code>83812652609</code>',
        f'Деканат РТФ: <code>83812652093</code>',
        f'Деканат ФЭСиУ: <code>83812242843</code>',
        f'Деканат ХТФ: <code>83812242807</code>',
        f'Деканат ФГО: <code>83812652798</code>',
        f'Деканат ФЭОиМ: <code>83812605946</code>',
        f'Деканат ФДП: <code>83812652529</code>',
    ]
    await message.answer("\n\n".join(text), reply_markup=menu)
    