import requests
import fake_useragent
from bs4 import BeautifulSoup

all_teachers_id = []

with open('core/all_teachers.txt', 'r') as file:
    all_teachers = file.readlines()
    for line in all_teachers:
        line = line.replace('\n','')
        line = line.split(' : ')
        full_name = line[0].split()
        full_name[0] = full_name[0].upper()
        full_name[1] = full_name[1][0].upper()
        try:
            full_name[2] = full_name[2][0].upper()
        except IndexError:
            continue
        full_name = f'{full_name[0]} {full_name[1]}.{full_name[2]}.'
        link = f"https://rasp.omgtu.ru/api/search?term={full_name}&type=person"
        responce = requests.get(link).text
        soup = BeautifulSoup(responce, 'lxml')
        responce=responce.split(',')
        for id in responce:
            if '"id"' in id:
                if 'null' not in id:
                    id = id.replace('"','')
                    id = id.replace('id:','')
                    id = id.replace('\/','/')
                    id = id.replace('[','')
                    id = id.replace('{','')
                    all_teachers_id.append(f'{full_name} : {id}')
                    all_teachers_id = list(set(all_teachers_id))

sum = 0
#
with open('all_teachers_id.txt','w') as f:
    for line in all_teachers_id:
        if 'null' in line:
            continue
        else:
            sum+=1
            f.write(f'{line}\n')
