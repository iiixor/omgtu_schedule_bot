from itertools import count
import json
import datetime

# import find_teacher
# from find_teacher import find_teacher

# from database import classes


# with open (f'all_teachers_id.txt') as file:
#     lines = file.readlines()
#     i = 0
#     groups_info = dict()
#     for line in lines:

#         line = line.replace("\n",'')
#         line = line.split(" : ")
#         groups_info[str(line[0])] = str(line[1])

# with open(f'all_teachers_id.json','w',encoding="utf-8") as file:
#     json.dump(groups_info, file,ensure_ascii=False)
# 
# for line in groups_info.items():
#     print(line)
def even_odd():
    date = datetime.datetime.now().replace(second=0, microsecond=0)
    date = date + datetime.timedelta(hours=3)
    wk = date.isocalendar()[1]
    if (wk % 2 == 0):
        return "Нижняя неделя"
    else:
        return "Верхняя неделя"


def get_id_from_json(group):
    with open(f'core/all_groups.json','r',encoding="utf-8") as file:
        dic = json.load(file)
        # print(dic[group])
        return dic[group]

def find_group_json(date,group, boolean):
    if group == 'None':
        return "<i>Выберете группу в личном кабинете</i>"
    # import find_teacher
    from core.find_teacher import find_teacher

    group_id = get_id_from_json(group)

    with open (f'core/jsons/file_{date}_№{group_id}.json', encoding = 'utf-8') as file:

        json_dict = json.load(file)
        if json_dict == []:
            rez = 'Пар нет'
            return f'Группа: <code>{group}</code>\n\n{rez}\n\nСейчас идет: <i>{even_odd()}</i>'

        # print(json_dict)
        rez = ''
        for dic in json_dict:
            
            # group = dic['group']
            discipline = dic['discipline']
            auditorium = dic['auditorium']
            lecturer_title = dic['lecturer_title']
            count_lesson = dic['contentTableOfLessonsName']
            building = dic['building']
            
            kindOfWork = dic['kindOfWork']

            if kindOfWork == "Практические занятия":
                kindOfWork = 'Практика'
            if kindOfWork == "Лабораторные работы":
                kindOfWork = 'Лабы'
            
            lecturer_title = find_teacher(lecturer_title)

            if lecturer_title == f'Преподатель с такой фамилией не найден!\nПопробуйте еще раз!':
                lecturer_title = f'Неизвестно'
            if lecturer_title != f'Неизвестно':
                lecturer_title = lecturer_title.split()
                lecturer_title = f'{lecturer_title[1]} {lecturer_title[2]} {lecturer_title[3]}'
         
            beginLesson = dic['beginLesson']
            endLesson = dic['endLesson']

            if boolean == False:
                lecturer_title = 'Недоступно'
                building = 'Недоступно'
                auditorium = 'Недоступно'
        
            text = [
                f'{count_lesson}. {discipline}({kindOfWork})',
                f'{beginLesson} - {endLesson}',
                f'{lecturer_title}',
                f'{building} ---> {auditorium}',
                f'\n'
            ]
            print('\n'.join(text))
            rez = rez + '\n'.join(text)
        return f'Группа: <code>{group}</code>\n\n{rez}Сейчас идет: <i>{even_odd()}</i>'
    

# get_id_from_json('НД-191')
# add_id_for_dp()

# find_group_json("2022.09.12","НД-191", True)  