from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from filters.emoji import *
# создаем кнопки
# в keyboard находится двумерный массив
# в прицнипе как матрицой можно задавать ряды строки кнопкам
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f'Получить данные о преподавателе')
        ],
        [
            KeyboardButton(text=f'Личный кабинет')
        ],
        [
            KeyboardButton(text=f'Выбор дня')
        ],
        [
            KeyboardButton(text=f'Обратная связь')
        ],
        [
            KeyboardButton(text=f'Карта университета')
        ]
        # [
            # KeyboardButton(text=f'Поменять язык {emoji_ruflag}'),
            # KeyboardButton(text=f'Пройти опрос {emoji_paper_pen}'),
            # KeyboardButton(text=f'Прайс {emoji_abacus}')
        # ],
        # [
        #     KeyboardButton(text=f'Отзывы {emoji_star}'),
        #     KeyboardButton(text=f'Прайс {emoji_abacus}')
        # ],
    ],
    # делаем нормальный размер клавиатуры
    resize_keyboard=True
)

personal_cabinet_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f'Оформить подписку')
        ],
        [
            KeyboardButton(text=f'Назад')
        ]
        # [
            # KeyboardButton(text=f'Поменять язык {emoji_ruflag}'),
            # KeyboardButton(text=f'Пройти опрос {emoji_paper_pen}'),
            # KeyboardButton(text=f'Прайс {emoji_abacus}')
        # ],
        # [
        #     KeyboardButton(text=f'Отзывы {emoji_star}'),
        #     KeyboardButton(text=f'Прайс {emoji_abacus}')
        # ],
    ],
    # делаем нормальный размер клавиатуры
    resize_keyboard=True
)
