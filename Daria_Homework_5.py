##################################
# # 1. Дано целое число (int). Определить сколько нулей в этом числе.

my_number = 546546128058505050359
my_number = str(my_number)
result = my_number.count("0")
print(result)

##################################
# 2. Дано целое число (int). Определить сколько нулей в конце этого числа.

my_number = 64500087942000000
my_str = str(my_number)
my_str = my_str[::-1]
my_value = 0

for symbol in my_str:
    if int(symbol) == 0:
        my_value = (my_value + 1)
    elif int(symbol) > 0:
        break
print(my_value)

# # 3a. Даны списки my_list_1 и my_list_2.
# # Создать список my_result в который вначале поместить
# # элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.

my_list_1 = [0, 8, 0, 5, 0]
my_list_2 = [5, 1, 9, 1, 8]
my_result = my_list_1[::2]
for index, symbol in enumerate(my_list_2):
   if index % 2:
      my_result.append(symbol)
print(my_result)

# # 3b. Даны списки my_list_1 и my_list_2. Создать список my_result в который
# # вначале поместить четные элементы (ИМЕННО ЭЛЕМЕНТЫ) из my_list_1 и потом нечетные элементы из my_list_2.
# # my_list_1 = [1,3,2,4,5], my_list_2 = [10, 20, 15, 25, 22] -> my_result [2, 4, 15, 25]

my_list_1 = [1, 3, 2, 4, 5]
my_list_2 = [10, 20, 15, 25, 22]
my_result = []

for symbol in my_list_1:
    if not symbol % 2:
        my_result.append(symbol)
for symbol in my_list_2:
    if symbol % 2:
        my_result.append(symbol)
print(my_result)

# # 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# # стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]

my_list = [1, 2, 3, 4]
new_list = my_list[1:]
new_list.append(my_list[0])
print(new_list)

# # 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# # [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

my_list = [1, 2, 3, 4, 5, 8, 9, 11]
my_list.append(my_list.pop(0))
print(my_list)

# # # 6. Дана строка в которой есть числа (разделяются пробелами).
# # # Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# # # Для данного примера ответ - 133.

my_string = "43 больше чем 34 но меньше чем 56"
my_result = []
my_string = my_string.split( )
for symbol in my_string:
    if symbol.isdigit():
        my_result.append(int(symbol))
print(sum(my_result))

# 7. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# # быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']

my_str = "gfhjks;glhjghsdls;dfkjkp"
my_list_1 = []
if len(my_str) % 2:
   my_str = my_str + '_'
for index, symbol in enumerate(my_str):
   my_list_1.append(my_str[index:(index+2)])
   my_list = my_list_1[::2]
print(my_list)

# 8. Дана строка my_str в которой символы не повторяются и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить часть строки между этими символами.
# my_str = "My_long str", l_limit = "o", r_limit = "t" -> sub_str = "ng s"

my_str = "My_long str"
l_limit = "o"
r_limit = "t"
res_1 = my_str.find(l_limit) + 1
res_2 = my_str.find(r_limit)
sub_str = my_str[res_1:res_2]
print(sub_str)

# 9. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

my_str = "My long string"
l_limit = "o"
r_limit = "g"
sub_str = my_str[my_str.find(l_limit) + 1 : my_str.rfind(r_limit)]
print(sub_str)

# 10. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.

my_list = [2, 4, 1, 5, 3, 9, 0, 7]
my_result = 0

for index, symbol in enumerate(my_list[1:]):
    if my_list[index] > (my_list[index-1] + my_list[index+1]):
        my_result += 1
print(my_result)

