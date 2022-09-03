from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


from keyboards.inline.callback_datas import *
from filters.emoji import *


# пишем ссылки для тех кнопок, которые перекидывают на ссылки
GIT_HUB_LINK = "https://github.com/wywdelpy"
KWORK_LINK = "https://kwork.ru/user/alex_odin"
ADMIN_LINK = "https://t.me/wywmusic"
GOOGLE_FORM_LINK = 'https://forms.gle/tvdUTDby1CVD4yno7'

# по своей структуре очень похоже на созадние обычных кнопок
# добавляем клавиатуру и передаем в нее метод inline_keyboard
# внутри которого добавляем сами кнопки с обязательным параметром text
# также внутрь передаем callback_data для созданию тригера на кнопку тк сказать
# обратите внимание на то, как меняется callback_data при первом упоминании и при втором


switch_language = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [
            InlineKeyboardButton(text=f'Русский {emoji_ruflag}', callback_data=switch_callback.new(language='russian'))
        ],
        [
            InlineKeyboardButton(text=f'English {emoji_engflag}', callback_data="switcher:english")
        ]
    ]
)

# по сути то же самое, что сверху
# однако тут обратите внимание, что еще передается url, данный параметр
# при нажатии кнопку пересылает по ссылке

media_buttons = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
        [
            InlineKeyboardButton(text=f'Git Hub {emoji_cat}', callback_data=media_callback.new(platform='git_hub'), url=GIT_HUB_LINK)
        ],
        [
            InlineKeyboardButton(text=f'Kwork {emoji_chain}', callback_data="media:kwork", url=KWORK_LINK)
        ],
        [
            InlineKeyboardButton(text=f'Задать вопрос {emoji_questionmark}', callback_data="media:answer", url=ADMIN_LINK),
            InlineKeyboardButton(text=f'Рассказать друзьям 💁‍♀️', switch_inline_query='Вот, как разрабатывают ботов!')
        ]
    ]
)

# по сути то же самое, что сверху

poll_buttons = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [
            InlineKeyboardButton(text='Google Forms', callback_data=poll_callback.new(platform='google_forms'), url=GOOGLE_FORM_LINK)
        ]
    ]
)

# на этом шаге, я думаю понятно, как создавать кнопки в этой дир-и

review_buttons = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
        [
            InlineKeyboardButton(text='Платформа №1', callback_data=review_callback.new(platform='platform_1'))
        ],
        [
            InlineKeyboardButton(text='Оставить отзыв', callback_data="review:write_a_review")
        ]
    ]
)


choice_buttons = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
        [
            InlineKeyboardButton(text=f'Да', callback_data=choice_callback.new(type='yes'))
        ],
        [
            InlineKeyboardButton(text=f'Нет', callback_data="choice:no")
        ]
    ]
)

skills_buttons = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(text=f'Характер', callback_data=skills_callback.new(type='character')),
        InlineKeyboardButton(text=f'Энергия', callback_data='skill:energy')
    ],
    [
        InlineKeyboardButton(text=f'Интерес', callback_data='skill:interest'),
        InlineKeyboardButton(text=f'Здоровье', callback_data='skill:health')
    ],
    [
        InlineKeyboardButton(text=f'Логика, Интуиация', callback_data='skill:logic'),
        InlineKeyboardButton(text=f'Труд', callback_data='skill:labour')
    ],
    [
        InlineKeyboardButton(text=f'Удача', callback_data='skill:luck'),
        InlineKeyboardButton(text=f'Чувство долга', callback_data='skill:duty')
    ],    
    [
        InlineKeyboardButton(text=f'Память', callback_data='skill:memory'),
        InlineKeyboardButton(text=f'Целеустрмленность', callback_data='skill:сommitment')
    ],    
    [
        InlineKeyboardButton(text=f'Семья', callback_data='skill:family'),
        InlineKeyboardButton(text=f'Стабильность', callback_data='skill:stability')
    ],    
    [
        InlineKeyboardButton(text=f'Самоценка', callback_data='skill:self_esteem'),
        InlineKeyboardButton(text=f'Материальная независимость', callback_data='skill:material_independence')
    ],    
    [
        InlineKeyboardButton(text=f'Талант', callback_data='skill:talant'),
        InlineKeyboardButton(text=f'Темперамент', callback_data='skill:tempepament')
    ],        
    [
        InlineKeyboardButton(text=f'Духовность', callback_data='skill:spirit'),
    ],

    ]
)