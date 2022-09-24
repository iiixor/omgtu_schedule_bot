import json
from core.find_teacher import *

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

def get_id_from_json(group):
    with open(f'all_groups.json','r',encoding="utf-8") as file:
        dic = json.load(file)
        return dic[group]

def find_group_json(date,group):
    from core.find_teacher import find_teacher
    group_id = get_id_from_json(group)

    with open (f'jsons/{date}_№{group_id}.json') as file:
        json_dict = json.load(file)

        # print(json_dict)

        for dic in json_dict:
            
            # group = dic['group']
            discipline = dic['discipline']
            auditorium = dic['auditorium']
            lecturer_title = dic['lecturer_title']
            lecturer_title = find_teacher(lecturer_title)
            if lecturer_title == f'Преподатель с такой фамилией не найден!\nПопробуйте еще раз!':
                lecturer_title = f'Неизвестно'
         
            beginLesson = dic['beginLesson']
            endLesson = dic['endLesson']
        
            text = [discipline, auditorium, lecturer_title, beginLesson, endLesson,'']
            print('\n'.join(text))
    

# get_id_from_json('НД-191')
# add_id_for_dp()
find_group_json("2022.09.13","НД-191")