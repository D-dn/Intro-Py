
# data.json - файл с данными о некоторых математиках прошлого.
# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.

import json


def read_json_file(filename):
    with open(filename, "r") as json_file:
        data = json.load(json_file)
    return data
my_dict_list = read_json_file("data.json")
print(my_dict_list)

# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.
#
def key_sort_by_surname(obj_dict):
    whole_name = obj_dict["name"]
    name = whole_name.split(" ")[-1]
    return name

my_result = sorted(my_dict_list, key=key_sort_by_surname)

print(my_result)
