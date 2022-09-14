import aiogram
from loader import dp,bot

from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

i_paid = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f'Я оплатил'),
            KeyboardButton(text=f'Отмена')
        ]
    ],resize_keyboard=True
)