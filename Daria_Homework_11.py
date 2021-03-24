

# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.

import json
#
#
def read_json_file(filename):
    with open(filename, "r") as json_file:
        data = json.load(json_file)
    return data
my_dict_list = read_json_file("data.json")
print(my_dict_list)

#############################################################
# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.

def key_sort_by_surname(obj_dict):
    full_name = obj_dict["name"]
    name = full_name.split(" ")[-1]
    return name

my_result = sorted(my_dict_list, key=key_sort_by_surname)

print(my_result)

#############################################################
# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.
import re

def key_sort_by_year(obj_dict):
    years = obj_dict["years"]
    dates = re.findall(r"[0-9]+", years)

    if years.find("BC") > 0:
        return int(dates[-1]) * -1

    else :
        return int(dates[-1])

my_result2 = sorted(my_dict_list, key = key_sort_by_year)

print(my_result2)

#############################################################
# 4. Написать функцию сортировки по количеству слов в поле "text"

def key_sort_by_text_len(obj_dict):
    my_text = obj_dict["text"]
    my_len = len(list(my_text.split(" ")))
    return my_len


my_result3 = sorted(my_dict_list, key=key_sort_by_text_len)

print(my_result3)
