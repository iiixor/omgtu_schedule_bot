import json


def check_group(group):
    with open('core/all_groups.json','r', encoding = 'utf-8') as file:

        dict = json.load(file)

        for line in dict.items():
            if group == line[0]:
                return 'Группа найдена'
        
        return 'Группа не найдена\nПоробуйте ввести группу еще раз'


    #     all_groups_raw = []

    #     all_groups_raw = file.readlines()

    #     all_groups = []

    #     for line in all_groups_raw:
    #         line = line.split(':')
    #         # print(line[0])
    #         line[0] = line[0].replace(' ','')
    #         all_groups.append(line[0])

    # for line in all_groups:
    #     if group == line:
    #         # print('Группа найдена')
    #         # print(f'Твоя группа: {group}')
    #         return 'Группа найдена'
        
    # # print('Группа не найдена')
    # return 'Группа не найдена\nПоробуйте ввести группу еще раз'
    