"""
Запускаем этот файл,
"""
num_typos = 5

from read_dict_n_create_top import start
from generate import generate_typos
from json_maker import add_phrases
import json



all = []
json_list = []
top_dict = start()

for el in top_dict:
    if len(el) > 2:
        all.append(generate_typos(el,num_typos))


for el in all:
    
    json_list.append(add_phrases(el))
    
        

def create_json_file(data, file_name):
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

create_json_file(json_list, 'intent.json')