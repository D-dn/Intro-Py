# 1. Написать функцию, которая генерирует и возвращает строку случайной длинны.
# Минимальную и максимальную длину строки ограничить с помощью параметров min_limit, max_limit, передаваемых в функцию.
import random
import string


def create_str(min_limit, max_limit):
    str_len = random.randint(min_limit, max_limit)
    my_str = string.ascii_letters[:str_len:]
    return my_str


print(create_str(2, 5))

#################################################################
# 2. Даны списки names и domains (создать самостоятельно).
# Написать функцию create_email для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# Обязательные параметры функции: names и domains.
# Параметры по умолчанию: границы генерируемого числа (100, 999), границы генерируемой строки (5, 7)
#
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
# Буквы в строке МОГУТ повторяться.
#
# Пример:
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)

names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
from random import randint, choice
import string
name = choice(names)
domain = choice(domains)
numb = randint(100, 999)
len_str = randint(5, 7)
alphabet = string.ascii_lowercase
my_str = "".join([choice(alphabet) for _ in range(len_str)])

def create_email(domains, names):
    email = name + str(numb) + "@" + my_str + "." + domain
    return email

print(create_email(domains, names))
