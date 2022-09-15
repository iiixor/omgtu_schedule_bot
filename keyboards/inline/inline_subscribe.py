from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from keyboards.inline.callback_datas import *
from filters.emoji import *

ADMIN_LINK = "https://t.me/wywmusic"
bot = "@omgtu_schedule_bot"

subscribe_button_yes = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
        [
            InlineKeyboardButton(text=f'Выбрать группу',callback_data=subscribe_callback.new(type='group'))
        ],
        [
            InlineKeyboardButton(text=f'Оформить подписку ✅', callback_data=subscribe_callback.new(type='yes')),
        ],
        [
            InlineKeyboardButton(text=f'Написать в поддержку 👨‍🔧', callback_data=media_callback.new(platform='support'), url=ADMIN_LINK)
        ],

    ]
)

subscribe_button_cancel = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
        [
           InlineKeyboardButton(text=f'Выбрать группу', callback_data=subscribe_callback.new(type='group'))
        ],
        [
            InlineKeyboardButton(text=f'Написать в поддержку 👨‍🔧', callback_data=media_callback.new(platform='support'), url=ADMIN_LINK)
        ],
    ]
)

subscribe_button_free_pass = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
        [
            InlineKeyboardButton(text=f'Выбрать группу',callback_data=subscribe_callback.new(type='group'))
        ],
        [
            InlineKeyboardButton(text=f'Получить неделю бесплатно ✅', callback_data=subscribe_callback.new(type='free_pass')),
        ],
        [
            InlineKeyboardButton(text=f'Написать в поддержку 👨‍🔧', callback_data=media_callback.new(platform='support'), url=ADMIN_LINK)
        ],

    ]
)

subscribe_button_sub_variants = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
        [
            InlineKeyboardButton(text=f'900₽ / Год ',callback_data=subscribe_callback.new(type='year'))
        ],
        [
            InlineKeyboardButton(text=f'500₽ / Пол года', callback_data=subscribe_callback.new(type='half_year')),
        ],
        [
            InlineKeyboardButton(text=f'100₽ / Месяц', callback_data=subscribe_callback.new(type='month')),
        ],

    ]
)


