from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.default import menu
from loader import dp, bot
from aiogram import types

@dp.message_handler(commands=['contacs'])
async def mm(message: types.Message):
    await message.delete()
    text = [
        f" Кафедра 1: <code>89854763245</code>",
        f'Кафедра 2: <code>89854763245</code>',
        f'Деканат ФИТиКс:<code>8(3812)65-22-08</code>',
        f'Деканат ФТНГ:<code>8(3812)65-26-09</code>',
        f'Деканат РТФ:<code>8(3812)65-20-93</code>',
        f'Деканат ФЭСиУ:<code>8(3812)24-28-43</code>',
        f'Деканат ХТФ:<code>8(3812)24-28-07</code>',
        f'Деканат ФГО:<code>8(3812)65-27-98</code>',
        f'Деканат ФЭОиМ:<code>8(3812)60-59-46</code>',
        f'Деканат ФДП:<code>8(3812)65-25-29</code>',


    ]
    await message.answer("\n\n".join(text), reply_markup=menu)
    