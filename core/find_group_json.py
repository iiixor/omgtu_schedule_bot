import json
def find_group_json(date,group):
    with open (f'jsons/{date}_*{group}*.json') as file:
        json_dict = json.load(file)

        for i in json_dict:
            group = i['group']
            discipline = i['discipline']
            auditorium = i['auditorium']
            lecturer_title = i['lecturer_title']
            beginLesson = i['beginLesson']
            endLesson = i['endLesson']
            text = [group,discipline, auditorium, lecturer_title, beginLesson, endLesson]
            print('\n'.join(text))


find_group_json("2022.09.21","НД-191")