import json

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

def find_group(group, date):
    from find_teacher import find_teacher
    import requests
    import fake_useragent
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


    with open('all_groups.txt', 'r') as file:
        all_groups = file.readlines()
    for line in all_groups:
        line = line.replace('\n','')
        if group.upper() in line:
            line = line.split(' : ')
            link = f"https://rasp.omgtu.ru/api/schedule/group/{line[1]}?start={date}&finish={date}&lng=2"
            print(link)
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
                        discipline_dict['lecturer_title'].append(lecturer_title)
                        continue

                if '"subGroup"' in line_2:
                    subGroup = line_2.replace('"subGroup"','')
                    subGroup = subGroup.replace('"','')
                    subGroup = subGroup.replace(':','',1)
                    subGroup = subGroup.replace('{','')
                    subGroup = subGroup.replace('[','')
                    subGroup = subGroup.replace('\\/','/')
                    if 'null' in subGroup:
                        subGroup = group
                    discipline_dict['subGroup'].append(subGroup)
                    continue




    for line in discipline_dict.items():
        print(line)

find_group('ПИ-202',"2022.09.02")
