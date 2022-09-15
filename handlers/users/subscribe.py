from datetime import datetime
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
from keyboards.inline.inline_subscribe import *
from keyboards.default.pay_status import *
from handlers.users.personal_cabinet import *
from core.check_group import * 
from database.classes import *


from pyqiwip2p import QiwiP2P
import random
import time


database = Database()
database.path = 'database/users.db'
path = database.path

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


@dp.callback_query_handler(subscribe_callback.filter(type='yes'))
async def choice_sub_format(call:CallbackQuery):
    await call.message.answer('Выберете формат подписки:', reply_markup=subscribe_button_sub_variants)


@dp.callback_query_handler(subscribe_callback.filter(type='month'))
async def handle_creation_of_payment(call:CallbackQuery):
    check_bill_id = database.find_value(path, call.from_user.id, 'bill_id')
    if check_bill_id != "Empty":
        await call.message.answer('Вы получили ссылку на оплату в одном из прошлых сообщений. Пожалуйста, нажмите кнопку "Проверить оплату"', reply_markup=i_paid)
    else:
        comment = str(call.from_user.id) + "_" + str(random.randint(1000, 9999))
        bill = p2p.bill(amount=1, lifetime=5, comment=comment)
        database.change_value(path, call.from_user.id, 'bill_id', bill.bill_id)
        await call.message.answer(text=f'Ваш счёт на оплату\n {bill.pay_url}\n\nСсылка действительна 5 минут, после завершения оплаты нажмите кнопку "Проверить оплату"', reply_markup=i_paid)


@dp.callback_query_handler(subscribe_callback.filter(type='free_pass'))
async def handle_creation_of_payment(call:CallbackQuery):
    today = datetime.date.today()
    Omsk_hour = datetime.timedelta(days=1)
    Omsk_hours = today + Omsk_hour
    Omsk_hours = Omsk_hours.strftime("%Y.%m.%d")
    new_sub_expiration = Omsk_hours
    database.change_value(path, call.from_user.id, 'sub_expiration', new_sub_expiration)
    database.change_value(path, call.from_user.id, 'sub_format', 'Free_pass')
    await call.message.answer(f'Поздравляем, Вам достпупен весь функционал до {new_sub_expiration} 🎉')
    

@dp.message_handler(text="Проверить оплату")
async def handle_successful_payment(message: types.Message):
    # bill: Bill = data.get("bill")
    bill_id = database.find_value(path, message.from_user.id, 'bill_id')
    print(str(p2p.check(bill_id = bill_id).status))
    if str(p2p.check(bill_id = bill_id).status) == "PAID":
        today = datetime.date.today()
        Omsk_hour = datetime.timedelta(days=31)
        Omsk_hours = today + Omsk_hour
        Omsk_hours = Omsk_hours.strftime("%Y.%m.%d")
        new_sub_expiration = Omsk_hours
        await message.answer("Оплата прошла")
        await message.answer(f'Поздравляем, Вам достпупен весь функционал до {new_sub_expiration} 🎉')
        database.change_value(path, message.from_user.id, 'sub_expiration', new_sub_expiration)
        database.change_value(path, message.from_user.id, 'sub_format', 'Full')
        database.change_value(path, message.from_user.id, 'bill_id', 'Empty')
    elif str(p2p.check(bill_id = bill_id).status) == "WAITING" :
        await message.answer("Оплата не прошла\n<i>Попробуйте еще раз</i>")
    else:
        database.change_value(path, message.from_user.id, 'bill_id', 'Empty')
        await message.answer("Оплата не прошла\n<i>Попробуйте сформировать новую ссылку</i>")

        
@dp.message_handler(text = f'Отмена')
async def cancel(message:types.Message):
    database.change_value(path, message.from_user.id, 'bill_id', 'Empty')
    await message.answer('Вы отменили оплату.<i>Старая ссылка не действительна</i>')