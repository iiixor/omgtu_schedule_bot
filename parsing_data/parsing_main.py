def get_pifagor(days, months, years):
    import requests
    import fake_useragent
    from bs4 import BeautifulSoup
    # import grequests

    if days[0] == '0':
        days = days[1]

    if months[0] == '0':
        months = months[1]


    # days = input('Введите день?\n')
    # months = input('Введите месяц?\n')
    # years = input('Введите год?\n')

    link = f"https://v-kosmose.com/numerologiya/kvadrat-pifagora/?days={days}&month={months}&years={years}"
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')

    block = soup.find('div', class_ = 'pythagoras-square-table')

    values = block.find_all('td')
    title = soup.find('div', class_ = 'pythagoras-square-title')
    title = title.text

    values_in_tg = []
    values_in_tg.append(f'<b>{title}</b>\n')

    for value in values:

        skill = value.find('b').text
        data = value.text.replace(skill, '')
        # print(f'\n{skill} - {data}')
        values_in_tg.append(f'<b>{skill}</b> - <i>{data}</i>')

    # print('')

    with open("parsing_data/date.txt",'w') as f:
        f.write(f'{days}\n')
        f.write(f'{months}\n')
        f.write(f'{years}\n')



    return values_in_tg

def get_skill_from_parsing(skill_number):
    import requests
    import fake_useragent
    from bs4 import BeautifulSoup

    with open("parsing_data/date.txt",'r') as f:
        days = f.readline()
        months = f.readline()
        years = f.readline()
        
    days = days.replace('\n','')
    days = days.replace(',','')
    months = months.replace('\n','')
    months = months.replace(',','')
    years = years.replace('\n','')
    years = years.replace(',','')


    # print(f'{days},{months},{years}')


    link = f"https://v-kosmose.com/numerologiya/kvadrat-pifagora/?days={days}&month={months}&years={years}"
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')

    # print_skills = input('Хотите получить данные по показателям?[Да/Нет]')

    # print_skills = print_skills.capitalize()
    # print(print_skills)

    # if print_skills.capitalize() == 'Да':

    block_2 = soup.find('div', class_= 'pythagoras-square')

    values_2 = block_2.find_all('p')

    all_skills = {}

    character = values_2[0:5] #Характер
    energy = values_2[5:10] #Энергия
    interest  = values_2[10:11] #Интерес
    health  = values_2[11:12] #Здоровье
    logic = values_2[12:13] #Логика, Интуиция
    labour = values_2[13:14] #Труд
    luck = values_2[14:15] #Удача
    duty = values_2[15:16] #Чувство долга
    memory = values_2[16:17] #Память
    сommitment = values_2[18:21] #Целеустремленность
    family = values_2[21:24] #Семья
    stability = values_2[24:27] #Стабильность
    self_esteem = values_2[27:30] #Самоценка
    material_independence = values_2[30:33] #Материальная независимость
    talant =  values_2[33:41] #Талант
    tempepament = values_2[41:44] #Темеперамент
    spirit = values_2[44:50] #Духовность

    all_skills['1'] = character
    all_skills['2'] = energy
    all_skills['3'] = interest
    all_skills['4'] = health
    all_skills['5'] = logic
    all_skills['6'] = labour
    all_skills['7'] = luck
    all_skills['8'] = duty
    all_skills['9'] = memory
    all_skills['10'] = сommitment
    all_skills['11'] = family
    all_skills['12'] = stability
    all_skills['13'] = self_esteem
    all_skills['14'] = material_independence
    all_skills['15'] = talant
    all_skills['16'] = tempepament
    all_skills['17'] = spirit



    choise = [
    '1 - Характер',
    '2 - Энергия',
    "3 - Интерес",
    "4 - Здоровье",
    "5 - Логика, Интуиация",
    "6 - Труд",
    "7 - Удача",
    "8 - Чувство долга",
    "9 - Память",
    "10 - Целеустрмленность",
    "11 - Семья",
    "12 - Стабильность",
    "13 - Самоценка",
    "14 - Материальная независимость",
    "15 - Талант",
    "16 - Темперамент",
    "17 - Духовность"
    ]

    # print('Выберете показатель:\n')
    # print('\n'.join(choise))

    # choise_done = input('\nВведите цифру:')

    # print('\n')

    # for item in spirit:
    #     print(f'{item.text}\n')

    items_for_tg = []

    for item in all_skills[skill_number]:
        items_for_tg.append(f'{item.text}')

    # for item in all_skills[skill_number]:
    #     print(f'{item.text}\n')



    print(f'{link} \n')

    # print(all_skills[choise_done])

    # print(items_for_tg)

    return items_for_tg