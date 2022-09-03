from aiogram import types
from loader import dp


# ловит в хендлер в фото
# @dp.message_handler(content_types = types.ContentTypes.PHOTO)

@dp.message_handler()
async def unknown_msg(message: types.Message):
    await message.answer(f'К сожалению, я не знаю такой команды')

    # оформить, как ответ на конретное сообщение
    # await message.reply(f'Cам ты {message.text}')
