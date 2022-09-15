from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f'Найти преподавателя'),
            KeyboardButton(text=f'Карта университета')
        ],
        [
            KeyboardButton(text=f'Расписание')
        ],
        [
            KeyboardButton(text=f'Личный кабинет')
        ],
    ],
    # делаем нормальный размер клавиатуры
    resize_keyboard=True
)

