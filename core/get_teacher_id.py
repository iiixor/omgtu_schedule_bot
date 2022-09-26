import json

def get_teacher_id(name):
    if '.' in name:
        name = name.replace('.',' ')
        name = name.split()
    
    all_teachers = []


    with open ('core/all_teachers_id.txt','r', encoding = 'utf-8') as file:
        all_teachers = file.readlines()
        for teacher in all_teachers:
            teacher = teacher.replace('\n','')
            teacher_ziped = teacher.split(' : ')
            teacher_ziped = teacher_ziped[0].replace(".",' ')
            teacher_ziped = teacher_ziped.split()

            if type(name) is list:
                if name[0].upper() == teacher_ziped[0].upper():
                    if name[1].upper() in teacher_ziped[1].upper():
                        if name[2].upper() in teacher_ziped[2].upper():
                            teacher = teacher.split(' : ')
                            id = teacher[1]
                            # print(id)
                            return id
            else:
                if name.upper() == teacher_ziped[0].upper():
                    teacher = teacher.split(' : ')
                    id = teacher[1]
                    # print(id)
                    return id
        return f'Преподатель с такой фамилией не найден!\nПопробуйте еще раз'

def get_teacher_id_json(name):
    name = name.upper()
    # if '.' in name:
    #     name = name.replace('.',' ')
    #     name = name.split()
    
    with open(f'core/all_teachers_id.json','r', encoding='utf-8') as file:
        json_dict = json.load(file)
        print(json_dict[name])

get_teacher_id_json('ПАНИН Ю.Н.')

