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

##################################################
# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.

my_str = "asdfgahfghjkl"

my_list = []
my_set = set(my_str)
for symbol in my_set:
    if my_str.count(symbol) == 1:
        my_list.append(symbol)
        print(my_list)

# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
 
my_str_1 = "gaudeamus igitur"
my_str_2 = "igitur"

my_set_1 = set(my_str_1)
my_set_2 = set(my_str_2)

my_list = [my_set_1.intersection(my_set_2)]
print(my_list)


