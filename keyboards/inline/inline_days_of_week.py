from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from keyboards.inline.callback_datas import *


Raspisanie = InlineKeyboardMarkup(row_width=7, inline_keyboard=[
        [
            InlineKeyboardButton(text=f'Пн', callback_data=raspisanie_callback.new(pn = '1')),
            InlineKeyboardButton(text=f'Вт', callback_data=raspisanie_callback.new(pn = '2')),
            InlineKeyboardButton(text=f'Ср', callback_data=raspisanie_callback.new(pn = '3')),
            InlineKeyboardButton(text=f'Чт', callback_data=raspisanie_callback.new(pn = '4')),
            InlineKeyboardButton(text=f'Пт', callback_data=raspisanie_callback.new(pn = '5')),
            InlineKeyboardButton(text=f'Сб', callback_data=raspisanie_callback.new(pn = '6')),
        ],
        [
            InlineKeyboardButton(text=f'Пн', callback_data=raspisanie_callback.new(pn = '8')),
            InlineKeyboardButton(text=f'Вт', callback_data=raspisanie_callback.new(pn = '9')),
            InlineKeyboardButton(text=f'Ср', callback_data=raspisanie_callback.new(pn = '10')),
            InlineKeyboardButton(text=f'Чт', callback_data=raspisanie_callback.new(pn = '11')),
            InlineKeyboardButton(text=f'Пт', callback_data=raspisanie_callback.new(pn = '12')),
            InlineKeyboardButton(text=f'Сб', callback_data=raspisanie_callback.new(pn = '13')),
        ],
        [
           InlineKeyboardMarkup(text=f'Сегодня', callback_data= raspisanie_callback.new(pn = '15')),
           InlineKeyboardMarkup(text=f'Завтра', callback_data= raspisanie_callback.new(pn = '16'))
        ]
    ]
)
