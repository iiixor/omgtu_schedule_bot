from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from filters.emoji import *

aditional_numerology = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f'Характер'),
            KeyboardButton(text=f'Энергия')
        ],
        [
            KeyboardButton(text=f'Интерес'),
            KeyboardButton(text=f'Здоровье')
        ],
        [
            KeyboardButton(text=f'Логика, Интуиция'),
            KeyboardButton(text=f'Труд')
        ],
        [
            KeyboardButton(text=f'Удача'),
            KeyboardButton(text=f'Чувство долга')
        ],
        [
            KeyboardButton(text=f'Память'),
            KeyboardButton(text=f'Целеустремленность')
        ],
        [
            KeyboardButton(text=f'Семья'),
            KeyboardButton(text=f'Стабильность')
        ],
        [
            KeyboardButton(text=f'Самоценка'),
            KeyboardButton(text=f'Материальная независимость')
        ],
        [
            KeyboardButton(text=f'Талант'),
            KeyboardButton(text=f'Темеперамент')
        ],
        [
            KeyboardButton(text=f'Духовность')
        ]
    ],
    resize_keyboard=True
)

zodiacs = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f'Козерог ♑️'),
            KeyboardButton(text=f'Водолей ♒️')
        ],
        [
            KeyboardButton(text=f'Рыбы ♓️'),
            KeyboardButton(text=f'Овен ♈️')
        ],
        [
            KeyboardButton(text=f'Телец ♉️'),
            KeyboardButton(text=f'Близнецы ♊️')
        ],
        [
            KeyboardButton(text=f'Рак ♋️'),
            KeyboardButton(text=f'Лев ♌️')
        ],
        [
            KeyboardButton(text=f'Дева ♍️'),
            KeyboardButton(text=f'Весы ♎️')
        ],
        [
            KeyboardButton(text=f'Скорпион ♏️'),
            KeyboardButton(text=f'Стрелец ♐️')
        ],
    ],
    resize_keyboard=True
)
