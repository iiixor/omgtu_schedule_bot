from asyncio import streams
import json
import os
import re

dates = ["12","13","14","15","16","17","18","19","20","21","22","23","24","25"]

for day in dates:
    for i in range(1001):
        # print(i)
        with open (f'jsons/2022.09.{day}_№{i}.json') as file:
            json_dict = json.load(file)
            if json_dict == []:
                os.remove(f"jsons/2022.09.{day}_№{i}.json")
                continue

            try:
                for i in json_dict:
                    stream = i['stream']
                    group = i["group"]
                    sub_group = i["subGroup"]
                    if group == None and stream == None and sub_group == None:
                        os.remove(f"jsons/2022.09.{day}_№{i}.json")

                    if group != None:
                        if '/' in group:
                            group = re.sub('/',r';',group)
                        os.rename(f"jsons/2022.09.{day}_№{i}.json",f"jsons/2022.09.{day}_{group}.json")
                    elif stream != None:
                        stream = re.sub('/',r';',stream)
                        os.rename(f"jsons/2022.09.{day}_№{i}.json",f"jsons/2022.09.{day}_{stream}.json")
                    elif sub_group != None:
                        sub_group = re.sub('/',r';',sub_group)
                        os.rename(f"jsons/2022.09.{day}_№{i}.json",f"jsons/2022.09.{day}_{sub_group}.json")

            except KeyError:
                print(f'{day}.{i}')
                continue
                

