def find_teacher(name):
    import requests
    import fake_useragent
    from bs4 import BeautifulSoup

    if '.' in name:
        name = name.replace('.',' ')
        name = name.split()

    with open('core/all_teachers.txt', 'r', encoding = 'utf-8') as file:
        all_groups = file.readlines()
    for line in all_groups:
        line = line.replace('\n','')
        line_ziped = line.split(' : ')
        line_ziped = line_ziped[0].split()
        if type(name) is list:
            if name[0].upper() == line_ziped[0].upper():
                if name[1].upper() in line_ziped[1].upper():
                    if name[2].upper() in line_ziped[2].upper():
                        line = line.split(' : ')
                        text = [
                        '\n'
                        f'  Имя: {line[0]}',
                        f'  Ссылка: {line[1]}'
                        ]
                        text = '\n'.join(text)
                        # print(text)
                        return text
        else:
            if name.upper() == line_ziped[0].upper():
                line = line.split(' : ')
                text = [
                '\n',
                f'  Имя: {line[0]}',
                f'  Ссылка: {line[1]}'
                ]
                text = '\n'.join(text)
                # print(text)
                return text
    return f'Преподатель с такой фамилией не найден!\nПопробуйте еще раз!'


def format_dayofweek(str):
    days = {
    "Mon":"Пн",
    'Fri':'Пт',
    'Sat':"Сб",
    'Sun':'Вс',
    "Tue":'Вт',
    "Wed":"Ср",
    "Thu":'Чт'
    }
    return days[str]


def get_teacher_schedule(name, date, choice):
    import requests
    import fake_useragent
    from bs4 import BeautifulSoup

    from core.get_teacher_id import get_teacher_id

    discipline_dict = {}
    discipline_dict.setdefault('disciplines',[])
    discipline_dict.setdefault('beginLesson',[])
    discipline_dict.setdefault('endLesson',[])
    discipline_dict.setdefault('lecturer_title',[])
    discipline_dict.setdefault('count_lessons',[])
    discipline_dict.setdefault('dayOfWeekString',[])
    discipline_dict.setdefault('building',[])
    discipline_dict.setdefault('auditorium',[])
    discipline_dict.setdefault('kindOfWork',[])
    discipline_dict.setdefault('kindOfWork',[])
    discipline_dict.setdefault('subGroup',[])

    count_teacher = 0
    count_lessons = 0

    id = get_teacher_id(name)
    link = f"https://rasp.omgtu.ru/api/schedule/person/{id}?start={date}&finish={date}&lng=2"
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    responce = responce.split(',')

    for line_2 in responce:
        if '"discipline"' in line_2:
            count_lessons+=1
            discipline = line_2.replace('"discipline"','')
            discipline = discipline.replace('"','')
            discipline = discipline.replace(':','')
            discipline_dict['disciplines'].append(discipline)
            discipline_dict['count_lessons'].append(count_lessons)
            continue

        if '"beginLesson"' in line_2:
            beginLesson = line_2.replace('"beginLesson"','')
            beginLesson = beginLesson.replace('"','')
            beginLesson = beginLesson.replace(':','',1)
            discipline_dict['beginLesson'].append(beginLesson)
            continue

        if '"endLesson"' in line_2:
            endLesson = line_2.replace('"endLesson"','')
            endLesson = endLesson.replace('"','')
            endLesson = endLesson.replace(':','',1)
            discipline_dict['endLesson'].append(endLesson)
            continue

        if '"dayOfWeekString"' in line_2:
            dayOfWeekString = line_2.replace('"dayOfWeekString"','')
            dayOfWeekString = dayOfWeekString.replace('"','')
            dayOfWeekString = dayOfWeekString.replace(':','',1)
            dayOfWeekString = format_dayofweek(dayOfWeekString)
            discipline_dict['dayOfWeekString'].append(dayOfWeekString)
            continue

        if '"building"' in line_2:
            building = line_2.replace('"building"','')
            building = building.replace('"','')
            building = building.replace(':','',1)
            discipline_dict['building'].append(building)
            continue

        if '"auditorium"' in line_2:
            auditorium = line_2.replace('"auditorium"','')
            auditorium = auditorium.replace('"','')
            auditorium = auditorium.replace(':','',1)
            auditorium = auditorium.replace('{','')
            auditorium = auditorium.replace('[','')
            discipline_dict['auditorium'].append(auditorium)
            continue

        if '"kindOfWork"' in line_2:
            kindOfWork = line_2.replace('"kindOfWork"','')
            kindOfWork = kindOfWork.replace('"','')
            kindOfWork = kindOfWork.replace(':','',1)
            kindOfWork = kindOfWork.replace('{','')
            kindOfWork = kindOfWork.replace('[','')
            discipline_dict['kindOfWork'].append(kindOfWork)
            continue

        if '"lecturer_title"' in line_2:
            count_teacher+=1
            if count_teacher%2 == 0:
                lecturer_title = line_2.replace('"lecturer_title"','')
                lecturer_title = lecturer_title.replace('"','')
                lecturer_title = lecturer_title.replace(':','')
                lecturer_title = lecturer_title.replace(']','')
                lecturer_title = lecturer_title.replace('}','')
                lecturer_title = find_teacher(lecturer_title)
                discipline_dict['lecturer_title'].append(lecturer_title)
                continue


    if len(discipline_dict['disciplines']) == 0:
        #print('<b>Пар нет</b>')
        return 'Пар нет'

    for i in range(len(discipline_dict['disciplines'])):

        disciplines = discipline_dict['disciplines'][i]
        kindOfWork = discipline_dict['kindOfWork'][i]
        beginLesson = discipline_dict['beginLesson'][i]
        endLesson = discipline_dict['endLesson'][i]

        if '08:00' in beginLesson:
            count_lessons = '1'
        if '09:40' in beginLesson:
            count_lessons = '2'
        if '11:35' in beginLesson:
            count_lessons = '3'
        if '13:15' in beginLesson:
            count_lessons = '4'

        if choice:
            lecturer_title = discipline_dict['lecturer_title'][i]
            building = discipline_dict['building'][i]
            auditorium = discipline_dict['auditorium'][i]
        else:
            lecturer_title = 'Недосутпно в беслатной версии'
            building = 'Недосутпно в беслатной версии'
            auditorium = 'Недосутпно в беслатной версии'


        text = [
        f'Предмет</b>: {count_lessons}я пара ({kindOfWork}) {disciplines}',
        f'Время занятия</b>: {beginLesson} - {endLesson}',
        f'Преподатель</b>: {lecturer_title}',
        f'Корпус</b>: {building}',
        f'Аудитория:</b> {auditorium}',


        ]

        # print('\n'.join(text))
        # print()
        return text




#find_group('ПИ-202/2',"2022.09.05", False)
get_teacher_schedule('Панин','2022.09.05', True)
