import json
from tokenize import group
dates = ["03","04","05","06","07","08","09","10","11","12","13","14","15","16"]

all_subs = {}

for day in dates:
    for i in range(1,1000):
        try:
            with open (f'jsons/file_2022.10.{day}_№{i}.json') as file:
                dict = json.load(file) 

                
                for dic in dict:
                    # print(dic)
                    try: 
                        sub_group = dic['subGroup']
                        if sub_group == None:
                            continue
                        all_subs[sub_group] = i
                        # print(f'{sub_group} - {i}')
                    except TypeError:
                        continue
        except FileNotFoundError:
            break



with open('all_groups.json') as file:
    dict = json.load(file) 


    for line in all_subs.items():
        group = line[0]
        id = line[1]
        dict[group] = line[1]
                    
    for line in dict.items():
        dict[line[0]] = str(line[1])
        

with open("all_groups.json",'w') as file:
    json.dump(dict,file,ensure_ascii=False)

