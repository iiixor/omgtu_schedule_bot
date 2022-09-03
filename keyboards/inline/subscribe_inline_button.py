from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from keyboards.inline.callback_datas import *
from filters.emoji import *

ADMIN_LINK = "https://t.me/wywmusic"

subscribe_button_yes = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [
            InlineKeyboardButton(text=f'Оформить подписку ✅', callback_data=subscribe_callback.new(type='yes')),
            InlineKeyboardButton(text=f'Написать в поддержку 👨‍🔧', callback_data=media_callback.new(platform='support'), url=ADMIN_LINK)
        ],
        
        [
           InlineKeyboardButton(text=f'Изменить группу', callback_data=prepod_callback.new(fio='fioo')) 
        ]
    
    ]
)

subscribe_button_cancel = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [
            InlineKeyboardButton(text=f'Написать в поддержку 👨‍🔧', callback_data=media_callback.new(platform='support'), url=ADMIN_LINK),
            InlineKeyboardButton(text=f'Отменить подписку 🚫', callback_data="subscribe:cancel")
        ],
        [
           InlineKeyboardButton(text=f'Изменить группу', callback_data=subscribe_callback.new(type='1')) 
        ]
    ]
)
