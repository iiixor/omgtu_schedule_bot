def find_teacher(name):
    import requests
    import fake_useragent
    from bs4 import BeautifulSoup

    if '.' in name:
        name = name.replace('.',' ')
        name = name.split()
        # print(name)

    with open('core/all_teachers.txt', 'r') as file:
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
                        f'  <b>Имя</b>: {line[0]}',
                        f'  <b>Ссылка</b>: {line[1]}'
                        ]
                        text = '\n'.join(text)
                        # print(text)
                        return text
        else:
            if name.upper() == line_ziped[0].upper():
                line = line.split(' : ')
                text = [
                '\n',
                f'  <b>Имя</b>: {line[0]}',
                f'  <b>Ссылка</b>: {line[1]}'
                ]
                text = '\n'.join(text)
                # print(text)
                return text
    return f'<b>Преподатель с такой фамилией не найден!</b>\nПопробуйте еще раз'

find_teacher('gdfgdfg')
