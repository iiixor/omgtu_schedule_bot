from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from loader import dp, bot

from keyboards.inline.callback_datas import *

map_pg1 = InlineKeyboardMarkup(row_width=3, inline_keyboard=[

        [
        InlineKeyboardButton(text = f'Главный корпус', callback_data=map_callback.new(type='Main')),
        InlineKeyboardButton(text = f'УЛК-1', callback_data=map_callback.new(type='ulk-1')),
        InlineKeyboardButton(text = f'УЛК-2', callback_data=map_callback.new(type='ulk-2')),
        ],
        [
        InlineKeyboardButton(text = f'УЛК-3', callback_data=map_callback.new(type='ulk-3')),
        InlineKeyboardButton(text = f'УЛК-4', callback_data=map_callback.new(type='ulk-4')),
        InlineKeyboardButton(text = f'УЛК-5', callback_data=map_callback.new(type='ulk-5')),
        ],
        [
        InlineKeyboardButton(text = f'УЛК-6', callback_data=map_callback.new(type='ulk-6')),
        InlineKeyboardButton(text = f'УЛК-7', callback_data=map_callback.new(type='ulk-7')),
        InlineKeyboardButton(text = f'УЛК-8', callback_data=map_callback.new(type='ulk-8')),
        ],
        [
        InlineKeyboardButton("• 1 •", callback_data=page_switcher_callback.new(number='1')),
        InlineKeyboardButton("• 2 •", callback_data=page_switcher_callback.new(number='2')),
        InlineKeyboardButton("• 3 •", callback_data=page_switcher_callback.new(number='3'))
        ]
    ]
)

map_pg2 = InlineKeyboardMarkup(row_width=3, inline_keyboard=[
    
    
        [
        InlineKeyboardButton(text = f'УЛК-9', callback_data=map_callback.new(type='ulk-9')),
        InlineKeyboardButton(text = f'УЛК-10', callback_data=map_callback.new(type='ulk-10')),
        InlineKeyboardButton(text = f'УЛК-11', callback_data=map_callback.new(type='ulk-11')),
        ],
        [
        InlineKeyboardButton(text = f'УЛК-12', callback_data=map_callback.new(type='ulk-12')),
        InlineKeyboardButton(text = f'УЛК-13', callback_data=map_callback.new(type='ulk-13')),
        InlineKeyboardButton(text = f'УЛК-14', callback_data=map_callback.new(type='ulk-14')),
        ],
        [
        InlineKeyboardButton(text = f'УПМ', callback_data=map_callback.new(type='UPM')),
        InlineKeyboardButton(text = f'ФИЗ корпус', callback_data=map_callback.new(type='FIZ')),
        InlineKeyboardButton(text = f'Медиацентр, столовая', callback_data=map_callback.new(type='MEDST')),
        ],
        [
        InlineKeyboardButton("• 1 •", callback_data=page_switcher_callback.new(number='1')),
        InlineKeyboardButton("• 2 •", callback_data=page_switcher_callback.new(number='2')),
        InlineKeyboardButton("• 3 •", callback_data=page_switcher_callback.new(number='3'))
        ]   
    ]   
)

map_pg3 = InlineKeyboardMarkup(row_width=3, inline_keyboard=[
    
    
        [
        InlineKeyboardButton(text = f'Бассейн', callback_data=map_callback.new(type='BAS')),
        InlineKeyboardButton(text = f'ВУК-1(Тир)', callback_data=map_callback.new(type='vuk-1')),
        InlineKeyboardButton(text = f'ВУК-2(Общага-N1)', callback_data=map_callback.new(type='vuk-2')),
        ],
        [
        InlineKeyboardButton(text = f'ВУК-3(Склад)', callback_data=map_callback.new(type='vuk-3')),
        InlineKeyboardButton(text = f'ВУК-4(Танки)', callback_data=map_callback.new(type='vuk-4')),
        InlineKeyboardButton(text = f'ВУК-5', callback_data=map_callback.new(type='vuk-5')),
        ],
        [
        InlineKeyboardButton(text = f'ВУК-6', callback_data=map_callback.new(type='vuk-6')),
        InlineKeyboardButton(text = f'ВУК-7(Гараж)', callback_data=map_callback.new(type='vuk-7')),
        ],
        [
        InlineKeyboardButton("• 1 •", callback_data=page_switcher_callback.new(number='1')),
        InlineKeyboardButton("• 2 •", callback_data=page_switcher_callback.new(number='2')),
        InlineKeyboardButton("• 3 •", callback_data=page_switcher_callback.new(number='3'))
        ]   
    ]   
)

# map_pg3 = InlineKeyboardMarkup(row_width=3, inline_keyboard=[
#     InlineKeyboardButton(text = f'Главный корпус 3', callback_data=map_callback.new(type='Main')),
#     InlineKeyboardButton(text = f'Главный корпус 3', callback_data=map_callback.new(type='Main')),
#     InlineKeyboardButton(text = f'Главный корпус 3', callback_data=map_callback.new(type='Main')),
#     InlineKeyboardButton(text = f'Главный корпус 3', callback_data=map_callback.new(type='Main')),
#     InlineKeyboardButton(text = f'Главный корпус 3', callback_data=map_callback.new(type='Main')),
#     InlineKeyboardButton(text = f'Главный корпус 3', callback_data=map_callback.new(type='Main')),
#     InlineKeyboardButton(text = f'Главный корпус 3', callback_data=map_callback.new(type='Main')),
#     InlineKeyboardButton(text = f'Главный корпус 3', callback_data=map_callback.new(type='Main')),
#     InlineKeyboardButton(text = f'Главный корпус 3', callback_data=map_callback.new(type='Main')),
# ])