import aiogram
from loader import dp,bot

from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

i_paid = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f'Проверить оплату'),
            KeyboardButton(text=f'Отмена')
        ]
    ],resize_keyboard=True
)