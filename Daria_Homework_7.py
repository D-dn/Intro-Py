############################################################
#1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
# Задание можно выполнить и через обычный цикл и через генератор списков.

import random as rnd
from random import randint
my_list = []

while int(len(my_list)) < 20:
    my_list.append(randint(1, 100)),

print(my_list)

############################################################
# 2) Создать словарь triangle в который записать точки A B C (ключи),
# и их координаты - кортежи (значения), созданные случайным образом с помощью модуля random в диапазоне от -10 до 10 по каждой оси.

triangle = {"A": (randint(-10,10), randint(-10,10)),
            "B": (randint(-10,10), randint(-10,10)),
            "c": (randint(-10,10), randint(-10,10))}
print(triangle)

############################################################
