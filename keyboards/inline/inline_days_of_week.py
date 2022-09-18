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

Raspisanie_2 = InlineKeyboardMarkup(row_width=7, inline_keyboard=[
        [
            InlineKeyboardButton(text=f'Пн', callback_data=raspisanie_callback_2.new(pn = '1p')),
            InlineKeyboardButton(text=f'Вт', callback_data=raspisanie_callback_2.new(pn = '2p')),
            InlineKeyboardButton(text=f'Ср', callback_data=raspisanie_callback_2.new(pn = '3p')),
            InlineKeyboardButton(text=f'Чт', callback_data=raspisanie_callback_2.new(pn = '4p')),
            InlineKeyboardButton(text=f'Пт', callback_data=raspisanie_callback_2.new(pn = '5p')),
            InlineKeyboardButton(text=f'Сб', callback_data=raspisanie_callback_2.new(pn = '6p')),
        ],
        [
            InlineKeyboardButton(text=f'Пн', callback_data=raspisanie_callback_2.new(pn = '8p')),
            InlineKeyboardButton(text=f'Вт', callback_data=raspisanie_callback_2.new(pn = '9p')),
            InlineKeyboardButton(text=f'Ср', callback_data=raspisanie_callback_2.new(pn = '10p')),
            InlineKeyboardButton(text=f'Чт', callback_data=raspisanie_callback_2.new(pn = '11p')),
            InlineKeyboardButton(text=f'Пт', callback_data=raspisanie_callback_2.new(pn = '12p')),
            InlineKeyboardButton(text=f'Сб', callback_data=raspisanie_callback_2.new(pn = '13p')),
        ],
        [
           InlineKeyboardMarkup(text=f'Сегодня', callback_data= raspisanie_callback.new(pn = '15p')),
           InlineKeyboardMarkup(text=f'Завтра', callback_data= raspisanie_callback.new(pn = '16p'))
        ]
    ]
)
