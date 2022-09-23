from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand('menu', 'Перейти в главное меню'),
        types.BotCommand('info', 'Получить информацию о боте'),
        types.BotCommand('contacs', 'Получить контакты учебных организаций'),
        ])
