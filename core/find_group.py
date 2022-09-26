import json
from core.find_teacher import *
import datetime


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

def even_odd():
    date = datetime.datetime.now().replace(second=0, microsecond=0)
    date = date + datetime.timedelta(hours=3)
    wk = date.isocalendar()[1]
    if (wk % 2 == 0):
        return "Нижняя неделя"
    else:
        return "Верхняя неделя"

def find_group(group, date, choice):
    import requests
    from bs4 import BeautifulSoup

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
    sub_group = ''

    if '/' in group:
        sub_group = group
        group = group.split('/')
        group = group[0]
        # print(group)
        # print(sub_group)
    with open('core/all_groups.txt','r', encoding='utf-8') as file:
        all_groups = file.readlines()
    for line in all_groups:
        line = line.replace('\n','')
        if group.upper() in line:
            line = line.split(' : ')
            link = f"https://rasp.omgtu.ru/api/schedule/group/{line[1]}?start={date}&finish={date}&lng=2"
            responce = requests.get(link).text
            soup = BeautifulSoup(responce, 'lxml')
            for line_2 in responce.split(','):
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
                    if kindOfWork == "Практические занятия":
                        kindOfWork = 'Практика'
                    if kindOfWork == "Лабораторные работы":
                        kindOfWork = 'Лабы'
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
                        # print(lecturer_title)
                        lecturer_title = find_teacher(lecturer_title)
                        if lecturer_title == f'Преподатель с такой фамилией не найден!\nПопробуйте еще раз!':
                            lecturer_title = f'Неизвестно'
                        discipline_dict['lecturer_title'].append(lecturer_title)
                        continue

                if '"subGroup"' in line_2:
                    subGroup = line_2.replace('"subGroup"','')
                    subGroup = subGroup.replace('"','')
                    subGroup = subGroup.replace(':','',1)
                    subGroup = subGroup.replace('{','')
                    subGroup = subGroup.replace('[','')
                    subGroup = subGroup.replace('\\/','/')
                    if sub_group != '':
                        if 'null' in subGroup:
                            subGroup = group
                            discipline_dict['subGroup'].append(subGroup)
                            continue
                        if sub_group in subGroup:
                            discipline_dict['subGroup'].append(subGroup)
                            continue
                        else:
                            discipline_dict['lecturer_title'].remove(lecturer_title)
                            discipline_dict['kindOfWork'].remove(kindOfWork)
                            discipline_dict['disciplines'].remove(discipline)
                            discipline_dict['count_lessons'].remove(count_lessons)
                            discipline_dict['beginLesson'].remove(beginLesson)
                            discipline_dict['endLesson'].remove(endLesson)
                            discipline_dict['dayOfWeekString'].remove(dayOfWeekString)
                            discipline_dict['building'].remove(building)
                            discipline_dict['auditorium'].remove(auditorium)
                    else:
                        if 'null' in subGroup:
                            subGroup = group
                        discipline_dict['subGroup'].append(subGroup)
                        continue

                    # discipline_dict['subGroup'].append(subGroup)
                    # continue
            break



    # print(discipline_dict['subGroup'])
    # for line in discipline_dict['subGroup']:
    #     if sub_group == line or group == line:
    #         print(line)
    #
    if len(discipline_dict['disciplines']) == 0:
        print(' Пар нет ')
        return ' Пар нет '

    rez = ''


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
            # print(discipline_dict['disciplines'][i])
            lecturer_title = discipline_dict['lecturer_title'][i]
            building = discipline_dict['building'][i]
            auditorium = discipline_dict['auditorium'][i]
            if lecturer_title != f'Неизвестно':
                lecturer_title = lecturer_title.split()
                lecturer_title = f'{lecturer_title[1]} {lecturer_title[2]} {lecturer_title[3]}'
        else:
            lecturer_title = 'Недоступно'
            building = 'Недоступно'
            auditorium = 'Недоступно'


        text = [
        f'{count_lessons}. {disciplines} ({kindOfWork})',
        f'{beginLesson} - {endLesson}',
        f'{lecturer_title}',
        f'{building} ---> {auditorium}',
        f'\n'
        ]
        # rez = ''
        rez = rez +'\n'.join(text)
        # return rez
        # print('\n'.join(text))
        # print()

    return f'Группа: <code>{group}</code>\n\n{rez}Сейчас идет: <i>{even_odd()}</i>'    # print(rez)


# find_group(2022.09'ПИ-202/2',".05", True)
