############################################################
#1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
# Задание можно выполнить и через обычный цикл и через генератор списков.

from random import randint
my_list = []

while int(len(my_list)) < 20:
    my_list.append(randint(1, 100)),

print(my_list)

############################################################
# 2) Создать словарь triangle в который записать точки A B C (ключи),
# и их координаты - кортежи (значения), созданные случайным образом с помощью модуля random в диапазоне от -10 до 10 по каждой оси.
from random import randint
triangle = {"A": (randint(-10,10), randint(-10,10)),
            "B": (randint(-10,10), randint(-10,10)),
            "c": (randint(-10,10), randint(-10,10))}
print(triangle)

########################## или ################################## 
from random import randint

def get_tuple():
    my_tuple = randint(-10, 10), randint(-10, 10)
    return my_tuple

triangle = {"A": get_tuple(),
            "B": get_tuple(),
            "C": get_tuple()}

print(triangle)

############################################################
# 3) Создать функцию my_print, которая принимает в виде параметра строку и печатает ее
# с тремя символами * вначале и в конце строки.
# Пример:
# my_str = 'I'm the string'
# Печатает ***I'm the string***

my_str = ";jkkl"
def my_print(my_str):
    print("***" + my_str + "***")
my_print(my_str)


############################################################
4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.

my_dict_list = [{"name": "John", "age": 15}, {"name": "Stephen", "age": 25},{"name": "Jack", "age": 45}]
ages = []
for index, dictionnary in enumerate(my_dict_list):
    for key, value in dictionnary.items():
        if key == "age":
            ages.append(value)
            if value == min(ages):
                 print(dictionnary["name"])
                    
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
НЕ РАБОТАЕТ, если длина имени совпадает 
my_dict_list = [{"name": "John", "age": 15}, {"name": "Stephen", "age": 25},{"name": "Jack", "age": 45}]
len_name = []
for dictionnary in my_dict_list:
    for key, value in dictionnary.items():
        if key == "name":
            len_name.append((len(value)))

for index, symbol in enumerate(len_name):
    if symbol == max(len_name):

        my_seq = my_dict_list[index]

print(my_seq["name"])

# в) Посчитать среднее количество лет всех людей из списка.
my_dict_list = [{"name": "John", "age": 15}, {"name": "Stephen", "age": 52}, {"name": "Jack", "age": 45}]
my_int = 0
my_numb = len(my_dict_list)
for dictionnary in my_dict_list:
    for key, value in dictionnary.items():
        # print(value)
            if type(value) == int:
                my_int += value
average_age = my_int/my_numb
print(average_age)

############################################################
# 5) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.

my_dict_1 = {"Какао": "20г", "Сахар": "100г", "Ваниль": "100г", "Масло": "100г"}
my_dict_2 = {"Сахар": "200г", "Масло": "100г", "Сметана": "100г"}
my_set_1 = set(my_dict_1)
my_set_2 = set(my_dict_2)
my_list = my_set_1.intersection(my_set_2)

# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
my_list_2 = list(my_set_1.difference(my_set_2))
print(my_list_2)

# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
new_dict = {}
for key, value in my_dict_1.items():
    if key not in my_dict_2:
        new_dict.update({key: value})
print(new_dict)

# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
new_dict_1 = {}

for key, value in my_dict_1.items():
    if key not in my_list:
        new_dict_1.update({key: value})
for key, value in my_dict_2.items():
    if key not in my_list:
        new_dict_1.update({key: value})
    else:
        new_dict_1.update({key: [my_dict_1[key], my_dict_2[key]]})
