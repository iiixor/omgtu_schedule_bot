from email import message
from aiogram import types
from loader import dp, bot
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import *
from filters.emoji import *
from parsing_data.parsing_main import *
from keyboards.default.menu import *
from keyboards.inline import inline_subscribe 

from glQiwiApi import QiwiWrapper
from glQiwiApi import QiwiP2PClient
from aiogram.dispatcher import FSMContext
from glQiwiApi.qiwi.clients.p2p.types import Bill

qiwi_p2p_client = QiwiP2PClient(secret_p2p='eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6Ijk3c2h4My0wMCIsInVzZXJfaWQiOiI3OTg1NDc2MzI0NSIsInNlY3JldCI6ImQ4Yjk4NmQ3ODgwM2I4MTczMjAyYjkyOWZiNWMxNGQxZWEyZDlkMGEzNDZlYWJjY2E2MGRmNzNhZjU5ZWQxMDgifX0=')

@dp.callback_query_handler(subscribe_callback.filter(type='yes'))
async def handle_creation_of_payment(call:CallbackQuery,state: FSMContext):
    async with qiwi_p2p_client:
        bill = await qiwi_p2p_client.create_p2p_bill(amount=50)
    await call.message.answer(text=f"Ваш счёт на оплату\n {bill.pay_url}")
    await state.set_state("payment")
    await state.update_data(bill=bill)

@dp.message_handler(state="payment", text="I paid")
async def handle_successful_payment(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        bill: Bill = data.get("bill")











# @dp.callback_query_handler(subscribe_callback.filter(type='cancel'))
# async def bot_get_russian(call: CallbackQuery):
#     allert_text = f'# ДОБАВИТЬ ПЛАТЕЖКУ'
#     await call.answer(allert_text, show_alert=False)
