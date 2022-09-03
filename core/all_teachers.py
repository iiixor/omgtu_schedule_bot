import requests
import fake_useragent
from bs4 import BeautifulSoup

all_teachers_list = []

for i in range(30):
    print(i)
    link = f"https://omgtu.ru/ecab/persons/index.php?b={i}"
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    block = soup.find_all('div', style = 'padding: 5px; font-size: 120%;')
    for line in block:
        teacher_url = line.find('a').get('href')
        name = line.text
        name = name.replace('\n','')
        name = name.strip()
        print(f'{name} : {teacher_url}')
        all_teachers_list.append(f'{name} : https://omgtu.ru/ecab/persons/{teacher_url}')


print(all_teachers_list)

all_teachers_list = list(set(all_teachers_list))
    # if block != None:
    #     print(block.text)


    # block = soup.find('span', class_ = 'objectBox objectBox-string')
#     responce=responce.split(',')
#     for line in responce:
#         if '"group"' in line:
#             line = line.replace('"','')
#             line = line.replace('group:','')
#             all_groups.append(f'{line} : {i}')
#             all_groups = list(set(all_groups))
#             print(line)
#             print(i)
#
#
# print()
#
# sum = 0
#
with open('core/all_teachers.txt','w') as f:
    for line in all_teachers_list:
        f.write(f'{line}\n')
        print(f'{line}')
