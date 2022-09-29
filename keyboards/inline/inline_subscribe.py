# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram.utils.callback_data import CallbackData

# from keyboards.inline.callback_datas import *


# ADMIN_LINK = "https://t.me/delpy_manager"

# subscribe_button_yes = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
#         [
#             InlineKeyboardButton(text=f'Выбрать группу',callback_data=subscribe_callback.new(type='group'))
#         ],
#         [
#             InlineKeyboardButton(text=f'Оформить подписку ✅', callback_data=subscribe_callback.new(type='yes'))
#         ],
#         [
#             InlineKeyboardButton(text=f'Написать в поддержку 👨‍🔧', callback_data=media_callback.new(platform='support'), url=ADMIN_LINK)
#         ],
#         [
#             InlineKeyboardButton(text=f'Реферальная ссылка', callback_data=referral_callback.new(ass='user'))
#         ]
#     ]
# )

# subscribe_button_cancel = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
#         [
#            InlineKeyboardButton(text=f'Выбрать группу', callback_data=subscribe_callback.new(type='group'))
#         ],
#         [
#             InlineKeyboardButton(text=f'Написать в поддержку 👨‍🔧', callback_data=media_callback.new(platform='support'), url=ADMIN_LINK)
#         ],
#     ]
# )

# subscribe_button_free_pass = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
#         [
#             InlineKeyboardButton(text=f'Выбрать группу',callback_data=subscribe_callback.new(type='group'))
#         ],
#         [
#             InlineKeyboardButton(text=f'Получить неделю бесплатно ✅', callback_data=subscribe_callback.new(type='free_pass')),
#         ],
#         [
#             InlineKeyboardButton(text=f'Написать в поддержку 👨‍🔧', callback_data=media_callback.new(platform='support'), url=ADMIN_LINK)
#         ],

#     ]
# )

# subscribe_button_sub_variants = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
#         [
#             InlineKeyboardButton(text=f'895 руб. / Год ',callback_data=subscribe_callback.new(type='year'))
#         ],
#         [
#             InlineKeyboardButton(text=f'495 руб. / Пол года', callback_data=subscribe_callback.new(type='half_year')),
#         ],
#         [
#             InlineKeyboardButton(text=f'95 руб. / Месяц', callback_data=subscribe_callback.new(type='month')),
#         ],

#     ]
# )

