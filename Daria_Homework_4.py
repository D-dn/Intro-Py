################################### №1
my_list = [2, 400, 52, 560, 82, 14]
for symbol in my_list:
    if symbol > 100:
        print(symbol)

################################### №2
my_list = [2, 400, 52, 560, 82, 14]
my_result = []
for symbol in my_list:
        if symbol > 100:
            my_result.append(symbol)
print(my_result)

################################### №3
my_list = [2, 22, 54, 124, 1, 2]
if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(my_list[-1] + my_list[-2])
print(my_list)

#################################### №4
value = input("Ввелите число с точкой:")

try:
    value = float(value)
    print(value ** -1)
except (ValueError, ZeroDivisionError):
    print("Неверный ввод")

#################################### №5

my_list = [1, 11, 20, 100]
for index, symbol in enumerate(my_list):
    if not (index + symbol) % 2:
        print(symbol)

#################################### №6
my_list = [1, 11, 20, 100]
my_list_2 = [3, 33, 30, 300]
for index in range(len(my_list)):
        print(my_list[index], my_list_2[index])

###############  or  ##################### №6
my_list = [1, 11, 20, 100]
my_list_2 = [3, 33, 30, 300]
for index, symbol in enumerate(my_list):
    print(my_list[index], my_list_2[index])

#################################### №7
my_string_1 = "0123456789"
my_string_2 = "0123456789"
for symb_1 in my_string_1:
	for symb_2 in my_string_2:
		print(int(symb_1 + symb_2))