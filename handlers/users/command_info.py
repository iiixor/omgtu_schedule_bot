from aiogram import types
from loader import dp, bot
import aiogram.utils.markdown as fmt

@dp.message_handler(commands=['info'])
async def information(message: types.Message):
    await message.delete()
    text = [
        'Данный телеграм бот был создан командой <i><u>@Delpy_Bot</u></i>, чтобы любой студент мог с лёгкостью узнать:\n',
        '- Данные преподавателя: "Имя, должность, кабинет, контакты, ссылки"',
        '- Недельное расписание по группам на две учебные недели',    
        '\n\n'
        'P.s есть раздел /support, в котором вы сможете напрямую связаться с разработчиками и предложить свою идею. :)'
    ]
    await message.answer('\n'.join(text))    