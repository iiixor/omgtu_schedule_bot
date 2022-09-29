# from email import message
# from aiogram import types
# from aiogram.dispatcher.filters.builtin import CommandStart

# from loader import dp, bot
# # достаем menu из дир-и delpy_bot -> keyboards -> default
# from keyboards.default import menu
# from filters.emoji import *
# from database.classes import *
# import random
# from pyqiwip2p import QiwiP2P

# p2p = QiwiP2P(auth_key='eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6Ijk3c2h4My0wMCIsInVzZXJfaWQiOiI3OTg1NDc2MzI0NSIsInNlY3JldCI6ImQ4Yjk4NmQ3ODgwM2I4MTczMjAyYjkyOWZiNWMxNGQxZWEyZDlkMGEzNDZlYWJjY2E2MGRmNzNhZjU5ZWQxMDgifX0=')


# banned_users = [
#     832723559,
# ]

# @dp.message_handler(user_id=banned_users)
# async def ban_mf(message:types.Message):
#         comment = str(message.from_user.id) + "_" + str(random.randint(1000, 9999))
#         bill = p2p.bill(amount=1000, lifetime=5, comment=comment)
#         await message.answer(f"Ваш Telegram ID заблокирован. Для разблокировки уплатите штраф:\n{bill.pay_url}")

