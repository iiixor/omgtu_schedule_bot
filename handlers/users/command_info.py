from aiogram import types
from loader import dp, bot
import aiogram.utils.markdown as fmt

@dp.message_handler(commands=['info'])
async def information(message: types.Message):
    await message.delete()
    text = [
        'Данный телеграм бот был создан командой @Delpy_Bot, чтобы любой студент мог с лёгкостью узнать:\n',
        '- Расписание преподавателя',
        '- Расписание выбранный группы',
        '- Карту вуза по геолокации'    
        '\n\n'
        'P.S Через личный кабинет Вы сможете напрямую связаться с разработчиками и предложить им свою идею :)'
    ]
    await message.answer('\n'.join(text))