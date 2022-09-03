from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from keyboards.inline.callback_datas import *


Raspisanie = InlineKeyboardMarkup(row_width=7, inline_keyboard=[
        
        [
            InlineKeyboardButton(text=f'Пн', callback_data=subscribe_callback.new(type='1')),
            InlineKeyboardButton(text=f'Вт', callback_data=subscribe_callback.new(type='2')),
            InlineKeyboardButton(text=f'Ср', callback_data=subscribe_callback.new(type='3')),
            InlineKeyboardButton(text=f'Чт', callback_data=subscribe_callback.new(type='4')),
            InlineKeyboardButton(text=f'Пт', callback_data=subscribe_callback.new(type='5')),
            InlineKeyboardButton(text=f'Сб', callback_data=subscribe_callback.new(type='6')),
            InlineKeyboardButton(text=f'Вс', callback_data=subscribe_callback.new(type='7'))
        ],
                [
            InlineKeyboardButton(text=f'Пн', callback_data=subscribe_callback.new(type='1')),
            InlineKeyboardButton(text=f'Вт', callback_data=subscribe_callback.new(type='2')),
            InlineKeyboardButton(text=f'Ср', callback_data=subscribe_callback.new(type='3')),
            InlineKeyboardButton(text=f'Чт', callback_data=subscribe_callback.new(type='4')),
            InlineKeyboardButton(text=f'Пт', callback_data=subscribe_callback.new(type='5')),
            InlineKeyboardButton(text=f'Сб', callback_data=subscribe_callback.new(type='6')),
            InlineKeyboardButton(text=f'Вс', callback_data=subscribe_callback.new(type='7'))
        ],  
        [
           InlineKeyboardButton(text=f'Сегодня', callback_data=subscribe_callback.new(type='1')) 
        ],
        [
           InlineKeyboardButton(text=f'Завтра', callback_data=subscribe_callback.new(type='1')) 
        ],
        [
           InlineKeyboardButton(text=f'Выбрать дату', callback_data=subscribe_callback.new(type='1')) 
        ]
    ]    
    
)