import requests
import fake_useragent
from bs4 import BeautifulSoup

all_teachers_id = []

with open('all_teachers.txt', 'r') as file:
    all_teachers = file.readlines()
    for line in all_teachers:
        line = line.replace('\n','')
        line = line.split(' : ')
        # print(line[0])
        full_name = line[0].split()
        print(full_name)
        full_name[0] = full_name[0].upper()
        full_name[1] = full_name[1][0].upper()
        try:
            full_name[2] = full_name[2][0].upper()
        except IndexError:
            continue
        full_name = f'{full_name[0]} {full_name[1]}.{full_name[2]}.'
        print(full_name)
        link = f"https://rasp.omgtu.ru/api/search?term={full_name}&type=person"
        responce = requests.get(link).text
        soup = BeautifulSoup(responce, 'lxml')
        responce=responce.split(',')
        # print(link, end='\r')
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
                    print(f'{full_name} : {id}')
                    # print(line)
                    # print(i)
        # print(link)

        # name = full_name[0]
        # second_name = full_name[1]
        # third_name = full_name[2]


# for i in range(1,1000):
#     link = f"https://rasp.omgtu.ru/api/schedule/person/{i}?start=2022.09.05&finish=2022.09.05&lng=2"
#     responce = requests.get(link).text
#     soup = BeautifulSoup(responce, 'lxml')
#     print(link)
#
#
#     # block = soup.find('span', class_ = 'objectBox objectBox-string')
#     responce=responce.split(',')
#     for line in responce:
#         if '"lecturer_title"' in line:
#             if 'null' not in line:
#                 line = line.replace('"','')
#                 line = line.replace('group:','')
#                 line = line.replace('\/','/')
#                 all_teachers_id.append(f'{line} : {i}')
#                 all_teachers_id = list(set(all_teachers_id))
#                 print(line)
#                 print(i)
# print()
#
sum = 0
#
with open('all_teachers_id.txt','w') as f:
    for line in all_teachers_id:
        if 'null' in line:
            continue
        else:
            sum+=1
            f.write(f'{line}\n')
            print(f'{line}')
