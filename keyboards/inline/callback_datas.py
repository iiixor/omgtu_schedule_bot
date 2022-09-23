from aiogram.utils.callback_data import CallbackData


# тут пишем так называемые тригеры для кнопок
# в 1м параметре CallbackData предаетсям тип кнопки, а затем один из парметров типа

switch_callback = CallbackData("switcher", "language")

media_callback = CallbackData("media", "platform")

poll_callback = CallbackData("poll", "platform")

review_callback = CallbackData("review", "platform")

choice_callback = CallbackData("choice", "type")

skills_callback = CallbackData('skill', 'type')

subscribe_callback = CallbackData('subscribe','type')

raspisanie_callback = CallbackData('days', 'pn')

raspisanie_callback_2 = CallbackData('days', 'pn')

map_callback = CallbackData('map', 'type')

prepod_callback = CallbackData('r', 'fio')

page_switcher_callback = CallbackData('page', 'number')

referral_callback = CallbackData('pers', 'ref')






