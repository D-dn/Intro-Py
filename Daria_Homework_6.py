##################################################
# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate.

my_list = ['qwe', 'rty', 'uio', 'opd', 'ljh']
new_list = [0]
for index, symbol in enumerate(my_list):
    if not index % 2:
        new_list.append(symbol)
    elif index % 2:
        new_list.append(symbol[::-1])
print(new_list)

##################################################
# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".

my_list = ['awe', 'rtay', 'uioa', 'aopd', 'lajh']
new_list = []
for symbol in my_list:
    if symbol[0] == "a":
        new_list.append(symbol)
print(new_list)

##################################################

3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.

my_list = ['gkfa', "dgafsd", "ajvlkd"]
new_list = []
for symbol in my_list:
    if 'a' in symbol:
        new_list.append(symbol)

print(new_list)

##################################################
# 4. Дан список my_list в котором могум быть как строки (type str) так и целые числа (type int).
# Создать новый список в который поместить только строки из my_list.

my_list = ['dyn', 456, 'fdgds', 123, 'jvgl.']
new_list = []
for symbol in my_list:
    if type(symbol) == str:
        new_list.append(symbol)
print(new_list)
