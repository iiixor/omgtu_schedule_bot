from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f'Магазин'),
            KeyboardButton(text=f'Личный кабинет')
        ],
        [
            KeyboardButton(text=f'Настройки')
        ],
    ],
    # делаем нормальный размер клавиатуры
    resize_keyboard=True
)

