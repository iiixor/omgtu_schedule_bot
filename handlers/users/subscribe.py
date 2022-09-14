from datetime import datetime
from email import message
from selectors import EpollSelector
from aiogram import types
from loader import dp, bot
from aiogram.types import CallbackQuery
import random
import time
import datetime


from keyboards.inline.callback_datas import *
from filters.emoji import *
from parsing_data.parsing_main import *
from keyboards.default.menu import *
from keyboards.inline import inline_subscribe 
from keyboards.default.pay_status import *
from handlers.users.personal_cabinet import *
from core.check_group import * 
from database.classes import *


from glQiwiApi import QiwiWrapper
from glQiwiApi import QiwiP2PClient
from aiogram.dispatcher import FSMContext
from glQiwiApi.qiwi.clients.p2p.types import Bill
from pyqiwip2p import QiwiP2P
from pyqiwip2p.p2p_types import QiwiCustomer, QiwiDatetime, PaymentMethods #можно удалить
import random
import time


database = Database()
database.path = 'database/users.db'
path = database.path

# qiwi_p2p_client = QiwiP2PClient(secret_p2p='eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6Ijk3c2h4My0wMCIsInVzZXJfaWQiOiI3OTg1NDc2MzI0NSIsInNlY3JldCI6ImQ4Yjk4NmQ3ODgwM2I4MTczMjAyYjkyOWZiNWMxNGQxZWEyZDlkMGEzNDZlYWJjY2E2MGRmNzNhZjU5ZWQxMDgifX0=')
p2p = QiwiP2P(auth_key='eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6Ijk3c2h4My0wMCIsInVzZXJfaWQiOiI3OTg1NDc2MzI0NSIsInNlY3JldCI6ImQ4Yjk4NmQ3ODgwM2I4MTczMjAyYjkyOWZiNWMxNGQxZWEyZDlkMGEzNDZlYWJjY2E2MGRmNzNhZjU5ZWQxMDgifX0=')

def days_to_second(days):
    return days * 24 * 60 * 60

def time_sub_days(sub_expiration):
    time_now = time.time()
    middle_time =  int(sub_expiration) - time_now
    if middle_time <=0:
        return False
    else:
        dt = str(datetime.timedelta(seconds=middle_time))
        dt = dt.split(', ')        
        return dt[0]

# def str_to_date(str_date):
#     return datetime.datetime.strptime(str_date,'%Y.%m.%d').date()

@dp.callback_query_handler(subscribe_callback.filter(type='yes'))
async def handle_creation_of_payment(call:CallbackQuery):
    comment = str(call.from_user.id) + "_" + str(random.randint(1000, 9999))
    bill = p2p.bill(amount=1, lifetime=5, comment=comment)
    database.change_value(path, call.from_user.id, 'bill_id', bill.bill_id)
    await call.message.answer(text=f"Ваш счёт на оплату\n {bill.pay_url}")
    timing = time.time()
    bill_id = database.find_value(path, call.from_user.id, 'bill_id')
    while time.time() - timing < 300:
        print(str(p2p.check(bill_id = bill_id).status))
        print(time.time() - timing)
        time.sleep(5)
        if str(p2p.check(bill_id = bill_id).status) == "PAID":
            database.change_value(path, call.from_user.id, 'sub_format', 'Full')
            today = datetime.date.today()
            Omsk_hour = datetime.timedelta(days=1)
            Omsk_hours = today + Omsk_hour
            Omsk_hours = Omsk_hours.strftime("%Y.%m.%d")
            new_sub_expiration = Omsk_hours
            database.change_value(path, call.from_user.id, 'sub_expiration', new_sub_expiration)
            sub_format = database.find_value(path, call.from_user.id, 'sub_format')
            await call.message.answer("Оплата прошла")
            break
    if time.time() - timing < 120 and str(p2p.check(bill_id = bill_id).status) != "PAID":
        await call.message.answer("Оплата не прошла\n<i>Попробуйте еще раз</i>")

# @dp.message_handler(text="Я оплатил")
# async def handle_successful_payment(message: types.Message):
#     # bill: Bill = data.get("bill")
#     bill_id = database.find_value(path, call.from_user.id, 'bill_id')
#     timi
#     if str(p2p.check(bill_id = bill_id).status) == "PAID":
#         await message.answer("Оплата прошла",reply_markup=subscribe_button_yes)
#         database.change_value(path, message.from_user.id, 'sub_format', 'Full')
#     else:
#         await message.answer("Оплата не прошла\n<i>Попробуйте еще раз</i>")
        

# @dp.message_handler(text = f'Отмена')
# async def cancel(message:types.Message):
#     await message.answer('Вы отменили отменили оплату')

#----------------------------------------------------

# logging.basicConfig(level=logging.INFO)

# bot = Bot(token=cfg.TOKEN)
# dp = Dispatcher(bot)

# database = Database("database")
# p2p = QiwiP2P(auth_key=cfg.QIWI_TOKEN)

# def is_number(_str):
#     try:
#         int(_str)
#         return True
#     except ValueError:
#         return False

# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     text = f'<b>Вселенский</b> приветсвует Вас, {message.from_user.full_name} 👋'
#     await message.answer(text, reply_markup=nav.topUpMenu)
#     if message.chat.type == 'private':
#         if not db.user_exists(message.from_user.id):
#             db.add_user(message.from_user.id)

# # @dp.message_handler(commands=['start'])
# # async def start(message: types.Message):
# #     if message.chat.type == 'private':
# #         if not db.user_exists(message.from_user.id):
# #             db.add_user(message.from_user.id)
# #
# #         await bot.send_message(message.from_user.id, f'Добро пожаловать!\nВаш счет: {db.user_money(message.from_user.id)} руб.', reply_markup=nav.topUpMenu)

# @dp.message_handler()
# async def bot_mess(message: types.Message):
#     if message.chat.type == 'private':
#         if is_number(message.text):
#             message_money = int(message.text)
#             if message_money >= 1:
#                 comment = str(message.from_user.id) + "_" + str(random.randint(1000, 9999))
#                 bill = p2p.bill(amount=1, lifetime=15, comment=comment)

#                 db.add_check(message.from_user.id, message_money, bill.bill.id)

#                 await bot.send_message(message.from_user.id, f"Вам нужно отправить {message_money} руб. на наш счет QIWI\nСсылку: {bill.pay_url}\nУказав комментарий к оплате: {comment}", reply_markup=nav.buy_menu(url=bill.pay_url, bill=bill.bill_id))

#             else:
#                 await bot.send_message(message.from_user.id, "Минимальная сумма для пополнения 5 руб.")
#         else:
#             await bot.send_message(message.from_user.id, "Введите целое число")


# @dp.callback_query_handler(text="top_up")
# async def top_up(callback: types.CallbackQuery):
#     await bot.delete_message(callback.from_user.id, callback.message.message_id)
#     await bot.send_message(callback.from_user.id, "Введите сумму для пополнения!")


# @dp.callback_query_handler(text_contains="check_")
# async def check(callback: types.CallbackQuery):
#     bill = str(callback.data[6:])
#     info = db.get_check(bill)
#     if info != False:
#         if str(p2p.check(bill_id=bill).status) == "PAID":
#             user_money = db.user_money(callback.from_user.id)
#             money = int(info[2])
#             db.set_money(callback.from_user.id, user_money+money)
#             await bot.send_message(callback.from_user.id, "Ваш счет пополнен! Напишите /start")
#             await bot.delete_message(callback.from_user_id, callback.message.message_id)
#         else:
#             await bot.send_message(callback.from_user.id, "Вы не оплатили счет!", reply_markup=nav.buy_menu(False, bill=bill))
#     else:
#         await bot.send_message(callback.from_user.id, "Счет не найден")


# if name == "main":
#     executor.start_polling(dp)

# def buy_menu(isUrl=True, url="", bill=""):
#     qiwiMenu = InlineKeyboardMarkup(row_width=1)
#     if isUrl:
#         btnUrlQIWI = InlineKeyboardButton(text="Ссылка на оплату", url=url)
#         qiwiMenu.insert(btnUrlQIWI)

#     btnCheckQIWI = InlineKeyboardButton(text="Проверить оплату", callback_data="check_"+bill)
#     qiwiMenu.insert(btnCheckQIWI)
#     return qiwiMenu