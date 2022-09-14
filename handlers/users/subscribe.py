from email import message
from aiogram import types
from loader import dp, bot
from aiogram.types import CallbackQuery

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

database = Database()
database.path = 'database/users.db'
path = database.path

qiwi_p2p_client = QiwiP2PClient(secret_p2p='eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6Ijk3c2h4My0wMCIsInVzZXJfaWQiOiI3OTg1NDc2MzI0NSIsInNlY3JldCI6ImQ4Yjk4NmQ3ODgwM2I4MTczMjAyYjkyOWZiNWMxNGQxZWEyZDlkMGEzNDZlYWJjY2E2MGRmNzNhZjU5ZWQxMDgifX0=')

@dp.callback_query_handler(subscribe_callback.filter(type='yes'))
async def handle_creation_of_payment(call:CallbackQuery):
    async with qiwi_p2p_client:
        bill = await qiwi_p2p_client.create_p2p_bill(amount=1)
    await call.message.answer(text=f"Ваш счёт на оплату\n {bill.pay_url}", reply_markup=i_paid)


@dp.message_handler(state="payment", text="Я оплатил")
async def handle_successful_payment(message: types.Message):
    bill: Bill = data.get("bill")
    if await qiwi_p2p_client.check_if_bill_was_paid(bill):
        await message.answer("Оплата прошла")
        database.change_value(path, message.from_user.id, 'sub_format', 'Full')
    else:
        await message.answer("Оплата не прошла")
        

@dp.message_handler(text = f'Отмена')
async def cancel(message:types.Message):
    # database.change_value(path, message.from_user.id, 'sub_format', 'Free')
    await message.answer('Вы отменили отменили оплату')
    # await state.reset_state()
    # await state.finish()




    
    
    # succesfull_payment = False
    # while succesfull_payment == False:
    #     if await qiwi_p2p_client.check_if_bill_was_paid(bill):
    #         succesfull_payment = True
    #         await message.answer("Оплата прошла")
    #     else:
    #         await message.answer("Оплата не прошла")
    # await state.finish()
    
    
    
    # if await qiwi_p2p_client.check_if_bill_was_paid(bill):
    #     await message.answer("Оплата прошла")
    #     await state.finish()
    # else:
    #     await message.answer("Оплата не прошла")
    #     await state.finish()

# @dp.message_handler(text=f"Личный кабинет")
# async def bot_data_request(message: types.Message):
#     user_id = message.from_user.id
#     sub_format = database.find_value(path, message.from_user.id, 'sub_format')
#     group = database.find_value(path, user_id, 'user_group')
#     # print(group)

#     subscribe_format=''
#     if sub_format == 'Full':
#         subscribe_format='Полный ✅'
#     else:
#         subscribe_format='Бесплатный ❌'

#     if subscribe_format == 'Бесплатный ❌':
#         text = [
#         f'<b>Ваше имя:</b> {message.from_user.full_name}',
#         f'<b>Ваш ID:</b> {message.from_user.id}',
#         f'Группы: <code>{group}</code>',
#         f'<b>Формат подписки</b>: {subscribe_format}',
#         ]
#         markup = subscribe_button_yes
#     else:
#         sub_expiration = database.find_value(path, user_id, 'sub_expiration')
#         text = [
#         f'<b>Ваше имя:</b> {message.from_user.full_name}',
#         f'<b>Ваш ID:</b> {message.from_user.id}',
#         f'Группы: <code>{group}</code>',
#         f'<b>Формат подписки</b>: {subscribe_format}',
#         f'<b>Подписка истекает:</b> {sub_expiration}',
#         ]
#         markup = subscribe_button_cancel
#     await message.answer("\n".join(text), reply_markup=markup)











# @dp.callback_query_handler(subscribe_callback.filter(type='cancel'))
# async def bot_get_russian(call: CallbackQuery):
#     allert_text = f'# ДОБАВИТЬ ПЛАТЕЖКУ'
#     await call.answer(allert_text, show_alert=False)
