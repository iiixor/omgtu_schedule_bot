import requests
import fake_useragent
from bs4 import BeautifulSoup

all_groups = []

for i in range(1,1000):
    link = f"https://rasp.omgtu.ru/api/schedule/group/{i}?start=2022.08.29&finish=2022.09.04&lng=1"
    responce = requests.get(link).text
    soup = BeautifulSoup(responce, 'lxml')
    print(link)


    # block = soup.find('span', class_ = 'objectBox objectBox-string')
    responce=responce.split(',')
    for line in responce:
        if '"subGroup"' in line:
            if 'null' not in line:
                line = line.replace('"','')
                line = line.replace('group:','')
                line = line.replace('\/','/')
                all_groups.append(f'{line} : {i}')
                all_groups = list(set(all_groups))
                print(line)
                print(i)
print()

sum = 0

with open('all_groups_2.txt','w') as f:
    for line in all_groups:
        if 'null' in line:
            continue
        else:
            sum+=1
            f.write(f'{line}\n')
            print(f'{line}')

# block = soup.find('div', class_ = 'pythagoras-square-table')
#
# values = block.find_all('td')
# title = soup.find('div', class_ = 'pythagoras-square-title')
# title = title.text
